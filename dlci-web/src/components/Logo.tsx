import { assetUrl, company } from '../data/dlci'

type Props = {
  /** Logo claro para fondos oscuros (hero, navbar sobre hero) */
  variant?: 'dark' | 'light'
  className?: string
}

export function Logo({ variant = 'dark', className = '' }: Props) {
  const src = variant === 'light' ? '/dlci/logo-light.png' : '/dlci/logo-transparent.png'

  return (
    <img
      src={assetUrl(src)}
      alt={company.name}
      className={`h-9 w-auto object-contain object-left sm:h-10 ${className}`}
      width={140}
      height={44}
      decoding="async"
    />
  )
}
