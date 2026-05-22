import { company } from '../data/dlci'

const STORAGE_KEY = 'dlci-site-version'

/** Si hay una versión nueva desplegada, recarga una vez para descartar HTML/JS en caché. */
export function ensureFreshSiteOnVisit() {
  const current = company.assetsVersion
  const previous = localStorage.getItem(STORAGE_KEY)

  if (previous === current) return

  localStorage.setItem(STORAGE_KEY, current)

  if (previous === null) return

  const url = new URL(window.location.href)
  if (url.searchParams.get('v') === current) return

  url.searchParams.set('v', current)
  window.location.replace(url.pathname + url.search + url.hash)
}
