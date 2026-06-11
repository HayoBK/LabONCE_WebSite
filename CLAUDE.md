# CLAUDE.md — Sitio web LAB ONCE

Contexto y reglas para trabajar en este repositorio con Claude.
Propietario: **Hayo Breinbauer** (otoneurólogo, dev Python). Idioma de trabajo: **español**.

---

## Qué es este repo
Sitio de **LAB ONCE — Laboratorio de Otoneurología Clínica y Neurociencias del Equilibrio**,
una red de investigadores de **Clínica Alemana de Santiago** y el **Departamento de
Neurociencia de la Universidad de Chile**.

Reemplaza la antigua web hecha en Wix (`https://hayobk.wixsite.com/labonce`, ya sin pago).
Dominio objetivo futuro: **labonce.cl** (hoy caído).

## Stack (IMPORTANTE: difiere del sitio de Neurociencia)
- **Hugo extended 0.162.1**, sitio **AUTOCONTENIDO** (sin Hugo Blox, sin módulos Go, sin
  Tailwind, sin pnpm). Todas las plantillas viven en `layouts/` y el CSS en
  `static/css/labonce.css`. Esto se eligió a propósito para evitar los dolores del otro repo
  (bug pnpm/Tailwind #14852, deprecations del tema, dependencia de `proxy.golang.org`).
- **GitHub Pages** vía GitHub Actions (`.github/workflows/deploy.yml`).
- **Pages CMS** (`.pages.yml`) para edición sin código.
- Se aloja en **otra cuenta de GitHub** (asociada a hayo.bk), repo aún por crear.
  Ver `GUIA-DEPLOY-LABONCE.md`.

## baseURL y rutas (clave)
- `config/_default/hugo.yaml` tiene un **placeholder**: `https://USUARIO.github.io/REPO/`.
- En **producción NO importa el placeholder**: el workflow hace
  `hugo --baseURL "${{ steps.pages.outputs.base_url }}/"`, es decir, usa la URL real de
  GitHub Pages (incluye el path `/REPO/`). Solo edita el placeholder si quieres que el
  **build local** genere links correctos.
- Por eso TODAS las rutas internas usan `relURL` / `.RelPermalink` / `pageRef` y NUNCA un
  path absoluto hardcodeado. Imágenes locales: `"images/x.jpg" | relURL` (sin slash inicial).

## Reglas de oro
1. **Valida el build antes de commitear:** `HUGO_ENVIRONMENT=production hugo --minify`
   (PowerShell: `$env:HUGO_ENVIRONMENT="production"; hugo --minify`). Sin `ERROR` = verde.
   Hugo extended 0.162.1 (mismo binario que ya tienes para el otro sitio).
2. **CMS-safe:** lo editable va en `data/*.yaml` o front-matter, y las plantillas toleran que
   una lista venga como string (el CMS a veces aplana listas). Patrón `reflect.IsSlice`
   (aplicado en `integrantes/list.html` campo `bio`).
3. **CSS propio:** un solo archivo `static/css/labonce.css`, clases prefijadas `lo-`.
4. **YAML:** valores escalares con `: ` / `#` / comillas → entre comillas dobles.
5. **Rutas:** `relURL` / `.RelPermalink` / `pageRef`. Nunca hardcodear `/REPO/...`.
6. **Imágenes:** hoy varias apuntan al **CDN de Wix** (`static.wixstatic.com`). Funcionan en
   el navegador del visitante, pero conviene **localizarlas** a `static/images/` (ver
   pendientes). El navbar usa el logo local si existe `static/images/labonce-logo.png`,
   y si no cae al de Wix (lógica en `partials/header.html`).
7. **Commits chicos y claros, en español.**

## Arquitectura
- `layouts/_default/baseof.html` → esqueleto (head, header, main, footer, scripts).
- `partials/`: `head.html`, `header.html` (navbar con dropdowns desde `menus.yaml`),
  `footer.html`, `scripts.html` (menú móvil + canvas "equilibrio").
- `layouts/index.html` → Home (hero + intro + publicaciones destacadas + integrantes + afiliaciones).
- Plantillas de sección: `integrantes/list.html`, `publicaciones/list.html`,
  `proyectos/list.html`, `blog/list.html`. Genéricas: `_default/list.html`, `_default/single.html`.
- **Datos** (CMS): `data/integrantes.yaml`, `data/publicaciones_seleccionadas.yaml`,
  `data/proyectos.yaml`.
- **Contenido**: `content/` con `_index.md` por sección + páginas sueltas (oferta-tesis,
  recursos/*, publicaciones/todas, blog/*).
- **Menú**: `config/_default/menus.yaml` (con submenús vía `parent`). La sección **Intranet**
  del Wix se OMITE (decisión de Hayo).
- **Paleta**: navy `#06182B`/`#0B2A45`, aqua `#1FC8DD`, teal `#0E8DA0`. Vars en `:root` de
  `labonce.css` con prefijo `--lo-`.
- **Fuentes**: Space Grotesk (títulos), Inter (cuerpo), Roboto Condensed (rótulos) — Google Fonts.

## Modo de trabajo — MODO DUAL
- **El chat (Cowork / Fable 5)** = cerebro: planifica, investiga, hace fetch del Wix y entrega
  **TODO lo que hay que pegar en Claude Code en UN SOLO bloque grande** (preferencia de Hayo).
  NO corre hugo ni git (su sandbox no puede instalar Hugo).
- **Claude Code (terminal sobre `E:\Git_Use_LabOnce`)** = manos: SÍ corre hugo y git. Edita,
  valida el build, hace commits/push. Lo maneja Hayo pegando los bloques y devolviendo el diff/salida.
- Al iniciar cada tarea, el chat recomienda **Sonnet** (default) vs **Opus** (solo razonamiento
  delicado) para Claude Code.
- Build local en Windows: Hugo extended 0.162.1 ya instalado. NO requiere npm/pnpm (sin Tailwind).

## Pendiente (ver CONTINUACION-LABONCE.md para el detalle)
- Crear el repo en la otra cuenta de GitHub y primer push (GUIA-DEPLOY-LABONCE.md).
- Portar páginas que quedaron como marcador: Proyectos Activos, Oferta Tesis, Todas las
  Publicaciones, y las 5 de Recursos Docentes; completar el Blog.
- Localizar imágenes del CDN de Wix a `static/images/`.
- Logo definitivo en `static/images/labonce-logo.png`.
