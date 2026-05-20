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

        <div className="grid grid-cols-2 gap-4 lg:grid-cols-3 lg:gap-6">
          {stats.map((stat, i) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, scale: 0.96 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.05 }}
              className="card-premium flex flex-col items-center justify-center p-6 text-center sm:p-8"
            >
              <p className="font-display text-3xl font-bold text-dlci-blue sm:text-4xl">{stat.value}</p>
              <p className="mt-2 text-sm font-medium text-dlci-dark/75">{stat.label}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
