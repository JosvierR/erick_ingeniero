import { motion } from 'framer-motion'
import { processSteps } from '../data/dlci'
import { SectionHeading } from './SectionHeading'

export function Process() {
  return (
    <section className="section-pad bg-white">
      <div className="mx-auto max-w-6xl">
        <SectionHeading
          eyebrow="Proceso"
          title="Metodología estructurada y confiable"
          subtitle="Un flujo claro para proyectos eléctricos de cualquier escala."
        />

        <div className="relative">
          <div className="absolute left-4 top-0 hidden h-full w-px bg-dlci-blue/15 md:left-1/2 md:block" aria-hidden />

          <ol className="space-y-6 md:space-y-8">
            {processSteps.map((step, i) => (
              <motion.li
                key={step.step}
                initial={{ opacity: 0, x: i % 2 === 0 ? -16 : 16 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                className={`relative flex flex-col gap-4 md:flex-row md:items-center ${
                  i % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse'
                }`}
              >
                <div className={`md:w-1/2 ${i % 2 === 0 ? 'md:pr-12 md:text-right' : 'md:pl-12'}`}>
                  <div
                    className={`card-premium inline-block w-full p-5 sm:p-6 ${
                      i % 2 === 0 ? 'md:ml-auto' : ''
                    }`}
                  >
                    <span className="font-mono-accent text-xs font-medium uppercase tracking-widest text-dlci-accent">
                      Paso {step.step}
                    </span>
                    <h3 className="font-display mt-2 text-lg font-bold text-dlci-blue">{step.title}</h3>
                    <p className="mt-2 text-sm leading-relaxed text-dlci-dark/75">{step.description}</p>
                  </div>
                </div>

                <div
                  className="absolute left-4 flex h-8 w-8 items-center justify-center rounded-full bg-dlci-blue text-sm font-bold text-white md:left-1/2 md:-translate-x-1/2"
                  aria-hidden
                >
                  {step.step}
                </div>

                <div className="hidden md:block md:w-1/2" />
              </motion.li>
            ))}
          </ol>
        </div>
      </div>
    </section>
  )
}
