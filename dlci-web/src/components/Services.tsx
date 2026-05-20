import { motion } from 'framer-motion'
import {
  ClipboardCheck,
  Factory,
  HardHat,
  Layers,
  Package,
  Zap,
  type LucideIcon,
} from 'lucide-react'
import { services } from '../data/dlci'
import { SectionHeading } from './SectionHeading'

const iconMap: Record<string, LucideIcon> = {
  blueprint: Layers,
  clipboard: ClipboardCheck,
  zap: Zap,
  factory: Factory,
  'hard-hat': HardHat,
  package: Package,
}

export function Services() {
  return (
    <section id="servicios" className="section-pad section-surface">
      <div className="mx-auto max-w-6xl">
        <SectionHeading
          eyebrow="Servicios"
          title="Soluciones eléctricas integrales"
          subtitle="Del diseño a la puesta en servicio, con cumplimiento normativo y control de calidad."
        />

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {services.map((service, i) => {
            const Icon = iconMap[service.icon] ?? Zap
            return (
              <motion.article
                key={service.id}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: '-40px' }}
                transition={{ delay: (i % 3) * 0.08 }}
                className="service-card"
              >
                <div className="service-card-icon">
                  <Icon size={20} aria-hidden />
                </div>
                <h3 className="font-display text-[17px] font-bold text-dlci-ink">{service.title}</h3>
                <p className="mt-2 text-[14px] leading-relaxed text-dlci-dark/68">{service.description}</p>
                <ul className="mt-5 flex flex-1 flex-col gap-2 border-t border-[#EEF1F5] pt-5">
                  {service.scope.map((item) => (
                    <li key={item} className="text-[13px] leading-snug text-dlci-dark/72">
                      {item}
                    </li>
                  ))}
                </ul>
              </motion.article>
            )
          })}
        </div>
      </div>
    </section>
  )
}
