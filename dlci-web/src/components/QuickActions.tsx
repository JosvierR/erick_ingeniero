import type { AnchorHTMLAttributes, ComponentType } from 'react'
import { motion } from 'framer-motion'
import { Download, Mail, MapPin, MessageCircle, Phone } from 'lucide-react'
import { company } from '../data/dlci'
import { mailtoUrl, telUrl, whatsappUrl } from '../lib/links'

type ActionVariant = 'primary' | 'whatsapp' | 'neutral' | 'social' | 'save'

type QuickAction = {
  label: string
  sublabel?: string
  href: string
  icon: ComponentType<{ size?: number; className?: string; 'aria-hidden'?: boolean }>
  variant: ActionVariant
  external?: boolean
  download?: boolean
}

const actions: QuickAction[] = [
  {
    label: 'WhatsApp',
    sublabel: 'Respuesta rápida',
    href: whatsappUrl,
    icon: MessageCircle,
    variant: 'whatsapp',
    external: true,
  },
  { label: 'Llamar', sublabel: 'Oficina', href: telUrl, icon: Phone, variant: 'primary' },
  { label: 'Correo', sublabel: 'Escríbenos', href: mailtoUrl, icon: Mail, variant: 'neutral' },
  { label: 'Ubicación', href: company.mapsUrl, icon: MapPin, variant: 'neutral', external: true },
  { label: 'Instagram', href: company.instagram.url, icon: InstagramMark, variant: 'social', external: true },
  { label: 'Facebook', href: company.facebook.url, icon: FacebookMark, variant: 'social', external: true },
  { label: 'Contacto', sublabel: 'vCard', href: company.vcardPath, icon: Download, variant: 'save', download: true },
]

function InstagramMark({ size = 18, className }: { size?: number; className?: string }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" className={className} aria-hidden>
      <rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" strokeWidth="1.75" />
      <circle cx="12" cy="12" r="4" stroke="currentColor" strokeWidth="1.75" />
      <circle cx="17.2" cy="6.8" r="1" fill="currentColor" />
    </svg>
  )
}

function FacebookMark({ size = 18, className }: { size?: number; className?: string }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="currentColor" className={className} aria-hidden>
      <path d="M14 8.5h2.5V5H14c-2.2 0-3.5 1.4-3.5 3.6V11H9v3.5h1.5V22h3.5v-7.5H17l.6-3.5h-3.1v-2c0-1 .3-1.5 1.6-1.5z" />
    </svg>
  )
}

const variantStyles: Record<ActionVariant, string> = {
  whatsapp: 'action-pill action-pill--whatsapp border-[#E0E4EA] bg-white hover:border-[#25D366]/30',
  primary: 'action-pill border-[#E0E4EA] bg-white hover:border-dlci-blue/25',
  neutral: 'action-pill border-[#E0E4EA] bg-white hover:border-dlci-blue/20',
  social: 'action-pill border-[#E0E4EA] bg-white hover:border-dlci-blue/20',
  save: 'action-pill border-dlci-blue/20 bg-[#f4f6f9] hover:border-dlci-blue/35',
}

const iconStyles: Record<ActionVariant, string> = {
  whatsapp: 'bg-[#e8f7ed] text-[#1a8f47]',
  primary: 'bg-[#eef1f6] text-dlci-blue',
  neutral: 'bg-[#eef1f6] text-dlci-blue',
  social: 'bg-[#eef1f6] text-dlci-dark/65',
  save: 'bg-dlci-blue text-white',
}

export function QuickActions() {
  return (
    <section
      id="acciones"
      className="sticky top-[52px] z-40 border-b border-[#E8ECF1] bg-white/98 backdrop-blur-md"
    >
      <div className="mx-auto max-w-6xl px-4 py-4 sm:px-6 lg:px-8">
        <p className="mb-3 text-[11px] font-semibold uppercase tracking-[0.2em] text-dlci-dark/45">
          Contacto inmediato
        </p>

        <motion.div
          initial={{ opacity: 0, y: 6 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="flex gap-2.5 overflow-x-auto pb-0.5 [-ms-overflow-style:none] [scrollbar-width:none] sm:grid sm:grid-cols-4 sm:overflow-visible lg:grid-cols-7 [&::-webkit-scrollbar]:hidden"
        >
          {actions.map((action, i) => {
            const Icon = action.icon
            const props: AnchorHTMLAttributes<HTMLAnchorElement> = {}
            if (action.download) props.download = true
            if (action.external) {
              props.target = '_blank'
              props.rel = 'noopener noreferrer'
            }

            return (
              <motion.div
                key={action.label}
                initial={{ opacity: 0, y: 8 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.04 }}
                whileTap={{ scale: 0.98 }}
                className={action.variant === 'whatsapp' ? 'sm:col-span-2 lg:col-span-1' : ''}
              >
                <a
                  href={action.href}
                  {...props}
                  className={variantStyles[action.variant]}
                >
                  <span className={`action-pill-icon ${iconStyles[action.variant]}`}>
                    <Icon size={18} />
                  </span>
                  <span className="action-pill-text">
                    <span className="action-pill-label">{action.label}</span>
                    {action.sublabel && <span className="action-pill-sublabel">{action.sublabel}</span>}
                  </span>
                </a>
              </motion.div>
            )
          })}
        </motion.div>
      </div>
    </section>
  )
}
