# LAB ONCE — Sitio web

Sitio de **LAB ONCE — Laboratorio de Otoneurología Clínica y Neurociencias del Equilibrio**
(Clínica Alemana de Santiago · Departamento de Neurociencia, Universidad de Chile).

Reemplaza la antigua web en Wix. Construido con **Hugo extended** (sitio autocontenido,
sin temas ni módulos externos), desplegado en **GitHub Pages** y editable con **Pages CMS**.

## Desarrollo local
Requiere Hugo extended 0.162.1.

```bash
hugo server          # previsualización en http://localhost:1313/
HUGO_ENVIRONMENT=production hugo --minify   # build de producción (carpeta public/)
```

## Estructura
- `config/_default/` — configuración (hugo, menús, parámetros).
- `layouts/` — plantillas (sitio autocontenido).
- `static/css/labonce.css` — estilos propios (prefijo `lo-`).
- `data/` — datos editables (integrantes, publicaciones, proyectos).
- `content/` — páginas y blog.
- `.pages.yml` — configuración de Pages CMS.
- `.github/workflows/deploy.yml` — despliegue a GitHub Pages.

## Publicar
Ver **GUIA-DEPLOY-LABONCE.md**. Reglas y arquitectura en **CLAUDE.md**.
Estado y pendientes en **CONTINUACION-LABONCE.md**.

© LAB ONCE — Hayo Breinbauer.
