# Desplegar en Netlify — DLCI Electricidad

## Opción A: Conectar el repositorio completo (`erick_ingeniero`)

El archivo **`netlify.toml`** en la raíz del repo ya define:

- **Base directory:** `dlci-web`
- **Build:** `npm run build`
- **Publish:** `dlci-web/dist`

Pasos:

1. [app.netlify.com](https://app.netlify.com) → **Add new site** → **Import an existing project**
2. Conecta GitHub/GitLab y elige el repo `erick_ingeniero`
3. Netlify detectará el `netlify.toml` de la raíz (no cambies base ni publish manualmente)
4. En **Site configuration** → **Environment variables**, añade:

   | Variable | Valor |
   |----------|--------|
   | `VITE_SITE_URL` | URL del sitio, ej. `https://dlci-electricidad.netlify.app` (sin `/` final) |

5. **Deploy site**
6. Tras el primer deploy, copia la URL y actualiza `VITE_SITE_URL` si usaste un placeholder → **Trigger deploy**

## Opción B: Solo la carpeta `dlci-web`

Si subes únicamente `dlci-web` como repo:

- Usa el `netlify.toml` dentro de `dlci-web/`
- Mismas variables de entorno

## Dominio personalizado (opcional)

1. Netlify → **Domain management** → añade tu dominio
2. Actualiza en `src/data/contact.json`:
   - `website` → `https://tudominio.com`
3. Actualiza `VITE_SITE_URL` → misma URL
4. Redeploy

## Programar la tarjeta NFC

URL a grabar en la tarjeta = **`VITE_SITE_URL`** (o dominio custom).

## Formulario de contacto

El formulario usa **Netlify Forms** (`dlci-contacto`).

Tras el primer deploy:

1. Netlify → **Forms** → debe aparecer `dlci-contacto`
2. Opcional: **Form notifications** → email a `Info@dlci.com.do`
3. Probar envío desde la sección Contacto del sitio

En local (`npm run dev`) el envío puede fallar; se abre el correo como respaldo.

## Verificación post-deploy

- [ ] Abrir el sitio en el móvil
- [ ] Probar formulario de contacto (mensaje de éxito)
- [ ] WhatsApp abre con el mensaje correcto
- [ ] Llamar usa el número real
- [ ] `/dlci-contact.vcf` descarga el contacto
- [ ] Instagram / Facebook abren los perfiles correctos

## Datos de contacto

Antes del deploy, edita **`src/data/contact.json`**. Guía completa: **[CONTACTO.md](./CONTACTO.md)**.
