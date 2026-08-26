# -*- coding: utf-8 -*-
"""Prueba de orcid_sync.py con respuestas simuladas (no toca la red).

Adaptado del test de Neurosistemas. Diferencia importante: data/orcid.yaml
de LAB ONCE solo trae UN miembro real (el director), a propósito (ver la
nota en ese archivo). Por eso esta prueba NO reutiliza las filas de
producción — arma su propia configuración temporal con dos miembros de
prueba, corre el sincronizador contra ella, y al final restaura el
orcid.yaml real tal como estaba.

Uso:  python scripts/test_orcid_sync.py
Deja data/orcid.yaml y data/publicaciones_orcid.json tal como estaban.
"""
import sys, os, json, io
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, "scripts"))

import yaml

cfg_path = os.path.join(R, "data", "orcid.yaml")
backup = io.open(cfg_path, encoding="utf-8").read()
cfg_real = yaml.safe_load(backup)

# El test sobreescribe data/publicaciones_orcid.json con datos ficticios, así que
# hay que respaldarlo igual que orcid.yaml: si no, borra el resultado real de una
# corrida previa de scripts/orcid_sync.py y el sitio se queda sin publicaciones.
json_path = os.path.join(R, "data", "publicaciones_orcid.json")
SEMILLA = '{\n  "actualizado": "",\n  "fuentes": [],\n  "publicaciones": []\n}\n'
backup_json = io.open(json_path, encoding="utf-8").read() if os.path.exists(json_path) else SEMILLA

# Config de prueba: dos miembros ficticios, opciones tomadas de la config
# real (para probar con el anio_minimo/tipos_aceptados reales del sitio).
cfg_prueba = {
    "miembros": [
        {"nombre": "Miembro de Prueba Uno", "orcid": "0000-0000-0000-0001", "apellidos": ["UnoApellido"]},
        {"nombre": "Miembro de Prueba Dos", "orcid": "0000-0000-0000-0002", "apellidos": ["DosApellido"]},
    ],
    "opciones": cfg_real.get("opciones", {}),
}
io.open(cfg_path, "w", encoding="utf-8").write(yaml.dump(cfg_prueba, allow_unicode=True, sort_keys=False))

import orcid_sync

WORKS = {
 "0000-0000-0000-0001": {"group": [
   {"external-ids": {"external-id": [{"external-id-type": "doi", "external-id-value": "https://doi.org/10.1038/S41598-025-99999-9"}]},
    "work-summary": [{"title": {"title": {"value": "Active vision in freely moving observers"}},
                      "journal-title": {"value": "Scientific Reports"},
                      "publication-date": {"year": {"value": "2025"}}, "type": "journal-article"}]},
   # duplicado exacto, debe colapsar con el de "Miembro de Prueba Dos"
   {"external-ids": {"external-id": [{"external-id-type": "doi", "external-id-value": "10.1016/j.mex.2024.102500"}]},
    "work-summary": [{"title": {"title": {"value": "A shared methods paper"}},
                      "journal-title": {"value": "MethodsX"},
                      "publication-date": {"year": {"value": "2024"}}, "type": "journal-article"}]},
   # ya está en el histórico -> debe descartarse (ver DOI en publicaciones_historicas.yaml real)
   {"external-ids": {"external-id": [{"external-id-type": "doi", "external-id-value": "10.1038/s41598-025-25065-6"}]},
    "work-summary": [{"title": {"title": {"value": "Increased basal ganglia volume in older adults with tinnitus"}},
                      "journal-title": {"value": "Sci Rep"},
                      "publication-date": {"year": {"value": "2025"}}, "type": "journal-article"}]},
   # tipo no aceptado -> descartar
   {"external-ids": {"external-id": []},
    "work-summary": [{"title": {"title": {"value": "Una charla"}}, "publication-date": {"year": {"value": "2025"}},
                      "type": "lecture-speech"}]},
   # sin DOI pero válido -> se conserva por título
   {"external-ids": {"external-id": []},
    "work-summary": [{"title": {"title": {"value": "Un capítulo sin DOI"}},
                      "journal-title": {"value": "Editorial X"},
                      "publication-date": {"year": {"value": "2025"}}, "type": "book-chapter"}]},
 ]},
 "0000-0000-0000-0002": {"group": [
   {"external-ids": {"external-id": [{"external-id-type": "doi", "external-id-value": "10.1016/J.MEX.2024.102500"}]},
    "work-summary": [{"title": {"title": {"value": "A shared methods paper"}},
                      "journal-title": {"value": "MethodsX"},
                      "publication-date": {"year": {"value": "2024"}}, "type": "journal-article"}]},
 ]},
}
CROSSREF = {
 "10.1038/s41598-025-99999-9": {"message": {
   "author": [{"family": "DosApellido", "given": "Otro"}, {"family": "Pérez", "given": "Ana María"},
              {"family": "UnoApellido", "given": "Alguien"}],
   "container-title": ["Scientific Reports"], "volume": "15", "page": "1234",
   "issued": {"date-parts": [[2025, 4, 2]]}, "title": ["Active vision in freely moving observers"]}},
 "10.1016/j.mex.2024.102500": {"message": {
   "author": [{"family": "UnoApellido", "given": "Alguien"}, {"family": "DosApellido", "given": "Otro"}],
   "container-title": ["MethodsX"], "volume": "12", "page": "102500",
   "issued": {"date-parts": [[2024]]}, "title": ["A shared methods paper"]}},
}

def pedir_falso(s, url, intentos=3, espera=2.0):
    if url.startswith(orcid_sync.ORCID_API):
        return WORKS.get(url.split("/")[-2])
    if url.startswith(orcid_sync.CROSSREF_API):
        return CROSSREF.get(url.split("works/")[-1])
    return None

orcid_sync.pedir = pedir_falso
orcid_sync.PAUSA = 0
rc = orcid_sync.main()

print("\n--- JSON generado ---")
doc = json.load(io.open(os.path.join(R, "data", "publicaciones_orcid.json"), encoding="utf-8"))
print(json.dumps(doc, ensure_ascii=False, indent=2)[:2200])

pubs = doc["publicaciones"]
ok = True
def chk(cond, msg):
    global ok
    print(("  ✓ " if cond else "  ✗ ") + msg); ok = ok and cond

print("\n--- Aserciones ---")
chk(len(pubs) == 3, f"3 publicaciones tras filtrar y deduplicar (obtuve {len(pubs)})")
chk(all(p["anio"] >= 2024 for p in pubs), "ninguna anterior a lo esperado")
chk(not any("basal ganglia" in p["titulo"].lower() for p in pubs), "descarta lo que ya está en el histórico real (por DOI)")
chk(not any("charla" in p["titulo"].lower() for p in pubs), "descarta tipos no aceptados")
compartida = [p for p in pubs if "shared" in p["titulo"].lower()]
chk(len(compartida) == 1, "el DOI compartido aparece una sola vez")
chk(len(compartida[0]["miembros"]) == 2, f"acredita a los 2 miembros de prueba ({compartida[0]['miembros']})")
sr = [p for p in pubs if "Active vision" in p["titulo"]][0]
chk("<b>DosApellido, O.</b>" in sr["autores"] and "<b>UnoApellido, A.</b>" in sr["autores"],
    "resalta en negrita a los miembros de prueba")
chk("Pérez, A. M." in sr["autores"] and "<b>Pérez" not in sr["autores"], "no resalta a autores externos")
chk(sr["revista"] == "Scientific Reports, 15, 1234", f"revista con volumen y páginas: {sr['revista']}")
chk(sr["doi"] == "10.1038/s41598-025-99999-9", "DOI normalizado a minúsculas y sin prefijo URL")
chk(pubs[0]["anio"] >= pubs[-1]["anio"], "ordenado por año descendente")
chk(doc["actualizado"] != "", "registra la fecha de actualización")

# Prueba de resiliencia: ORCID caído -> conserva el JSON anterior
print("\n--- Resiliencia (ORCID caído) ---")
antes = io.open(os.path.join(R, "data", "publicaciones_orcid.json"), encoding="utf-8").read()
orcid_sync.pedir = lambda *a, **k: None
orcid_sync.main()
despues = io.open(os.path.join(R, "data", "publicaciones_orcid.json"), encoding="utf-8").read()
chk(antes == despues, "con ORCID caído no borra el JSON existente")

# Restaurar ambos archivos reales tal como estaban antes del test
io.open(cfg_path, "w", encoding="utf-8").write(backup)
io.open(json_path, "w", encoding="utf-8").write(backup_json)
print("\norcid.yaml y publicaciones_orcid.json restaurados a su estado previo.")
print("\nRESULTADO:", "TODO OK" if ok else "HAY FALLAS")
sys.exit(0 if ok else 1)
