import { motion } from 'framer-motion'
import { ArrowDown, Download, MessageCircle, Phone } from 'lucide-react'
import { company } from '../data/dlci'
import { telUrl, whatsappUrl } from '../lib/links'

export function Hero() {
  return (
    <section
      id="inicio"
      className="relative min-h-[100dvh] overflow-hidden bg-dlci-blue blueprint-bg pt-20 text-white"
    >
      <div className="pointer-events-none absolute inset-0 bg-gradient-to-br from-dlci-blue via-[#2a344f] to-[#1f2638]" />
      <div className="pointer-events-none absolute -right-20 top-1/3 h-72 w-72 rounded-full bg-dlci-accent/10 blur-3xl" />

      <div className="relative mx-auto grid max-w-6xl gap-10 px-4 pb-28 pt-8 sm:px-6 lg:grid-cols-2 lg:items-center lg:gap-14 lg:px-8 lg:pb-32 lg:pt-16">
        <motion.div
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="z-10"
        >
          <span className="inline-flex rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs font-medium tracking-wide text-white/90">
            {company.badge}
          </span>

          <h1 className="font-display mt-6 text-3xl font-bold leading-tight tracking-tight sm:text-4xl lg:text-[2.65rem] lg:leading-[1.15]">
            {company.tagline}
          </h1>

          <p className="mt-5 max-w-xl text-base leading-relaxed text-white/85 sm:text-lg">{company.subtitle}</p>

          <p className="font-mono-accent mt-4 text-xs uppercase tracking-[0.18em] text-white/60">
            Del diseño a la puesta en servicio
          </p>

          <div className="mt-8 flex flex-col gap-3 sm:flex-row sm:flex-wrap">
            <a href={whatsappUrl} target="_blank" rel="noopener noreferrer" className="btn-primary bg-white text-dlci-blue hover:bg-white/90">
              <MessageCircle size={18} aria-hidden />
              Contactar por WhatsApp
            </a>
            <a href={telUrl} className="btn-ghost-light">
              <Phone size={18} aria-hidden />
              Llamar ahora
            </a>
            <a href={company.vcardPath} download className="btn-ghost-light">
              <Download size={18} aria-hidden />
              Guardar contacto
            </a>
          </div>

          <div className="mt-5 flex flex-wrap gap-3">
            <a href="#servicios" className="text-sm font-semibold text-white/90 underline-offset-4 hover:underline">
              Ver servicios
            </a>
            <span className="text-white/30" aria-hidden>
              ·
            </span>
            <a href="#proyectos" className="text-sm font-semibold text-white/90 underline-offset-4 hover:underline">
              Ver proyectos
            </a>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.98 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.7, delay: 0.15 }}
          className="relative"
        >
          <div className="card-premium overflow-hidden border-white/10 bg-white/5 p-2 shadow-2xl backdrop-blur-sm">
            <div className="relative aspect-[4/3] overflow-hidden rounded-[16px]">
              <img
                src={company.assets.hero}
                alt="Proyecto eléctrico DLCI Electricidad"
                className="h-full w-full object-cover"
                width={1200}
                height={675}
                fetchPriority="high"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-dlci-blue/80 via-transparent to-transparent" />
              <div className="absolute bottom-4 left-4 right-4">
                <p className="font-display text-sm font-semibold text-white">Ingeniería eléctrica con calidad, seguridad y eficiencia</p>
              </div>
            </div>
          </div>

          <div className="absolute -bottom-4 -left-2 hidden rounded-2xl border border-white/15 bg-white/10 px-4 py-3 backdrop-blur-md sm:block">
            <p className="text-xs text-white/70">Tarjeta NFC</p>
            <p className="font-display text-sm font-semibold">Contacto instantáneo</p>
          </div>
        </motion.div>
      </div>

      <a
        href="#acciones"
        className="absolute bottom-24 left-1/2 hidden -translate-x-1/2 text-white/50 transition hover:text-white lg:flex lg:bottom-8"
        aria-label="Ir a acciones rápidas"
      >
        <ArrowDown className="animate-bounce" size={22} />
      </a>
    </section>
  )
}
