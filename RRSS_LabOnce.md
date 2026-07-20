# RRSS LAB ONCE — Difusión del Blog en X e Instagram

Flujo estándar para convertir cada **noticia nueva del Blog de LAB ONCE** en publicaciones
para **X (Twitter)** e **Instagram**. Publicación desde las **cuentas personales de Hayo**,
por **copy-paste asistido** (Cowork redacta, tú pegas). Tono: **divulgación cercana** —
accesible para público general y pacientes, sin perder rigor; emojis moderados.

Dominio del sitio: `https://labonce.cl` · Las noticias viven en `content/blog/` con
`categorias: ["noticias"]` y su URL pública es `https://labonce.cl/blog/<slug>/`.

---

## 📋 MENSAJE DE NUEVO HILO (copia este bloque en un hilo nuevo de Cowork)

> **Sitio:** LAB ONCE — carpeta `~/Git_Web/LabONCE`. Esta tarea es de **redes sociales**, NO
> toca Hugo ni git (no hay build que correr).
>
> **Tarea:** genera las publicaciones de RRSS para la(s) noticia(s) nueva(s) del Blog.
>
> Post(s) a difundir (pega el/los slug o pega el `.md` completo):
> - `content/blog/________.md`
>
> Reglas:
> 1. Lee el/los post indicado(s). Publicamos desde **mis cuentas personales**; entrégame el
>    texto **listo para copy-paste** (yo pego en X e Instagram).
> 2. Tono **divulgación cercana** (público general y pacientes, riguroso, emojis moderados),
>    en **español**, en primera persona plural ("nuestro grupo", "estuvimos", "publicamos").
> 3. Para **cada** post entrégame:
>    - **X:** un tweet principal (≤ 280 caracteres, con emoji inicial y la URL
>      `https://labonce.cl/blog/<slug>/`) + un tweet de respuesta **opcional** con el detalle
>      técnico y el link al artículo/fuente original si existe.
>    - **Instagram:** un caption de 4–8 líneas (gancho + qué es + por qué importa + resultado)
>      cerrando con "🔗 link en la bio / labonce.cl" y un bloque de **8–10 hashtags**.
>    - **Imagen sugerida:** nombre del archivo de imagen del post (campo `image:` o las
>      `![...](images/...)` del cuerpo) que conviene adjuntar; si no hay, avísame.
> 4. Verifica que la **URL** del post sea correcta (slug real del archivo) y que las **citas
>    o datos** que menciones estén en el post (no inventar cifras).
> 5. Si son varias noticias, sepáralas con encabezado claro por post.

---

## 🎨 Receta de estilo (referencia)

**Estructura X (principal):** `emoji + gancho en 1 frase → qué hicimos/publicamos → URL`.
Mantener ≤ 280 caracteres. La respuesta opcional lleva el dato duro + link a la fuente
(Nature, MDPI, Frontiers, etc.) + 1–2 hashtags.

**Estructura Instagram (caption):**
1. Gancho corto con emoji.
2. Qué es / dónde se presentó o publicó (congreso, revista, institución).
3. Por qué importa (traducción clínica o conceptual, cercana al lector).
4. Resultado o idea principal (sin sobre-tecnicismos; sin inventar cifras).
5. Cierre: "🔗 Artículo completo / nota en labonce.cl (link en la bio)".
6. Bloque de 8–10 hashtags.

**Hashtags base** (ajustar por tema): `#tinnitus #neurociencia #otoneurología
#investigación #saludauditiva #ClínicaAlemana #UniversidadDeChile`. Sumar específicos:
`#terapiasonora #música`, `#PPPD #mareo`, `#vértigo #equilibrio`, `#conciencia`,
`#congreso`, según el post.

**Imagen:** usar la imagen de cabecera del post (`image:` del front matter) o una foto del
cuerpo. Instagram **exige** imagen; X mejora mucho con ella.

**Longitudes de referencia:** X principal ≤ 280; caption IG ~600–1.000 caracteres.

---

## 🧪 Ensayo — borradores listos de las 2 últimas noticias

### 1) 29ª Reunión Anual de la ASSC (Santiago 2026)

**Post:** `content/blog/assc-29-santiago-2026.md`
**URL:** https://labonce.cl/blog/assc-29-santiago-2026/
**Imagen sugerida:** `assc29-poster-hayo.jpg` (Hayo junto al póster) — alternativa:
`assc29-banner.jpg`.

**X — tweet principal:**
```
🧠 Estuvimos en la 29ª Reunión Anual de la ASSC —el estudio científico de la conciencia—, este año en Santiago.

Presentamos un póster: ¿y si el tinnitus y el mareo crónico se entienden mejor desde la percepción consciente, y no solo desde el oído?

🔗 https://labonce.cl/blog/assc-29-santiago-2026/
```

**X — respuesta opcional (hilo):**
```
En el póster mostramos que los adultos mayores con tinnitus tienen mayor volumen de los ganglios de la base (pálido, putamen, caudado y accumbens): posibles "porteros" del fantasma auditivo.

Artículo abierto en Sci Rep (Nature): https://www.nature.com/articles/s41598-025-25065-6
#tinnitus #neurociencia
```

**Instagram — caption:**
```
🧠 Abrir la mente a nuevas posibilidades.

Del 30 de junio al 3 de julio estuvimos en la 29ª Reunión Anual de la ASSC (Association for the Scientific Study of Consciousness), este año en Santiago de Chile.

Nos llevamos una mirada nueva para dos problemas muy cercanos a nuestra clínica: el tinnitus y el mareo funcional (PPPD). ¿Y si el "fantasma" del tinnitus o la desorientación del mareo crónico se entienden mejor como fenómenos de la percepción consciente, y no solo como fallas del oído o del equilibrio?

Presentamos un póster sobre el posible rol de los ganglios de la base en el tinnitus: con resonancia magnética encontramos que los adultos mayores con tinnitus tienen mayor volumen de pálido, putamen, caudado y núcleo accumbens —estructuras no auditivas que podrían actuar como "porteros" de esa percepción fantasma.

📄 Artículo completo (acceso abierto) en Scientific Reports – Nature.
🔗 Nota completa en labonce.cl (link en la bio).

#tinnitus #neurociencia #otoneurología #conciencia #ASSC2026 #investigación #ClínicaAlemana #UniversidadDeChile #saludauditiva
```

---

### 2) mMIDST — terapia sonora para el tinnitus (Brain Sciences 2026)

**Post:** `content/blog/terapia-sonora-mmidst-tinnitus-brain-sciences.md`
**URL:** https://labonce.cl/blog/terapia-sonora-mmidst-tinnitus-brain-sciences/
**Imagen sugerida:** `mmidst-tinnitus-fig1.png` (figura de cabecera: tonos integrados en música).

**X — tweet principal:**
```
🎵 ¿Y si la terapia para el tinnitus pudiera ir escondida dentro de la música?

Publicamos en Brain Sciences un ensayo clínico de mMIDST: tonos personalizados incrustados en música, 1 hora al día. Redujo la severidad del tinnitus más que el control a los 2 y 3 meses.

🔗 https://labonce.cl/blog/terapia-sonora-mmidst-tinnitus-brain-sciences/
```

**X — respuesta opcional (hilo):**
```
Estudio aleatorizado, controlado y simple ciego (Hospital Clínico U. de Chile + Clínica Alemana–UDD). Alternativa no invasiva, bien tolerada y personalizable.

Artículo abierto en Brain Sciences: https://www.mdpi.com/2076-3425/16/6/644
#tinnitus #terapiasonora
```

**Instagram — caption:**
```
🎵 Una terapia para el tinnitus… escondida en la música.

Publicamos en Brain Sciences (MDPI) un ensayo clínico de una nueva estrategia de terapia sonora para el tinnitus crónico: la mMIDST.

La idea: el tinnitus se asocia a una sincronización "aberrante" de redes cerebrales. Varias terapias buscan desincronizar esos patrones, pero exigen sesiones largas y poco prácticas. Nuestro protocolo incrusta tonos terapéuticos personalizados —ajustados a la frecuencia del tinnitus de cada paciente— dentro de la música, para escuchar 1 hora al día.

El resultado: en un estudio aleatorizado, controlado y simple ciego (Hospital Clínico U. de Chile + Clínica Alemana–UDD), el grupo que usó mMIDST redujo la severidad del tinnitus (THI) significativamente más que el control a los 2 y 3 meses, con buena tolerancia. Una alternativa no invasiva, factible y personalizable.

🔗 Artículo completo (acceso abierto) y nota en labonce.cl (link en la bio).

#tinnitus #terapiasonora #música #neurociencia #otoneurología #investigación #saludauditiva #ClínicaAlemana #UniversidadDeChile
```

---

## Notas

- **X permite hilos:** publica primero el tweet principal y responde con el opcional para el
  detalle técnico. Si prefieres un solo tweet, usa solo el principal.
- **Instagram no admite links clicables en el caption:** por eso el cierre dice "link en la
  bio". Mantén el link de la última noticia en tu bio, o usa un enlace tipo Linktree.
- **Verificar la URL** antes de publicar: el slug es el nombre del archivo `.md` sin extensión.
- Si una noticia no trae imagen propia, avísale a Cowork: se puede sugerir/generar una o usar
  el logo de LAB ONCE.
