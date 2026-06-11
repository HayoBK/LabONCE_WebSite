# CONTINUACIÓN — Sitio LAB ONCE

Carpeta de trabajo: `E:\Git_Use_LabOnce`.
Sitio Hugo **autocontenido** que reemplaza el Wix `https://hayobk.wixsite.com/labonce`.
Última actualización: 2026-06-11.

---

## ⚠️ CÓMO TRABAJAMOS — MODO DUAL (igual que el sitio de Neurociencia)
Hayo trabaja con DOS herramientas en paralelo sobre este repo:

1. **El chat (Cowork / Fable 5)** = el cerebro. Planifica, investiga en la web (puede hacer
   fetch del Wix), decide arquitectura/diseño y **entrega BLOQUES en español listos para pegar
   en Claude Code**. Revisa los diffs/salidas que Hayo le pega de vuelta. **NO ejecuta git ni
   hugo** (su sandbox no puede instalar Hugo: binarios de GitHub y `proxy.golang.org` bloqueados
   por allowlist).
2. **Claude Code (terminal sobre `E:\Git_Use_LabOnce`)** = las manos. **SÍ corre hugo y git.**
   Edita archivos, valida el build, hace commits/push. Lo maneja Hayo pegando los bloques.

**Preferencia de Hayo (importante):** el chat debe entregar **TODO lo que hay que pegar en
Claude Code en UN SOLO bloque grande** (una sola ventana de copiado), no en trozos sueltos.

**Recomendación de modelo de Claude Code:** al iniciar cada tarea, el chat recomienda
**Sonnet** por defecto (edición de plantillas, git, builds), y **Opus** solo para razonamiento
delicado de arquitectura.

---

## Estado actual: PRIMERA VERSIÓN CONSTRUIDA — falta primer build verde + deploy
La estructura completa está hecha y validada estáticamente (todos los YAML/front-matter
parsean; estructura de plantillas correcta; `pageRef` del menú corregido). **El build con hugo
todavía NO se ha corrido** (no se pudo en el sandbox). **Primera acción del nuevo hilo: que
Claude Code corra el build y se arreglen los errores que aparezcan.**

### ✅ Hecho
- **Arquitectura Hugo autocontenida** (sin Hugo Blox / módulos Go / Tailwind / pnpm). Elegida a
  propósito para poder construir/desplegar sin las trabas del otro repo y del allowlist.
- **Config**: `config/_default/hugo.yaml` (baseURL placeholder `USUARIO/REPO`), `menus.yaml`
  (navbar con submenús; Intranet omitida), `params.yaml` (marca, contacto, afiliaciones).
- **Plantillas**: `_default/baseof|list|single`, `index.html` (Home), `integrantes/list.html`,
  `publicaciones/list.html`, `proyectos/list.html`, `blog/list.html`, y partials
  `head|header|footer|scripts`. Navbar con dropdown + menú móvil + canvas animado "equilibrio".
- **CSS** propio `static/css/labonce.css` (paleta navy/aqua, fuentes Space Grotesk/Inter, prefijo `lo-`).
- **Contenido portado del Wix**:
  - **Integrantes (8)** → `data/integrantes.yaml`: Hayo Breinbauer (Director), Phoebe Ramos,
    Daniela Contreras, Diego Herrero, Paul Délano, Pía Michael, Marcia Núñez, Cristián Barraza.
    Cargos y bios completas. Fotos = CDN de Wix.
  - **Publicaciones seleccionadas (5)** → `data/publicaciones_seleccionadas.yaml` (revista, año,
    link, abstract): Entropy/PPPD 2025, Brain Sci 2024, Frontiers 2019, Tinnitus 2019, BPPV 2016.
  - **Blog**: 3 entradas de muestra (Entropía PPPD, Bárány 2024, Videos VORx2 con embed YouTube).
- **Deploy**: `.github/workflows/deploy.yml` (Hugo extended 0.162.1 → Pages; fija la baseURL real
  automáticamente, por eso el placeholder no afecta producción). `.gitignore`, `static/.nojekyll`.
- **Pages CMS**: `.pages.yml` (integrantes, publicaciones, proyectos, blog, recursos, ajustes).
- **Docs**: `CLAUDE.md`, este archivo, `GUIA-DEPLOY-LABONCE.md`, `README.md`, `setup-git.ps1`.

### ⚠️ Riesgos a vigilar en el primer build (revisar si algo falla)
- Lookup de plantillas por sección (publicaciones/integrantes/proyectos/blog).
- `fileExists` del logo en `header.html` (cae al logo de Wix si no existe el local).
- El embed de YouTube en `content/blog/videos-vorx2.md` (usé `<iframe>` directo, no shortcode).
- `.IsMenuCurrent`/`.HasMenuCurrent` en `header.html`.

---

## Pendientes de portar (con URLs fuente del Wix — todas accesibles por fetch)
1. **Proyectos Activos** → `https://hayobk.wixsite.com/labonce/proyectos-activos` → `data/proyectos.yaml`.
2. **Oferta Tesis** → `https://hayobk.wixsite.com/labonce/oferta-tesis` → `content/oferta-tesis.md`.
3. **Todas las Publicaciones** → `https://hayobk.wixsite.com/labonce/todas-las-publicaciones`
   → `content/publicaciones/todas.md` (evaluar `data/publicaciones_todas.yaml`).
4. **Recursos Docentes** (5 páginas, hoy marcadores en `content/recursos/`):
   `/clases-on-line`, `/maniobras-y-terapias`, `/pregrado`, `/fisiologia-basica`,
   `/seminarios-alumnos`, y blog docente `/blog-docente`.
5. **Blog completo** → `https://hayobk.wixsite.com/labonce/blog` (+ posts en `/post/...`).
6. **Intranet / Repositorios**: OMITIDAS (decisión de Hayo).

## Otras tareas
- **Localizar imágenes** del CDN de Wix a `static/images/` y reemplazar por `images/<archivo>`
  (las baja Hayo; el chat no puede, el CDN está bloqueado en el sandbox). IDs en los `data/*.yaml`.
- **Logo** definitivo en `static/images/labonce-logo.png` (el navbar lo toma solo si existe).
- **Contacto/redes** en `params.yaml`; **Google Scholar** en `content/publicaciones/todas.md`.
- **Dominio**: si se recupera `labonce.cl`, configurar CNAME y `baseURL`.

## Decisiones ya tomadas con Hayo
- baseURL: placeholder editable (el workflow fija la real). ✔
- Deploy: Hayo crea el repo en la **otra cuenta de GitHub** (asociada a hayo.bk) y hace el primer
  push; el chat deja todo listo + guía/script. ✔
- Alcance: portar el sitio completo público (núcleo hecho; resto pendiente). ✔
- Intranet: omitida. ✔
- Arquitectura: Hugo autocontenido (no HugoBlox). ✔ (revisable si Hayo prefiere el stack idéntico)

---

## 🧭 MODELO DE REFERENCIA — Sitio del Depto. de Neurociencia
El sitio de Neurociencia es el **modelo de calidad y de patrones** a emular. Vive en un repo
APARTE, en **`E:\Git_Use_WebUchile`** (en vivo: `https://openneurocienciauchile.github.io/Web/`).

**IMPORTANTE:** en un hilo nuevo, el chat (Fable 5) NO tiene esa carpeta montada. Para poder
estudiarla, Hayo debe **conectar también `E:\Git_Use_WebUchile` (solo lectura basta)** al inicio
del hilo (selector de carpeta de Cowork). Alternativamente, Claude Code ya la tiene en disco y
puede pegar archivos puntuales.

**Qué mirar ahí (y por qué):**
- `CLAUDE.md` y `CONTINUACION-etapa-features.md` → reglas de oro, decisiones de arquitectura y
  una lista larga de *gotchas* ya resueltos (relURL/TrimPrefix, listas CMS-safe, YAML, etc.).
- `layouts/_partials/hooks/head-end/custom.html` → TODO el CSS propio + navbar con degradado +
  hero + canvas + las tarjetas (`dep-*`). Es la vara estética a igualar.
- `layouts/academicos/list.html` y `single.html` → grilla de tarjetas, orden por apellido y
  **guardas defensivas** (`reflect.IsSlice`) contra el aplanado de listas del CMS.
- `.pages.yml` → formato de colecciones de Pages CMS (de aquí salió el de LAB ONCE).
- `config/_default/` y `.github/workflows/deploy.yml` → estructura de config y deploy.

**Ojo — el STACK difiere:** Neurociencia usa **Hugo Blox + Tailwind v4 + pnpm/módulos**;
LAB ONCE es **autocontenido** (layouts propios + CSS plano, sin módulos). Por eso se emula el
**nivel de diseño/UX y los patrones CMS-safe / reglas de oro**, NO la mecánica de módulos ni el
pipeline de Tailwind. Cualquier `{{ range }}` sobre un campo editable debe tolerar string además
de lista (patrón `reflect.IsSlice`), igual que en Neurociencia.

---

## ▶️ PLAN SUGERIDO PARA EL NUEVO HILO (en orden)
1. **Build verde**: Claude Code corre `HUGO_ENVIRONMENT=production hugo --minify`. El chat
   recibe errores y entrega un bloque único de correcciones. Repetir hasta verde.
2. **Previsualizar** (`hugo server`) y ajustar diseño si hace falta.
3. **Crear repo + primer push** en la otra cuenta (ver `GUIA-DEPLOY-LABONCE.md`) y activar Pages.
4. **Seguir portando** las páginas pendientes (lista arriba), una por una con fetch del Wix.
5. **Localizar imágenes** y cargar el logo.

---

## 📋 MENSAJE INICIAL para pegar en el nuevo hilo de Cowork (Fable 5)
> Hola. Proyecto: sitio web de **LAB ONCE** (Hugo autocontenido) en `E:\Git_Use_LabOnce`,
> que reemplaza el Wix `https://hayobk.wixsite.com/labonce`. Lee primero
> `CONTINUACION-LABONCE.md` y `CLAUDE.md` en esa carpeta (el CONTINUACION trae el estado, los
> pendientes y la sección "MODELO DE REFERENCIA").
>
> **Carpetas:** trabaja sobre `E:\Git_Use_LabOnce`. Además te conecté (solo lectura) el repo del
> **Depto. de Neurociencia en `E:\Git_Use_WebUchile`**, que es el **modelo de referencia** de
> estética y de patrones (mira su `CLAUDE.md`, `layouts/_partials/hooks/head-end/custom.html`,
> `layouts/academicos/*` y `.pages.yml`). OJO: su stack es distinto (Hugo Blox + Tailwind);
> emula el NIVEL de diseño y los patrones CMS-safe, no la mecánica de módulos. Si no ves esa
> carpeta, pídeme conectarla.
>
> Trabajamos en **MODO DUAL**: tú (el chat) planificas, investigas y haces fetch del Wix, y me
> entregas **TODO lo que debo pegar en Claude Code en UN SOLO bloque grande**. Yo tengo
> **Claude Code activo en paralelo sobre `E:\Git_Use_LabOnce`, que SÍ puede correr hugo y git**;
> ejecuto tus bloques y te pego el diff/salida. Al iniciar cada tarea, recomiéndame Sonnet vs Opus
> para Claude Code (default Sonnet).
>
> El sitio ya está construido pero **el build con hugo aún no se ha corrido**. Primera tarea:
> dame un bloque único para que Claude Code corra `HUGO_ENVIRONMENT=production hugo --minify`,
> y arreglamos lo que falle hasta dejarlo verde. Después seguimos con el deploy (crear el repo en
> mi otra cuenta de GitHub) y con portar las páginas pendientes del Wix (Proyectos, Oferta Tesis,
> Todas las Publicaciones, Recursos Docentes, Blog). Confírmame que leíste ambos archivos y
> resúmeme el estado en 3 líneas antes de empezar.
