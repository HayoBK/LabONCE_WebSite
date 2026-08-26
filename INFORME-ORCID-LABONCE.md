# Informe de búsqueda de ORCID iD — LAB ONCE

Generado el 25 de agosto de 2026, durante la migración del sistema de publicaciones a ORCID.

## Qué se sincroniza automáticamente

`data/orcid.yaml` solo trae el ORCID de **Hayo Breinbauer** (`0000-0002-3278-065X`). Es una
decisión deliberada, no un pendiente: hoy la producción científica real de LAB ONCE es, en la
práctica, la de su director. El resto del equipo puede tener su propio ORCID mostrado como link
en su ficha (ver más abajo), pero eso **no** activa ninguna sincronización de publicaciones —
ese campo y la lista de `data/orcid.yaml` son independientes.

## Qué se completó en las fichas personales (`content/integrantes/*.md`, campo `orcid`)

| Persona | ORCID iD | Cómo se confirmó |
|---|---|---|
| Hayo Breinbauer | 0000-0002-3278-065X | Ya conocido (es la fuente de la sincronización) |
| Paul Délano | 0000-0003-2588-4757 | Ficha propia en el sitio del Depto. de Neurociencia (`content/academicos/paul-delano/`), afiliación coincide exactamente |
| Pablo Pozo | 0009-0002-1841-0801 | Coincide con "Pablo Pozo Santelices" en el sitio de Neurosistemas (mismo perfil: psicólogo clínico, neuropsicólogo) |

## Alta sospecha, sin confirmar — necesita tu visto bueno

**Andrés Contreras** — en Neurosistemas existe un "Andrés Contreras", psicólogo, tesista del
Magíster en Neurociencias de la Universidad de Chile, ORCID `0009-0009-8317-106X`. El nombre
coincide exactamente con tu alumno de LAB ONCE, pero esa ficha no menciona otoneurología, vértigo
ni Lab-ONCE, así que no lo di por confirmado. Si es la misma persona, dímelo y agrego el ORCID a
su ficha en una línea.

## Identidad y afiliación confirmadas, pero sin ORCID iD extraído

Un agente de búsqueda intentó consultar la API pública de ORCID para el resto del equipo y no
pudo acceder directamente (bloqueada para ese entorno). Para estas seis personas sí confirmó
identidad y afiliación por otras fuentes, así que la búsqueda manual en
[orcid.org/orcid-search](https://orcid.org/orcid-search/search) debería ser rápida si filtras por
el nombre + la afiliación indicada:

- **Phoebe Ramos** — Otorrinolaringología PUC, área neurotología y vértigo.
- **Daniela Contreras** — Servicio de ORL, Hospital Clínico La Florida Dra. Eloísa Díaz Insunza.
- **Diego Herrero** — Neurólogo, Clínica Alemana de Santiago.
- **Rosario Garrido** — coautora confirmada en el paper de Brain Sciences 2024 (Laboratorio de
  Otoneurología Clínica, Depto. de Neurociencia, U. de Chile), pero ni Crossref ni la página del
  artículo traen su ORCID.
- **Felipe Faúndez** — coautor/primer autor confirmado en el paper de Frontiers in Neurology 2025
  (mismo laboratorio), igual sin ORCID en Crossref/Frontiers.
- **Cristián Barraza** — ficha docente en uandes.cl, Escuela de Fonoaudiología, Universidad de
  los Andes.

## Sin ningún rastro público

**Asunción Ruiz**, **Pía Michael**, **Marcia Núñez**. Es probable que no tengan perfil ORCID
público, o que esté en privado. No es un error del sitio — igual que en Neurosistemas, hay
integrantes sin ORCID y sus fichas funcionan igual, solo sin el chip de enlace.

## Cómo completar lo que falta

1. Abre la ficha de la persona en `content/integrantes/<slug>.md` (o desde Pages CMS, colección
   "Equipo").
2. Pega su ORCID iD en el campo `orcid` (formato `0000-0000-0000-0000`, sin el prefijo
   `https://orcid.org/`).
3. Guarda. El chip "ORCID ..." aparece solo en su ficha individual — no cambia el listado
   agregado de `/publicaciones/todas/`, que sigue viniendo solo del ORCID del director hasta que
   decidas agregar a alguien más a `data/orcid.yaml`.
