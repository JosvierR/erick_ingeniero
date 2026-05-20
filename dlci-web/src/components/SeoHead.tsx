import { useEffect } from 'react'
import { absoluteAsset, company, siteUrl } from '../data/dlci'

/** Actualiza og:image con URL absoluta cuando VITE_SITE_URL está definida (Netlify). */
export function SeoHead() {
  useEffect(() => {
    if (!siteUrl) return
    const setMeta = (property: string, content: string) => {
      let el = document.querySelector(`meta[property="${property}"]`)
      if (!el) {
        el = document.createElement('meta')
        el.setAttribute('property', property)
        document.head.appendChild(el)
      }
      el.setAttribute('content', content)
    }
    setMeta('og:url', siteUrl)
    setMeta('og:image', absoluteAsset(company.assets.ogImage))
  }, [])

  return null
}
