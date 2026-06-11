# CONTINUACIÓN — Sitio LAB ONCE

Carpeta de trabajo: `E:\Git_Use_LabOnce`.
Sitio Hugo **autocontenido** que reemplaza el Wix `https://hayobk.wixsite.com/labonce`.
**EN VIVO:** `https://hayobk.github.io/LabONCE_WebSite/` (repo `github.com/HayoBK/LabONCE_WebSite`).
Última actualización: 2026-06-11 (rediseño logo arcoíris + porteo completo del Wix).

---

## ⚠️ CÓMO TRABAJAMOS — MODO DUAL
1. **El chat (Cowork / Fable 5)** = cerebro. Planifica, hace fetch web, edita archivos del repo
   directamente cuando Hayo lo autoriza, y entrega bloques para Claude Code. NO corre hugo ni git.
2. **Claude Code (terminal sobre `E:\Git_Use_LabOnce`)** = manos. Corre hugo y git, valida el
   build, commitea y **pushea a main** (cada push redeploya el sitio vía Actions).
   Default **Sonnet**; Opus solo para arquitectura delicada.
**Política:** cada etapa termina con build verde + commit + push (Hayo lo pidió explícito).

## Estado actual: REDISEÑO 2026 COMPLETO — pendiente build de validación + push
El 2026-06-11 el chat rediseñó todo el sitio en torno al **nuevo logo**
(`static/images/labonce-logo.png`, copia de "LabONCE v2026.png": fondo blanco, navy,
línea arcoíris, cerebro multicolor) y portó TODO el contenido restante del Wix.
**Falta:** que Claude Code corra el build, se corrija lo que falle, y se haga push.

### Identidad visual nueva (labonce.css reescrito)
- Fondo blanco/claro; texto navy `--lo-ink #16233B`; azul principal `--lo-blue #1D6FE0`.
- **Arcoíris del logo** como firma: `--lo-rainbow` (filete bajo navbar, subrayado de títulos
  de sección, borde superior de tarjetas al hover, filete sobre el footer).
- Hero claro con el logo grande a la derecha + canvas de nodos multicolor (scripts.html).
- Tipografías sin cambio: Space Grotesk / Inter / Roboto Condensed. Prefijo `lo-`.

### Arquitectura de contenido nueva (menús reorganizados)
Menú: **Inicio / Equipo / Investigación / Docencia / Blog**
- **Equipo** (`/integrantes`, título "Equipo"): agrupado por `categoria` en data/integrantes.yaml:
  director (Hayo) → activos (Délano, Ramos, D. Contreras, **Asunción Ruiz** (nueva, sin foto/bio),
  Herrero) → alumnos activos (**Pablo Pozo, Andrés Contreras**) → egresados (**Rosario Garrido,
  Felipe Faúndez**) → anteriores (Michael, Núñez, Barraza). Plantilla `integrantes/list.html`
  agrupa con `where` + color de grupo; tolera falta de categoria.
- **Investigación** (dropdown): Proyectos (`data/proyectos.yaml`, ya con el proyecto FONDECYT
  11200469 completado), Publicaciones destacadas, **Todas las publicaciones** (45 refs portadas
  del Wix a `content/publicaciones/todas.md`), **Oferta de Tesis** (texto completo del Wix).
- **Docencia** (`/recursos`, dropdown): plantilla genérica `layouts/recursos/recurso.html`
  (lee `data_src` del front matter) + 5 data files CMS-editables:
  `clases_online.yaml` (35 clases), `maniobras.yaml` (11), `esenciales.yaml` (6),
  `fisiologia.yaml` (5), `seminarios.yaml` (5). Campo `video` = ID de YouTube.
- **Blog**: 8 posts (3 previos + 5 portados: curso otoneurología 2025, vértigo funcional MPPP,
  clase balance 2022, VPPB difícil manejo, musicoterapia ORL). Chips de tags en la lista.

### ⚠️ Videos pendientes de ID (importante)
El Wix usaba un reproductor propio y el fetch no entrega las URLs de los videos. Tienen ID
de YouTube confirmado: las 4 clases del blog docente, y en maniobras: Epley detallado
(3oKt028hWyk), reentrenamiento auditivo (r1ZZ57jz_B8), estabilidad de la mirada (6WDXnLouGh4),
VORx2 (qpWq3qQpQA4) — tomados del sitio personal/blog (Hayo: verificar asignación).
El RESTO de las clases del catálogo está sin `video:`; se completan por Pages CMS o
pegándole al chat la lista de IDs del canal de YouTube.

### Riesgos a vigilar en el primer build del rediseño
- `where . "categoria" "in" (slice ...)` en index.html y los `where` de integrantes/list.html.
- `layout: "recurso"` + `data_src` (lookup layouts/recursos/recurso.html, `index site.Data`).
- El logo con espacio "LabONCE v2026.png" NO se usa (se usa la copia labonce-logo.png).

## Pendientes
1. **Build + push del rediseño** (bloque ya entregado a Hayo).
2. Completar IDs de YouTube de los videos del catálogo (CMS o chat).
3. Localizar imágenes del CDN de Wix (fotos de integrantes, portadas de pubs/posts) y el PDF
   "Vértigo y Equilibrio" + "Detalles del estudio" (hoy en filesusr de Wix) a static/.
4. Foto/bio de Asunción Ruiz; bios de Pozo y A. Contreras; fotos de egresados (opcional).
5. Google Scholar IDs en publicaciones/todas.md (se quitaron los placeholders rotos).
6. Dominio labonce.cl si se recupera (CNAME + baseURL).
7. Limpiar warnings de deprecación de Hugo (languageCode, .Site.Data… no fatales).

## Decisiones tomadas
- Intranet y Repositorios del Wix: OMITIDOS. ✔
- Arquitectura 4 áreas (Equipo/Investigación/Docencia/Blog) en vez de las ~12 pestañas del Wix. ✔
- Push a main en cada etapa con build verde. ✔
- Deploy: actions en versiones Node 24; Pages activado a mano (Settings → Pages → GitHub Actions). ✔

## 🧭 MODELO DE REFERENCIA — Sitio del Depto. de Neurociencia
Vive en `E:\Git_Use_WebUchile` (conectar solo-lectura en hilos nuevos). Stack distinto
(Hugo Blox + Tailwind): emular nivel de diseño y patrones CMS-safe, no la mecánica.
