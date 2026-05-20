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
    <motion.header
      initial={{ opacity: 0, y: 14 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-60px' }}
      transition={{ duration: 0.45 }}
      className={`mb-12 md:mb-14 ${center ? 'mx-auto max-w-3xl text-center' : 'max-w-2xl'}`}
    >
      {eyebrow && (
        <p
          className={`section-eyebrow ${center ? 'justify-center' : ''} ${
            light ? 'text-white/65' : 'text-dlci-dark/50'
          }`}
        >
          <span className={`section-eyebrow-line ${light ? 'bg-white/40' : 'bg-dlci-blue/35'}`} aria-hidden />
          {eyebrow}
        </p>
      )}
      <h2
        className={`font-display text-[1.65rem] font-bold leading-[1.2] tracking-tight sm:text-3xl lg:text-[2.125rem] ${
          light ? 'text-white' : 'text-[#252b3d]'
        }`}
      >
        {title}
      </h2>
      {subtitle && (
        <p
          className={`mt-4 text-[15px] leading-relaxed sm:text-base ${
            light ? 'text-white/78' : 'text-dlci-dark/72'
          }`}
        >
          {subtitle}
        </p>
      )}
    </motion.header>
  )
}
