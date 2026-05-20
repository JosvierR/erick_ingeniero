import { motion } from 'framer-motion'
import { missionVision } from '../data/dlci'
import { SectionHeading } from './SectionHeading'

export function MissionVision() {
  return (
    <section className="section-pad section-surface">
      <div className="mx-auto max-w-6xl">
        <SectionHeading eyebrow="Propósito" title="Misión, visión y valores" />

        <div className="grid gap-6 lg:grid-cols-2">
          <motion.div
            initial={{ opacity: 0, y: 12 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="card-premium p-6 sm:p-8"
          >
            <h3 className="font-display text-lg font-bold text-dlci-blue">Misión</h3>
            <p className="mt-3 text-sm leading-relaxed text-dlci-dark/80 sm:text-base">{missionVision.mission}</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 12 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.08 }}
            className="card-premium p-6 sm:p-8"
          >
            <h3 className="font-display text-lg font-bold text-dlci-blue">Visión</h3>
            <p className="mt-3 text-sm leading-relaxed text-dlci-dark/80 sm:text-base">{missionVision.vision}</p>
          </motion.div>
        </div>

        <motion.div
          initial={{ opacity: 0, y: 12 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="card-premium mt-6 p-6 sm:p-8"
        >
          <h3 className="font-display text-lg font-bold text-dlci-blue">Valores</h3>
          <ul className="mt-4 flex flex-wrap gap-2">
            {missionVision.values.map((value) => (
              <li
                key={value}
                className="rounded-xl border border-dlci-blue/15 bg-dlci-blue/5 px-3 py-2 text-sm font-medium text-dlci-blue"
              >
                {value}
              </li>
            ))}
          </ul>
        </motion.div>
      </div>
    </section>
  )
}
