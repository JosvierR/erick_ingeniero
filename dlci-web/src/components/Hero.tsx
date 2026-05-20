import { motion } from 'framer-motion'
import { ArrowDown, ChevronRight, Download, MessageCircle, Phone, Shield } from 'lucide-react'
import { company, stats } from '../data/dlci'
import { telUrl, whatsappUrl } from '../lib/links'

const heroStats = stats.slice(0, 3)

export function Hero() {
  return (
    <section
      id="inicio"
      className="hero-section relative min-h-[100dvh] overflow-hidden bg-[#1a2236] pt-[4.5rem] text-white"
    >
      <div className="hero-grid pointer-events-none absolute inset-0" aria-hidden />
      <div className="pointer-events-none absolute inset-0 bg-gradient-to-br from-[#313D5E] via-[#28324d] to-[#1a2236]" />
      <div className="pointer-events-none absolute -left-32 top-20 h-96 w-96 rounded-full bg-[#4a6fa5]/20 blur-[100px]" />
      <div className="pointer-events-none absolute bottom-0 right-0 h-80 w-80 rounded-full bg-white/5 blur-[80px]" />

      <div className="relative mx-auto grid max-w-6xl gap-10 px-4 pb-32 pt-6 sm:px-6 lg:grid-cols-[1.05fr_0.95fr] lg:items-center lg:gap-12 lg:px-8 lg:pb-28 lg:pt-10">
        <motion.div
          initial={{ opacity: 0, y: 28 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.65, ease: [0.22, 1, 0.36, 1] }}
          className="z-10"
        >
          <span className="hero-badge">
            <Shield size={14} aria-hidden />
            {company.badge}
          </span>

          <div className="hero-accent-line mt-6" aria-hidden />

          <h1 className="font-display mt-5 text-[1.75rem] font-bold leading-[1.12] tracking-tight sm:text-4xl lg:text-[2.85rem]">
            <span className="block text-white">{company.tagline.split(',')[0]},</span>
            <span className="mt-1 block bg-gradient-to-r from-white via-white to-white/75 bg-clip-text text-transparent">
              {company.tagline.includes(',') ? company.tagline.split(',')[1].trim() : company.tagline}
            </span>
          </h1>

          <p className="mt-5 max-w-lg text-base leading-relaxed text-white/88 sm:text-lg">{company.subtitle}</p>

          <div className="mt-6 flex flex-wrap gap-2">
            {heroStats.map((stat, i) => (
              <motion.span
                key={stat.label}
                initial={{ opacity: 0, y: 8 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.35 + i * 0.08 }}
                className="hero-stat-pill"
              >
                <strong className="font-display text-white">{stat.value}</strong>
                <span className="text-white/65">{stat.label}</span>
              </motion.span>
            ))}
          </div>

          <div className="mt-8 flex flex-col gap-3 sm:flex-row sm:flex-wrap">
            <a
              href={whatsappUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="hero-cta-primary"
            >
              <MessageCircle size={20} aria-hidden />
              Contactar por WhatsApp
            </a>
            <a href={telUrl} className="hero-cta-secondary">
              <Phone size={18} aria-hidden />
              Llamar ahora
            </a>
            <a href={company.vcardPath} download className="hero-cta-secondary">
              <Download size={18} aria-hidden />
              Guardar contacto
            </a>
          </div>

          <div className="mt-6 flex flex-wrap items-center gap-4">
            <a href="#servicios" className="hero-text-link group">
              Ver servicios
              <ChevronRight size={16} className="transition group-hover:translate-x-0.5" aria-hidden />
            </a>
            <a href="#proyectos" className="hero-text-link group">
              Ver proyectos
              <ChevronRight size={16} className="transition group-hover:translate-x-0.5" aria-hidden />
            </a>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 32 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.75, delay: 0.12, ease: [0.22, 1, 0.36, 1] }}
          className="relative lg:pl-2"
        >
          <div className="hero-visual-frame">
            <div className="relative aspect-[4/3] overflow-hidden rounded-[20px] sm:rounded-[22px]">
              <img
                src={company.assets.hero}
                alt="Proyecto eléctrico DLCI Electricidad"
                className="h-full w-full object-cover"
                width={1200}
                height={675}
                fetchPriority="high"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-[#1a2236]/90 via-[#1a2236]/15 to-transparent" />
              <div className="absolute bottom-0 left-0 right-0 p-5 sm:p-6">
                <p className="font-mono-accent text-[10px] uppercase tracking-[0.2em] text-white/55">
                  Proyectos reales · República Dominicana
                </p>
                <p className="font-display mt-1 text-base font-semibold leading-snug text-white sm:text-lg">
                  Ingeniería eléctrica con calidad, seguridad y eficiencia
                </p>
              </div>
            </div>
          </div>

          <motion.div
            initial={{ opacity: 0, x: -12 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.5 }}
            className="absolute -bottom-3 -left-1 hidden rounded-2xl border border-white/15 bg-[#1a2236]/80 px-4 py-3 shadow-xl backdrop-blur-md sm:block"
          >
            <p className="text-[10px] font-medium uppercase tracking-wider text-white/50">Tarjeta NFC</p>
            <p className="font-display text-sm font-semibold text-white">Contacto al instante</p>
          </motion.div>
        </motion.div>
      </div>

      <motion.a
        href="#acciones"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.9 }}
        className="hero-scroll-cue"
        aria-label="Descubrir más contenido"
      >
        <span className="font-mono-accent text-[10px] uppercase tracking-[0.25em] text-white/50">Descubrir</span>
        <span className="flex h-10 w-10 items-center justify-center rounded-full border border-white/20 bg-white/5">
          <ArrowDown size={18} className="animate-hero-bounce" aria-hidden />
        </span>
      </motion.a>
    </section>
  )
}
