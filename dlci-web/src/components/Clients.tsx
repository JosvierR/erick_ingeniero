import { motion } from 'framer-motion'
import { Building2, Handshake, Package } from 'lucide-react'
import { clients, providers } from '../data/dlci'
import { partnerAccent, partnerInitials } from '../lib/partners'
import { SectionHeading } from './SectionHeading'

type PartnerListProps = {
  items: readonly string[]
  title: string
  description: string
  icon: typeof Building2
  variant: 'client' | 'provider'
}

function PartnerList({ items, title, description, icon: Icon, variant }: PartnerListProps) {
  return (
    <div className="partner-panel">
      <div className="partner-panel-header">
        <span className={`partner-panel-icon partner-panel-icon--${variant}`}>
          <Icon size={20} aria-hidden />
        </span>
        <div>
          <h3 className="font-display text-lg font-bold text-dlci-blue">{title}</h3>
          <p className="mt-0.5 text-sm text-dlci-dark/55">{description}</p>
        </div>
        <span className="partner-count">Destacados</span>
      </div>

      <ul className="mt-5 grid gap-2.5 sm:grid-cols-2">
        {items.map((name, i) => (
          <motion.li
            key={name}
            initial={{ opacity: 0, y: 10 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: Math.min(i * 0.03, 0.24) }}
          >
            <div className="partner-card group">
              <span
                className="partner-monogram"
                style={{ background: partnerAccent(name) }}
                aria-hidden
              >
                {partnerInitials(name)}
              </span>
              <span className="min-w-0 flex-1">
                <span className="block text-sm font-semibold leading-snug text-dlci-dark group-hover:text-dlci-blue">
                  {name}
                </span>
                <span className="mt-0.5 block text-[10px] font-medium uppercase tracking-[0.14em] text-dlci-dark/40">
                  {variant === 'client' ? 'Cliente' : 'Proveedor'}
                </span>
              </span>
            </div>
          </motion.li>
        ))}
      </ul>
    </div>
  )
}

export function Clients() {
  return (
    <section className="section-pad bg-white">
      <div className="mx-auto max-w-6xl">
        <SectionHeading
          eyebrow="Red de confianza"
          title="Clientes y aliados estratégicos"
          subtitle="Empresas con las que hemos construido relaciones duraderas en obra y en ingeniería eléctrica."
        />

        <div className="mb-8 flex flex-wrap items-center justify-center gap-6 text-center sm:gap-10">
          <div className="flex items-center gap-2 text-sm text-dlci-dark/60">
            <Handshake size={18} className="text-dlci-accent" aria-hidden />
            <span>
              <strong className="font-semibold text-dlci-blue">Clientes</strong> destacados
            </span>
          </div>
          <div className="hidden h-4 w-px bg-[#E8ECF1] sm:block" aria-hidden />
          <div className="flex items-center gap-2 text-sm text-dlci-dark/60">
            <Package size={18} className="text-dlci-accent" aria-hidden />
            <span>
              <strong className="font-semibold text-dlci-blue">Proveedores</strong> destacados
            </span>
          </div>
        </div>

        <div className="grid gap-6 lg:grid-cols-2 lg:gap-8">
          <PartnerList
            items={clients}
            title="Clientes"
            description="Constructoras e ingenierías con proyectos ejecutados."
            icon={Building2}
            variant="client"
          />
          <PartnerList
            items={providers}
            title="Proveedores"
            description="Suministro confiable de materiales y equipos."
            icon={Package}
            variant="provider"
          />
        </div>
      </div>
    </section>
  )
}
