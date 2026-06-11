# GUÍA DE DEPLOY — LAB ONCE (paso a paso para Hayo)

El sitio ya está construido en `E:\Git_Use_LabOnce`. Esta guía es para publicarlo en GitHub
Pages en **tu otra cuenta de GitHub** (la asociada a hayo.bk). Solo tú puedes hacer esto
porque requiere tus credenciales.

---

## Paso 0 — (Recomendado) Probar el build local
Tienes Hugo extended 0.162.1 instalado (el mismo del sitio de Neurociencia). En PowerShell:

```powershell
cd E:\Git_Use_LabOnce
$env:HUGO_ENVIRONMENT="production"; hugo --minify
```

Debe terminar **sin `ERROR`** y crear la carpeta `public/`. Para previsualizar:

```powershell
hugo server
# abre http://localhost:1313/
```

Si aparece algún `ERROR`, cópialo y pásamelo: lo corregimos antes de publicar.

> Nota: el `baseURL` de `config/_default/hugo.yaml` es un **placeholder** (`USUARIO/REPO`).
> En producción NO importa: el workflow de GitHub fija automáticamente la URL real de Pages.
> Solo en `hugo server` local algunos links pueden verse raros; es normal.

---

## Paso 1 — Crear el repositorio en la OTRA cuenta de GitHub
1. Inicia sesión en GitHub con la cuenta asociada a **hayo.bk**.
2. Crea un repositorio **nuevo y vacío** (sin README), por ejemplo llamado `Web` o `labonce`.
   - Público (para GitHub Pages gratis).
   - NO agregues README, .gitignore ni licencia (el repo local ya los tiene).
3. Anota el `USUARIO` y el `REPO`. La URL final del sitio será:
   `https://USUARIO.github.io/REPO/`

---

## Paso 2 — (Opcional) Fijar el baseURL local
Para que el build local genere links correctos, edita `config/_default/hugo.yaml`:

```yaml
baseURL: "https://USUARIO.github.io/REPO/"
```

(reemplaza USUARIO y REPO por los reales). No es obligatorio para producción.

---

## Paso 3 — Primer push
Tienes dos opciones para autenticarte en la otra cuenta:

**Opción A — GitHub CLI (`gh`), la más simple:**
```powershell
gh auth login          # elige la cuenta hayo.bk
cd E:\Git_Use_LabOnce
git init
git add -A
git commit -m "LAB ONCE: primera versión del sitio (Hugo autocontenido)"
git branch -M main
gh repo create USUARIO/REPO --public --source . --remote origin --push
```

**Opción B — Git + URL del remoto (HTTPS con token o SSH):**
```powershell
cd E:\Git_Use_LabOnce
git init
git add -A
git commit -m "LAB ONCE: primera versión del sitio (Hugo autocontenido)"
git branch -M main
git remote add origin https://github.com/USUARIO/REPO.git
git push -u origin main
```

(También puedes usar el script `setup-git.ps1` de este repo: te pide USUARIO/REPO y hace todo.)

---

## Paso 4 — Activar GitHub Pages
1. En GitHub: repo → **Settings → Pages**.
2. En **Build and deployment → Source**, elige **GitHub Actions**.
3. El workflow `Deploy Hugo site to Pages` se ejecuta solo en cada push a `main`
   (pestaña **Actions**). Espera a que quede verde.
4. El sitio queda en `https://USUARIO.github.io/REPO/`.

---

## Paso 5 — Pages CMS (edición sin código)
1. Entra a `app.pagescms.org` → login con GitHub (cuenta hayo.bk).
2. Abre el repo `REPO`. El `.pages.yml` ya define las colecciones (Integrantes, Publicaciones,
   Proyectos, Blog, Recursos, Ajustes).
3. **Recomendación**: crea una rama de trabajo (`trabajo`) y apunta el CMS a esa rama, no a
   `main`, para revisar antes de publicar. (Igual que en el sitio de Neurociencia.)

---

## Flujo de trabajo posterior
- Cada push a `main` re-despliega el sitio.
- Para seguir portando contenido del Wix o ajustar diseño, trabaja con Claude (modo dual o
  edición directa) sobre `E:\Git_Use_LabOnce`. Ver `CONTINUACION-LABONCE.md`.
