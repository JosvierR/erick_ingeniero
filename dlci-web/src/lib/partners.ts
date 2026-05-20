/** Iniciales para monograma (omite artículos y conectores) */
export function partnerInitials(name: string): string {
  const skip = new Set(['de', 'la', 'el', 'los', 'las', 'y', '&'])
  const words = name
    .split(/[\s&]+/)
    .map((w) => w.replace(/[^a-zA-ZáéíóúñÁÉÍÓÚÑ]/g, ''))
    .filter((w) => w.length > 1 && !skip.has(w.toLowerCase()))

  if (words.length === 0) return name.charAt(0).toUpperCase()
  if (words.length === 1) return words[0].slice(0, 2).toUpperCase()
  return (words[0].charAt(0) + words[1].charAt(0)).toUpperCase()
}

/** Tono sutil distinto por nombre (marca corporativa) */
export function partnerAccent(name: string): string {
  let hash = 0
  for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash)
  const hues = [220, 210, 235, 200, 225]
  const h = hues[Math.abs(hash) % hues.length]
  return `hsl(${h} 28% 94%)`
}
