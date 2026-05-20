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
    <section id="servicios" className="section-pad blueprint-bg-alt">
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
                className="card-premium flex h-full flex-col p-6"
              >
                <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-2xl bg-dlci-blue/10 text-dlci-blue">
                  <Icon size={22} aria-hidden />
                </div>
                <h3 className="font-display text-lg font-bold text-dlci-blue">{service.title}</h3>
                <p className="mt-2 text-sm leading-relaxed text-dlci-dark/75">{service.description}</p>
                <ul className="mt-4 flex flex-1 flex-col gap-1.5 border-t border-[#E5E7EB] pt-4">
                  {service.scope.map((item) => (
                    <li key={item} className="flex gap-2 text-sm text-dlci-dark/80">
                      <span className="mt-2 h-1 w-1 shrink-0 rounded-full bg-dlci-accent" aria-hidden />
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
