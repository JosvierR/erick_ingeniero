import type { CSSProperties } from 'react'
import { motion } from 'framer-motion'
import { ArrowDown, ChevronRight, Download, MessageCircle, Phone, Shield } from 'lucide-react'
import { assetUrl, company, stats } from '../data/dlci'
import { telUrl, whatsappUrl } from '../lib/links'

const heroStats = stats.slice(0, 3)

export function Hero() {
  return (
    <section
      id="inicio"
      className="hero-section relative min-h-[100dvh] overflow-hidden bg-[#1a2236] pt-[max(4.5rem,env(safe-area-inset-top))] text-white"
      style={
        { '--hero-bg-image': `url(${assetUrl(company.assets.heroBackground)})` } as CSSProperties
      }
    >
      <div className="hero-bg-photo" aria-hidden>
        <img
          src={assetUrl(company.assets.heroBackground)}
          alt=""
          className="hero-bg-photo__img"
          width={1920}
          height={1080}
          fetchPriority="high"
        />
      </div>
      <div className="hero-bg-overlay pointer-events-none absolute inset-0" aria-hidden />
      <div className="hero-grid pointer-events-none absolute inset-0" aria-hidden />

      <div className="relative mx-auto grid max-w-6xl gap-10 px-4 pb-[calc(7.5rem+env(safe-area-inset-bottom,0px))] pt-6 sm:px-6 lg:grid-cols-[1.05fr_0.95fr] lg:items-center lg:gap-12 lg:px-8 lg:pb-28 lg:pt-10">
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
            <span className="block text-white drop-shadow-sm">{company.tagline.split(',')[0]},</span>
            <span className="mt-1 block text-white/95 drop-shadow-sm">
              {company.tagline.includes(',') ? company.tagline.split(',')[1].trim() : company.tagline}
            </span>
          </h1>

          <p className="mt-5 max-w-lg text-base leading-relaxed text-white/90 drop-shadow-sm sm:text-lg">
            {company.subtitle}
          </p>

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
                <span className="text-white/70">{stat.label}</span>
              </motion.span>
            ))}
          </div>

          <div className="mt-8 flex flex-col gap-3 sm:flex-row sm:flex-wrap">
            <a
              href={whatsappUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="hero-cta-primary shadow-lg"
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
          className="relative z-10 hidden sm:block lg:pl-2"
        >
          <div className="hero-visual">
            <div className="hero-visual__media" role="img" aria-label="Proyecto eléctrico DLCI Electricidad" />
            <div className="hero-visual__shade" aria-hidden />
            <div className="hero-visual__copy">
              <p className="font-mono-accent text-[10px] uppercase tracking-[0.2em] text-white/60">
                Proyectos reales · República Dominicana
              </p>
              <p className="font-display mt-1 text-base font-semibold leading-snug text-white sm:text-lg">
                Ingeniería eléctrica con calidad, seguridad y eficiencia
              </p>
            </div>
            <div className="hero-visual__nfc">
              <p className="text-[10px] font-medium uppercase tracking-wider text-white/50">Tarjeta NFC</p>
              <p className="font-display text-sm font-semibold text-white">Contacto al instante</p>
            </div>
          </div>
        </motion.div>
      </div>

      <motion.a
        href="#acciones"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.9 }}
        className="hero-scroll-cue z-20"
        aria-label="Descubrir más contenido"
      >
        <span className="font-mono-accent text-[10px] uppercase tracking-[0.25em] text-white/55">Descubrir</span>
        <span className="flex h-10 w-10 items-center justify-center rounded-full border border-white/20 bg-black/20 backdrop-blur-sm">
          <ArrowDown size={18} className="animate-hero-bounce" aria-hidden />
        </span>
      </motion.a>
    </section>
  )
}
