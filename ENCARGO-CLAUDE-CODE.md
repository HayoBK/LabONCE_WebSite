# ENCARGO para Claude Code — Sincronización ORCID en LAB ONCE

Este archivo lo escribió Cowork (el "cerebro"). Tú eres las manos: tienes Hugo, git y red
abierta. Ejecuta las tareas en orden y no pases a la siguiente si la anterior no quedó en verde.
Si algo de lo que sigue te parece mal pensado, dímelo antes de improvisarlo.

## Qué cambió (resumen)

Se replicó en LAB ONCE el sistema de publicaciones automáticas vía ORCID que ya funciona en
`~/Git_Web/Neurosistemas`, con tres decisiones importantes ya conversadas y aprobadas por Hayo:

1. **Equipo migrado a páginas individuales.** `data/integrantes.yaml` deja de ser la fuente del
   equipo. Ahora cada persona es un archivo en `content/integrantes/<slug>.md`, con su propia
   URL. `data/integrantes.yaml` queda como referencia histórica sin uso — puedes hacer
   `git rm data/integrantes.yaml` una vez que confirmes visualmente que `/integrantes/` se ve
   bien, o dejarlo un tiempo por si hay que comparar algo.
2. **ORCID solo para el director.** `data/orcid.yaml` trae únicamente a Hayo Breinbauer
   (`0000-0002-3278-065X`) — es intencional, está documentado dentro del archivo y en
   `INFORME-ORCID-LABONCE.md`. El resto del equipo puede tener su propio `orcid` en su ficha
   (link a su perfil), sin que eso dispare sincronización.
3. **Publicaciones destacadas con más detalle + portada rediseñada.** `/publicaciones/` (la
   antigua vitrina de 6 papers) ahora muestra año y factor de impacto (campo nuevo,
   `factor_impacto`, vacío por ahora) además del abstract e imagen que ya tenía.
   `/publicaciones/todas/` reemplaza el fetch en JavaScript (que solo cubría el perfil personal
   de Hayo y no cargaba en buscadores) por el listado automático fusionado (ORCID + archivo
   histórico), con buscador y agrupado por año. La portada cambió su bloque de "Publicaciones
   destacadas" (3 tarjetas) por "Publicaciones de los últimos años", con conteos automáticos de
   los últimos 5 y 10 años.

## Paso 0 — un archivo que TIENES que crear tú, no llegó por el puente

El puente que uso para escribir en tu carpeta rechaza por seguridad los archivos dentro de
`.github/workflows/` ("protected file"). Todo lo demás de este encargo ya está escrito en el
repo; falta únicamente este archivo. Créalo tú con este contenido exacto:

`.github/workflows/orcid.yml`:
```yaml
name: Sincronizar publicaciones desde ORCID

on:
  schedule:
    # Todos los días a las 08:10 UTC (~05:10 hora de Chile)
    - cron: '10 8 * * *'
  workflow_dispatch:

permissions:
  contents: write

jobs:
  sincronizar:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Instalar Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Instalar dependencias
        run: pip install requests PyYAML

      - name: Consultar ORCID
        run: python scripts/orcid_sync.py

      - name: Commitear cambios si los hay
        run: |
          git config user.name  "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          if [[ -n "$(git status --porcelain data/publicaciones_orcid.json)" ]]; then
            git add data/publicaciones_orcid.json
            git commit -m "chore(orcid): actualización automática de publicaciones"
            git push
          else
            echo "Sin cambios en las publicaciones ORCID."
          fi
```
Es una copia exacta del que ya funciona en `~/Git_Web/Neurosistemas/.github/workflows/orcid.yml`
(mismo horario, mismo flujo). Si prefieres, cópialo directo desde ahí en vez de transcribirlo.

## Archivos nuevos

```
data/orcid.yaml
data/publicaciones_historicas.yaml        (migrado desde el listado curado que vivía en todas.md)
data/publicaciones_orcid.json             (semilla vacía, la llena el sincronizador)
content/integrantes/*.md                  (13 fichas, una por integrante)
layouts/integrantes/single.html
layouts/publicaciones/todas.html
layouts/partials/pub-merge.html
layouts/partials/publicacion.html
scripts/orcid_sync.py
scripts/test_orcid_sync.py
scripts/verify_static.py
.github/workflows/orcid.yml
INFORME-ORCID-LABONCE.md
ENCARGO-CLAUDE-CODE.md                    (este archivo)
```

## Archivos modificados

```
layouts/integrantes/list.html   (ahora agrupa .Pages en vez de site.Data.integrantes)
layouts/publicaciones/list.html (agrega anio + factor_impacto, ordena por año)
layouts/index.html              (equipo enlaza a fichas; nueva sección de publicaciones recientes)
content/publicaciones/todas.md  (ahora casi vacío: front-matter + layout "todas")
data/publicaciones_seleccionadas.yaml  (agrega campo factor_impacto, vacío, a las 6 entradas)
static/css/labonce.css          (2 líneas: las tarjetas de equipo ahora son <a>, sin subrayado)
.pages.yml                      (colección "integrantes" pasa a content/integrantes; se agregan
                                  las colecciones "orcid" y "publicaciones_historicas"; se agrega
                                  factor_impacto a "publicaciones")
```

Ya se corrió `python scripts/verify_static.py` y `python scripts/test_orcid_sync.py` desde
Cowork (sin poder compilar Hugo) — ambos en verde, 0 errores. Aun así, hazlo tú de nuevo apenas
tengas el repo actualizado, por si algo se perdió en la copia.

## Tareas, en orden

### A. Verificación estática (de nuevo, ya con el repo completo)
```bash
python scripts/verify_static.py
```
Debe dar 0 errores. Si hay avisos de "posible ruta absoluta", revísalos — pueden ser falsos
positivos dentro de comentarios.

### B. Primera compilación real
```bash
HUGO_ENVIRONMENT=production hugo --minify
```
Sin `ERROR` = verde. Después:
```bash
hugo server -D
```
Revisa especialmente:
- `/integrantes/` — que los 5 grupos se vean, con las 13 fichas, y que cada tarjeta lleve a su
  página individual.
- La ficha de Hayo Breinbauer en particular: debería mostrar el chip ORCID y (después del paso C)
  su sección de "Producción científica".
- Las fichas de Paul Délano y Pablo Pozo: deberían mostrar el chip ORCID (sin sección de
  publicaciones propia, por diseño — ver el punto 2 de arriba).
- `/publicaciones/` — 6 tarjetas con año, factor de impacto (vacío, se ve como nada, no debería
  romper el layout) y abstract.
- `/publicaciones/todas/` — agrupado por año, buscador funcionando, con el ORCID de Hayo y las
  45 referencias históricas fusionadas sin duplicados.
- La portada (`/`) — bloque nuevo "Publicaciones de los últimos años" con los tres contadores.

### C. Corre el sincronizador de verdad
```bash
pip install requests PyYAML
python scripts/orcid_sync.py
```
Revisa a ojo `data/publicaciones_orcid.json`: años correctos, sin duplicados con el histórico
(en particular que NO aparezcan de nuevo las 3 publicaciones del histórico que sí tienen DOI:
`10.1038/s41598-025-25065-6`, `10.3389/fneur.2025.1599307`, `10.3390/brainsci14010016`).

### D. Corre el test del sincronizador
```bash
python scripts/test_orcid_sync.py
```
Debe terminar en "RESULTADO: TODO OK" y dejar `data/orcid.yaml` y
`data/publicaciones_orcid.json` exactamente como estaban (restaura ambos al final). Si el
sincronizador real del paso C generó datos, ese resultado real queda intacto — el test no lo
toca, solo usa un `orcid.yaml` temporal con miembros ficticios.

### E. Permisos de GitHub Actions (paso que se salta fácil y rompe todo en silencio)
En GitHub, repo `HayoBK/LabONCE_WebSite` → **Settings → Actions → General → Workflow
permissions → Read and write permissions**. Sin esto, `orcid.yml` va a leer ORCID
correctamente pero fallar al hacer `git push`, con un error de permisos que no es obvio.

### F. Commit y push
```bash
git add -A
git commit -m "feat(orcid): sincronización automática de publicaciones + fichas individuales de equipo"
git push
```
Esto dispara `deploy.yml` (ya existente, sin cambios). Espera a que quede verde:
```bash
gh run list --limit 5
```

### G. Disparar el workflow de ORCID una vez a mano
En GitHub: **Actions → Sincronizar publicaciones desde ORCID → Run workflow**. Verifica que
quede verde y que, si hay novedades, haga su propio commit automático.

## Al terminar

- Dime la URL funcionando, qué errores encontraste (si hubo) y cómo los resolviste.
- Actualiza `CONTINUACION-LABONCE.md` con el estado nuevo (fichas individuales + ORCID en
  producción) y anota los pendientes que quedaron: completar los ORCID del resto del equipo
  (ver `INFORME-ORCID-LABONCE.md`), confirmar si "Andrés Contreras" de Neurosistemas es la misma
  persona, y completar `factor_impacto` en `data/publicaciones_seleccionadas.yaml` cuando Hayo
  tenga esos datos a mano.
- No borres `data/integrantes.yaml` sin que Hayo lo confirme, aunque ya no se use.
