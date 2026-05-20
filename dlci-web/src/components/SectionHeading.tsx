import { motion } from 'framer-motion'

type Props = {
  eyebrow?: string
  title: string
  subtitle?: string
  light?: boolean
  center?: boolean
}

export function SectionHeading({ eyebrow, title, subtitle, light, center = true }: Props) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-80px' }}
      transition={{ duration: 0.5 }}
      className={`mb-10 max-w-3xl ${center ? 'mx-auto text-center' : ''}`}
    >
      {eyebrow && (
        <p
          className={`font-mono-accent mb-3 text-xs font-medium uppercase tracking-[0.2em] ${
            light ? 'text-white/70' : 'text-dlci-accent'
          }`}
        >
          {eyebrow}
        </p>
      )}
      <h2
        className={`font-display text-2xl font-bold tracking-tight sm:text-3xl lg:text-4xl ${
          light ? 'text-white' : 'text-dlci-blue'
        }`}
      >
        {title}
      </h2>
      {subtitle && (
        <p className={`mt-4 text-base leading-relaxed sm:text-lg ${light ? 'text-white/80' : 'text-dlci-dark/80'}`}>
          {subtitle}
        </p>
      )}
    </motion.div>
  )
}
