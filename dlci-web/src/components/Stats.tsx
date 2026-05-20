import { motion } from 'framer-motion'
import { stats } from '../data/dlci'
import { SectionHeading } from './SectionHeading'

export function Stats() {
  return (
    <section className="section-pad bg-white">
      <div className="mx-auto max-w-6xl">
        <SectionHeading
          eyebrow="Confianza"
          title="Indicadores que respaldan nuestra experiencia"
          subtitle="Soluciones para construcción, comercio e industria."
        />

        <div className="grid grid-cols-2 gap-3 sm:gap-4 lg:grid-cols-3 lg:gap-5">
          {stats.map((stat, i) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, y: 12 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.04 }}
              className="stat-card"
            >
              <strong>{stat.value}</strong>
              <span>{stat.label}</span>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
