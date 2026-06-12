# CONTINUACIÓN — Sitio LAB ONCE

Carpeta de trabajo: `E:\Git_Use_LabOnce`.
Sitio Hugo **autocontenido**. Repo: `github.com/HayoBK/LabONCE_WebSite` (cuenta HayoBK).
URL GitHub Pages: `https://hayobk.github.io/LabONCE_WebSite/` · Dominio en corte: `labonce.cl`.
Última actualización: 2026-06-11 (noche) — V2 publicada (commit `fb407f0`).

---

## ⚠️ CÓMO TRABAJAMOS — MODO DUAL
1. **El chat (Cowork / Fable 5)** = cerebro. Planifica, hace fetch web, **edita archivos del
   repo directamente** (Hayo lo autorizó para este repo), usa Chrome para páginas con JS.
   NO corre hugo ni git.
2. **Claude Code (terminal sobre `E:\Git_Use_LabOnce`)** = manos: hugo + git. Default
   **Sonnet**. Política: cada etapa cierra con build verde + commit + push (deploy automático).
3. Conectar también `E:\Git_Use_WebUchile` (solo lectura) como referencia si hace falta.

## Estado: V2 EN PRODUCCIÓN (commit fb407f0, deploy verde)
El sitio completo está publicado: rediseño con el logo arcoíris 2026 + arquitectura de
**blog unificado**. 134 páginas, build verde.

### Lo que ya está hecho y funcionando
- **Identidad**: fondo claro, navy + azul `#1D6FE0`, arcoíris del logo como firma (filete
  navbar, títulos, hovers, footer). "equilibrio" del hero en degradé de azules.
  Navbar = solo la cabeza del logo (`static/images/labonce-head.png`); hero con
  `labonce-hero.png` (fondo transparente). Generados con PIL desde "LabONCE v2026.png".
- **Arquitectura**: Inicio / Equipo / Investigación (Proyectos · Pub. destacadas · Todas ·
  Oferta Tesis) / **Recursos Docentes** (= `/categorias/clases`, dropdown por tags) /
  **Actualidad** (= `/categorias/noticias`).
- **Blog unificado**: TODO el material vive en `content/blog/` (70 posts + _index).
  Front matter: `categorias: ["noticias"|"clases"]` + `tags` de área
  (esenciales-de-vertigo, fisiologia-basica, clases-on-line, maniobras-y-terapias,
  seminarios-de-alumnos). Plantilla término: `layouts/_default/term.html`.
  YA NO existen `content/recursos/` ni data files de docencia.
- **Equipo** (`data/integrantes.yaml`, campo `categoria`): director / activos (Délano,
  Ramos, D. Contreras, A. Ruiz, Herrero) / alumnos (Pozo, A. Contreras) / egresados
  (Garrido, Faúndez) / anteriores (Michael, Núñez, Barraza).
- **ORCID**: `publicaciones/todas` carga en vivo `pub.orcid.org/v3.0/0000-0002-3278-065X/works`
  (JS client-side; listado curado de 45 refs como respaldo en la misma página).
- **YouTube**: canal `@VertigoyEquilibrio-HayoBre6046` (channel ID `UCRgbxmT-Pzw78ZdB_7If-fw`),
  30 videos recolectados; 32 posts con video embebido.
- Deploy: Actions Node 24, Pages activo, `.pages.yml` al día (blog con categorías).

## 🔴 PENDIENTE INMEDIATO: DNS labonce.cl (¡con errores de tipeo detectados!)
Hayo ya hizo: Cloudflare (Free) + nameservers en NIC + custom domain `labonce.cl` en
GitHub Pages. **PERO los registros en Cloudflare quedaron MAL TIPEADOS** (verificado por
DNS 2026-06-11 noche):
- CNAME www → `hayobk_github.io` (guión bajo) — debe ser **`hayobk.github.io`** (punto).
- Las 4 A apuntan a IPs erróneas (185.199.188.153 / 185.100.111.153 / 185.199.118.153 /
  185.199.189.153). Deben ser EXACTAMENTE: **185.199.108.153, 185.199.109.153,
  185.199.110.153, 185.199.111.153** (todas DNS only / nube gris).
Consecuencia actual: github.io redirige a labonce.cl (custom domain ya seteado) y
labonce.cl no responde → **el sitio está inaccesible hasta corregir los registros**.
Tras corregir: GitHub emite el certificado (minutos a horas) → marcar "Enforce HTTPS".
Verificación: `https://dns.google/resolve?name=labonce.cl&type=A` debe devolver las 4 IPs
correctas; NS deben pasar de wixdns a Cloudflare (TTL viejo 6 h).
**Después del corte:** (1) `baseURL: "https://labonce.cl/"` en `config/_default/hugo.yaml`
(solo afecta builds locales); (2) actualizar el botón LAB ONCE del sitio personal
(`E:\Git_Use_HayoPersonalWeb/config/_default/params.yaml`) a `https://labonce.cl/` + push
de ese repo; (3) opcional: verified domain en GitHub.

## Otros pendientes (en orden)
1. **38 posts de clases sin video** (el Wix no exponía las URLs; muestran nota "en
   migración"). Se completan por Pages CMS o pegando al chat los links/IDs que falten.
   Posibles matches dudosos ya anotados: "Fisiología de la Audición PRO" (Wix 2019) vs
   "Fisiología Auditiva 1-2 de 2" (canal) — Hayo decide si fusionar.
2. **Localizar imágenes** del CDN de Wix (fotos integrantes, portadas pubs/posts) y los
   PDFs de filesusr (texto guía "Vértigo y Equilibrio", "Detalles del estudio") a static/.
3. **Fichas incompletas**: foto+bio de Asunción Ruiz; bios de Pablo Pozo y Andrés
   Contreras; fotos de egresados.
4. Revisar visualmente la V2 (Hayo aún no la ve) y ajustar detalles de estética.
5. Limpiar warnings de deprecación de Hugo (languageCode, .Site.Data — no fatales).
6. Pages CMS: probar flujo de edición con la nueva estructura de blog.

## Datos útiles
- ORCID Hayo: `0000-0002-3278-065X` · Email académico: `hbreinbauer@uchile.cl`.
- Canal YouTube: `https://www.youtube.com/@VertigoyEquilibrio-HayoBre6046`.
- El sandbox del chat NO puede: instalar Hugo, consultas DNS directas (usar
  `dns.google/resolve?name=X&type=Y`), descargar modelos de voz (audios de WhatsApp:
  pedir a Hayo la transcripción), ni descargar del CDN de Wix.
- El chat SÍ puede: editar el repo, procesar imágenes (PIL), usar Chrome (con permisos
  que Hayo aprueba en pantalla), fetch de Wix/YouTube(parcial)/ORCID.

## 📋 MENSAJE INICIAL para el próximo hilo de Cowork (Fable 5)
> Hola. Proyecto: **sitio LAB ONCE** (Hugo autocontenido) en `E:\Git_Use_LabOnce`, en vivo
> vía GitHub Pages (repo HayoBK/LabONCE_WebSite) y en corte de dominio a labonce.cl.
> Lee primero `CONTINUACION-LABONCE.md` y `CLAUDE.md` en esa carpeta: la V2 (blog
> unificado + ORCID + logo arcoíris) ya está publicada (commit fb407f0).
>
> Trabajamos en **MODO DUAL**: tú (el chat) planificas, investigas y **editas los archivos
> del repo directamente** (te autoricé), y me entregas al final UN SOLO bloque para pegar
> en **Claude Code** (corre en paralelo sobre `E:\Git_Use_LabOnce`; hace hugo + git + push,
> default Sonnet). Yo te pego de vuelta el diff/salida.
>
> Primera tarea: revisa el estado del DNS de labonce.cl (sección "PENDIENTE INMEDIATO" del
> CONTINUACION: quedaron registros mal tipeados en Cloudflare que yo debía corregir —
> verifica con `dns.google/resolve` si ya quedó bien y si GitHub emitió el certificado).
> Si el dominio ya está activo, haz el post-corte (baseURL + botón del sitio personal).
> Después seguimos con los pendientes numerados del CONTINUACION.
