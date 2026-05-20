import { motion } from 'framer-motion'
import { aboutText, timeline } from '../data/dlci'
import { SectionHeading } from './SectionHeading'

export function About() {
  return (
    <section id="nosotros" className="section-pad section-surface">
      <div className="mx-auto max-w-6xl">
        <SectionHeading
          eyebrow="Sobre nosotros"
          title="Ingeniería eléctrica con trayectoria comprobada"
          subtitle="Más de 15 años ejecutando proyectos eléctricos en República Dominicana."
        />

        <motion.p
          initial={{ opacity: 0, y: 12 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mx-auto max-w-3xl text-center text-base leading-relaxed text-dlci-dark/85 sm:text-lg"
        >
          {aboutText}
        </motion.p>

        <div className="mt-12 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {timeline.map((item, i) => (
            <motion.div
              key={item.year}
              initial={{ opacity: 0, y: 16 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.08 }}
              className="card-premium p-5"
            >
              <p className="font-display text-xl font-bold text-dlci-blue">{item.year}</p>
              <p className="mt-2 text-sm leading-relaxed text-dlci-dark/80">{item.label}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
