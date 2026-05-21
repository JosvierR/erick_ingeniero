import { motion } from 'framer-motion'
import { Building2, Package } from 'lucide-react'
import { clients, providers, type Partner } from '../data/dlci'
import { SectionHeading } from './SectionHeading'

type PartnerStripProps = {
  items: readonly Partner[]
  title: string
  description: string
  icon: typeof Building2
  variant: 'client' | 'provider'
}

function PartnerLogo({ partner }: { partner: Partner }) {
  return (
    <div className="partner-logo-cell" title={partner.name}>
      {partner.logo ? (
        <img
          src={partner.logo}
          alt={partner.name}
          loading="lazy"
          decoding="async"
          className="partner-logo-img"
        />
      ) : (
        <span className="partner-logo-placeholder">{partner.name}</span>
      )}
    </div>
  )
}

function PartnerStrip({ items, title, description, icon: Icon, variant }: PartnerStripProps) {
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

      <ul className="partner-logo-strip" aria-label={title}>
        {items.map((partner, i) => (
          <motion.li
            key={partner.name}
            initial={{ opacity: 0, y: 8 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: Math.min(i * 0.04, 0.28) }}
            className="flex"
          >
            <PartnerLogo partner={partner} />
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

        <div className="grid gap-6 lg:grid-cols-2 lg:items-stretch lg:gap-8">
          <PartnerStrip
            items={clients}
            title="Clientes"
            description="Constructoras e ingenierías con proyectos ejecutados."
            icon={Building2}
            variant="client"
          />
          <PartnerStrip
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
