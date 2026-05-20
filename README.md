# DLCI Electricidad — Tarjeta NFC

Repositorio con documentación corporativa (PDF) y la **landing page NFC** en la carpeta [`dlci-web/`](dlci-web/).

## Landing web

```bash
cd dlci-web
npm install
npm run dev
```

- **Datos a reemplazar:** [`dlci-web/CONTACTO.md`](dlci-web/CONTACTO.md) → editar `dlci-web/src/data/contact.json`
- **Despliegue Netlify:** [`dlci-web/NETLIFY.md`](dlci-web/NETLIFY.md) (ya configurado `netlify.toml` en raíz y en `dlci-web/`)

## PDFs de referencia

- Información General DLCI Electricidad
- Manual Corporativo DLCI
- Portafolio DLCI Electricidad

Las imágenes del sitio se generaron a partir de estos PDFs (`extracted/` y `setup_assets.py`).
