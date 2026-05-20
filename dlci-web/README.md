# DLCI Electricidad — Tarjeta NFC / Landing

Landing page mobile-first para la tarjeta NFC de **DLCI Electricidad**. React + TypeScript + Vite + Tailwind CSS.

## Requisitos

- Node.js 18+
- npm

## Cómo correr el proyecto

```bash
cd dlci-web
npm install
npm run dev
```

## Desplegar en Netlify

Configuración lista. Sigue **[NETLIFY.md](./NETLIFY.md)**.

Resumen:

1. Conecta el repo en Netlify (usa `netlify.toml` de la raíz del monorepo o de `dlci-web`)
2. Variable de entorno: `VITE_SITE_URL` = URL pública del sitio
3. Edita **`src/data/contact.json`** antes del deploy

## Datos que debes reemplazar

Lista detallada en **[CONTACTO.md](./CONTACTO.md)**.

**Archivo principal:** `src/data/contact.json` (teléfono, email, web, mapas, redes). El vCard se genera solo al compilar.

## Imágenes

Carpeta `public/dlci/` — ver CONTACTO.md sección 5.

## Contenido (servicios, proyectos, etc.)

`src/data/dlci.ts`

## Scripts

| Comando | Descripción |
|---------|-------------|
| `npm run dev` | Desarrollo local |
| `npm run build` | Genera vCard + build producción |
| `npm run preview` | Vista previa del build |
