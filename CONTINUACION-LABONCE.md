# CONTINUACIÓN — Sitio LAB ONCE

Carpeta de trabajo: `E:\Git_Use_LabOnce` (en el Mac de Hayo: `~/Git_Web/LabONCE`).
Sitio Hugo **autocontenido**. Repo: `github.com/HayoBK/LabONCE_WebSite` (cuenta HayoBK).
En vivo: **https://labonce.cl/** (HTTPS OK) · GitHub Pages: `https://hayobk.github.io/LabONCE_WebSite/`.
Última actualización: 2026-08-26 — V4 (ORCID + fichas individuales) **EN PRODUCCIÓN**.

---

## ✅ V4 (2026-08-26) — ORCID automático + fichas individuales de equipo. EN PRODUCCIÓN
Commit `121db17`, deploy verde, 163 páginas. Implementado desde `ENCARGO-CLAUDE-CODE.md`
(escrito por Cowork) y compilado/corregido por Claude Code.

1. **Equipo migrado a páginas individuales.** Cada persona es ahora
   `content/integrantes/<slug>.md` con URL propia (13 fichas) + `layouts/integrantes/single.html`.
   `data/integrantes.yaml` quedó como **referencia histórica sin uso** — NO borrar sin que Hayo
   lo confirme. `/integrantes/` agrupa en 5 categorías (director / activo / alumno / egresado /
   anterior) leyendo `.Pages`, ya no el data file.
2. **Sincronización ORCID diaria.** `.github/workflows/orcid.yml` (08:10 UTC ≈ 05:10 Chile,
   + `workflow_dispatch`) corre `scripts/orcid_sync.py`, que lee `data/orcid.yaml`, consulta la
   API pública de ORCID, enriquece con Crossref y escribe `data/publicaciones_orcid.json`.
   **Solo se sincroniza el ORCID del director** (decisión deliberada, documentada en
   `data/orcid.yaml` e `INFORME-ORCID-LABONCE.md`). El campo `orcid` de cada ficha personal es
   independiente: solo pinta un chip con link al perfil, no dispara sincronización.
3. **Publicaciones.** `/publicaciones/` = las 6 destacadas, ahora con año y `factor_impacto`
   (campo nuevo, vacío por ahora). `/publicaciones/todas/` ya NO usa fetch en JavaScript: se
   genera en el build fusionando ORCID + `data/publicaciones_historicas.yaml` (45 refs curadas),
   agrupado por año, con buscador. Hoy son **52 entradas** (45 históricas + 7 de ORCID).
   La portada cambió "Publicaciones destacadas" por "Publicaciones de los últimos años" con
   contadores automáticos (últimos 5 / 10 años / total).
4. **GitHub Actions:** `Settings → Actions → Workflow permissions` se subió a **Read and write**
   (estaba en `read`, lo que habría hecho fallar el `git push` de `orcid.yml` en silencio).
   `deploy.yml` no se ve afectado porque declara su propio bloque `permissions:` restrictivo.

### 🐛 Bugs encontrados al compilar de verdad (el encargo nunca se había compilado)
Los cuatro venían en el material entregado por Cowork y quedaron corregidos en `121db17`:
- **`layouts/integrantes/list.html`** — los colores de cada grupo se emitían como
  `style="background:ZgotmplZ"` (Go/Hugo bloquea interpolar un string en contexto CSS): 18
  estilos inline rotos. Fix: `| safeCSS` en las 2 líneas (los valores son literales de la
  plantilla, no datos de usuario).
- **`scripts/orcid_sync.py`** — el dedup contra el histórico normalizaba `cita[:90]`; en estilo
  Vancouver esos 90 caracteres son casi todo el listado de autores, así que el título quedaba
  decapitado y el match por título **nunca** podía ocurrir. Resultado: 8 publicaciones duplicadas
  (entre ellas el preprint bioRxiv `10.1101/2025.06.08.658513` del paper de ganglios basales, que
  esquivaba el filtro por DOI porque el histórico tiene el DOI publicado de Sci Rep). Fix: no
  truncar la cita. Pasó de 15 a 7 publicaciones ORCID, las 8 eliminadas verificadas una por una.
  ⚠️ **El mismo bug existe en `~/Git_Web/Neurosistemas/scripts/orcid_sync.py`** (es la copia
  original) — conviene portar el fix allá.
- **`scripts/test_orcid_sync.py`** — respaldaba `orcid.yaml` pero no `publicaciones_orcid.json`,
  y al terminar reescribía el JSON con la semilla vacía, **borrando el resultado real** de
  `orcid_sync.py`. Como el encargo mandaba correr el test justo después del sync y antes del
  commit, habría publicado el sitio sin publicaciones ORCID. Fix: respalda y restaura ambos.
- **`scripts/verify_static.py`** — parseaba `layouts/index.json` (plantilla Hugo del buscador
  global, empieza con `{{`) como si fuera un JSON de datos → 1 error falso. Fix: saltar `layouts/`.

### Pendientes que deja la V4
1. **ORCID del resto del equipo** — ver `INFORME-ORCID-LABONCE.md`. Falta confirmar si el
   "Andrés Contreras" de Neurosistemas (`0009-0009-8317-106X`) es el mismo alumno de LAB ONCE, y
   buscar a mano los de Phoebe Ramos, Daniela Contreras, Diego Herrero, Rosario Garrido, Felipe
   Faúndez y Cristián Barraza (identidad y afiliación ya confirmadas en el informe).
2. **`factor_impacto`** en `data/publicaciones_seleccionadas.yaml`: las 6 entradas lo tienen
   vacío. Cuando Hayo tenga los datos, se rellena y aparece el chip "IF x.x" en `/publicaciones/`.
3. **Republicación francesa 2022** — ORCID trae dos veces el mismo trabajo con DOIs distintos:
   "Central nystagmus and alterations in vestibular tests…" (European Annals) y su
   "Republication de : …" (Annales françaises d'ORL). El primero ya está en el histórico, así que
   hoy en `/publicaciones/todas/` se ve solo la versión francesa. Decisión editorial de Hayo:
   si molesta, se agrega la republicación al histórico o se filtra por título.
4. **Títulos bilingües de Scopus** — las 2 entradas de 2009 traen desde ORCID el título en inglés
   y español concatenados con coma ("Original and abbreviated Zarit… ,Validación en Chile de la
   Escala…"). Se arregla mejor en el propio registro ORCID de Hayo que en el script.

---

## ⚡ V3 (2026-06-12) — videos conectados, buscador, contacto, landing. PENDIENTE build+push
DNS labonce.cl YA RESUELTO y en vivo con HTTPS. Ronda V3 implementada por el chat:
1. **Videos**: Hayo entregó `labonce_videos_mapeo_v2.md` (uploads) con los 63 IDs reales.
   Se conectaron TODOS los embeds. Multi-video: balance 2022 (4 partes), NAVI/mareo crónico
   (2). Epley básica=`3oKt028hWyk`, detallada=`CbVbmZSbzVA`. Se eliminaron los 2 posts
   "Métodos de Evaluación". Nuevos posts: "Navegación espacial alocéntrica en PPPD — Bárány
   2024" (`xNNK5gZtqYA`) y "Actualidad en Tinnitus" (3 partes: `0ZirE4vRMHc`, `PwCjd3qdnyk`,
   `_pnmf6gNr1A`). Ya NO quedan notas "en migración". 71 posts (66 clases + 5 noticias).
2. **Landing**: navbar con LOGO COMPLETO (`labonce-hero.png`, 74px). Hero con logo grande
   (620px) y texto más chico. Kicker "Universidad de Chile · Clínica Alemana". Se eliminó
   "Quiénes somos" → arriba van las Últimas noticias.
3. **Noticia nueva** (hoy): "Nueva página web, nuevo equipo, nuevos proyectos" (menciona
   investigación interdisciplinaria U. de Chile + FONDECYT 2026). Imagen Unsplash (placeholder).
4. **Foto Asunción Ruiz** (`static/images/asuncion.jpeg`); plantillas resuelven rutas locales
   con relURL.
5. **Proyectos**: quitado el marcador "pendiente de portar".
6. **Recursos Docentes** (`term.html`): 5 tags grandes + TODOS los demás tags + **buscador
   que filtra** las tarjetas. Cada tag tiene "← Volver a todos los recursos". Menú: nuevo
   subítem "Todos los recursos".
7. **Buscador global**: lupa arriba a la derecha → `/buscar/` (JS sobre `index.json`, nuevo
   output JSON del home en `layouts/index.json`).
8. **Contacto**: ítem de menú + `/contacto` con hbreinbauer@uchile.cl.

**Riesgos del build V3:** nuevo output JSON (`layouts/index.json`, usa `site.GetPage`),
`term.html` con recolección de tags vía `range .Pages`+`append`, layouts nuevos
`buscar.html`/`contacto.html` (lookup por `layout:` en front matter), menú con pageRef a
`/contacto`. Si algún `pageRef`/`GetPage` falla, revisar esos puntos.
Pendiente menor (⚠️): Esenciales 2 (Vértigo Agudo) quedó con ID `JCZZnAxosQQ` — hay 3 tomas
en el canal; Hayo confirma cuál prefiere (ver final del mapeo_v2).

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

## ✅ RESUELTO: DNS labonce.cl (histórico — el sitio responde en https://labonce.cl/)
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

## Nota técnica videos (2026-06-11 noche): Error 153 de YouTube RESUELTO
Los embeds fallaban con "Error 153 — configuración del reproductor": YouTube ahora EXIGE
que el iframe envíe referrer. Fix aplicado a TODOS los iframes (32 posts LAB ONCE + 3 del
sitio personal): atributos oficiales `referrerpolicy="strict-origin-when-cross-origin"` +
`allow="...web-share"`. Verificado vía oEmbed que los videos del canal SÍ permiten
inserción. Si un embed vuelve a fallar, revisar ese patrón.

## Otros pendientes (en orden)
1. **38 posts de clases sin video** (nota "en migración" + link al canal). Los videos
   antiguos NO están públicos en YouTube: casi seguro están **NO LISTADOS** en el canal
   (patrón confirmado: -VrOzj-Wda8 e irUXJJ5huqk son unlisted). **ACCIÓN HAYO:** abrir
   YouTube Studio → Contenido → filtro Visibilidad "No listado", y pegar al chat la lista
   título+link; el chat los conecta todos de una vez. Matches dudosos anotados:
   "Fisiología de la Audición PRO" (Wix 2019) vs "Fisiología Auditiva 1-2 de 2" (canal).
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
