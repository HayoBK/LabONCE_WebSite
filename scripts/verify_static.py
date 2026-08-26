#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificación estática del sitio LAB ONCE, para correr antes de un build
real (que solo puede hacer Claude Code con el binario de Hugo). Atrapa los
errores más comunes sin necesitar compilar:

  1. YAML y JSON sintácticamente válidos.
  2. Front-matter con 'title' en cada content/*.md.
  3. Balance de acciones de bloque Hugo (if/with/range/define/block vs end).
  4. Partials referenciados por nombre existen en layouts/partials/.
  5. Rutas hardcodeadas ('/algo') en href/src, que deberían ir con relURL
     (se reportan como aviso, no como error: a veces son intencionales,
     p.ej. dentro de comentarios o ejemplos en la documentación del CMS).

Uso:  python scripts/verify_static.py
"""
import glob
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("Falta PyYAML. Instala con:  pip install PyYAML")
    sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errores = []
avisos = []


def rel(p):
    return os.path.relpath(p, ROOT)


# ---------------------------------------------------------------- 1) YAML/JSON
excluir_dirs = {"public", ".git", "node_modules", ".venv"}

def listar(patron):
    for p in glob.glob(os.path.join(ROOT, patron), recursive=True):
        if not any(f"{os.sep}{d}{os.sep}" in p for d in excluir_dirs):
            yield p

for path in list(listar("**/*.yaml")) + list(listar("**/*.yml")):
    try:
        with open(path, encoding="utf-8") as fh:
            yaml.safe_load(fh)
    except Exception as e:
        errores.append(f"YAML inválido: {rel(path)}: {e}")

for path in listar("**/*.json"):
    # layouts/ contiene plantillas Hugo que EMITEN json (p.ej. layouts/index.json,
    # el índice del buscador global): no son JSON parseable, se saltan.
    if rel(path).startswith("layouts" + os.sep):
        continue
    try:
        with open(path, encoding="utf-8") as fh:
            json.load(fh)
    except Exception as e:
        errores.append(f"JSON inválido: {rel(path)}: {e}")

# ---------------------------------------------------------------- 2) front-matter
for path in listar("content/**/*.md"):
    with open(path, encoding="utf-8") as fh:
        txt = fh.read()
    if not txt.startswith("---"):
        errores.append(f"Sin front-matter: {rel(path)}")
        continue
    fm_end = txt.find("\n---", 3)
    fm = txt[3:fm_end] if fm_end != -1 else txt[3:]
    try:
        data = yaml.safe_load(fm) or {}
    except Exception as e:
        errores.append(f"Front-matter YAML inválido: {rel(path)}: {e}")
        continue
    if "title" not in data:
        errores.append(f"Front-matter sin 'title': {rel(path)}")

# ---------------------------------------------------------------- 3) balance de bloques
ABREN = re.compile(r"{{-?\s*(if|with|range|define|block)\b")
CIERRAN = re.compile(r"{{-?\s*end\s*-?}}")
for path in listar("layouts/**/*.html"):
    with open(path, encoding="utf-8") as fh:
        txt = fh.read()
    abren = len(ABREN.findall(txt))
    cierran = len(CIERRAN.findall(txt))
    if abren != cierran:
        errores.append(f"Desbalance de bloques en {rel(path)}: {abren} aperturas vs {cierran} 'end'")

# ---------------------------------------------------------------- 4) partials referenciados
disponibles = {os.path.basename(p) for p in listar("layouts/partials/*.html")}
PARTIAL_REF = re.compile(r'partial\s+"([^"]+)"')
for path in listar("layouts/**/*.html"):
    with open(path, encoding="utf-8") as fh:
        txt = fh.read()
    for ref in PARTIAL_REF.findall(txt):
        nombre = ref.split("/")[-1]
        if nombre not in disponibles:
            errores.append(f"Partial referenciado pero no encontrado: '{ref}' en {rel(path)}")

# ---------------------------------------------------------------- 5) rutas absolutas (aviso)
HREF_ABS = re.compile(r'(?:href|src)="\/(?!\/)[^"]*"')
for path in listar("layouts/**/*.html"):
    with open(path, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            for m in HREF_ABS.finditer(line):
                avisos.append(f"Posible ruta absoluta en {rel(path)}:{i}: {m.group(0)}")

print(f"Revisado bajo {ROOT}")
print(f"\nErrores: {len(errores)}")
for e in errores:
    print("  ✗", e)
print(f"\nAvisos: {len(avisos)}")
for a in avisos:
    print("  !", a)

sys.exit(1 if errores else 0)
