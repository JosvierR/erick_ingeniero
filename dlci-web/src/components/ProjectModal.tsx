import { useEffect } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { ArrowRight, Calendar, MapPin, X } from 'lucide-react'
import type { Project } from '../data/dlci'
import { whatsappUrl } from '../lib/links'

type Props = {
  project: Project | null
  onClose: () => void
}

export function ProjectModal({ project, onClose }: Props) {
  useEffect(() => {
    if (!project) return
    const prev = document.body.style.overflow
    document.body.style.overflow = 'hidden'
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose()
    }
    window.addEventListener('keydown', onKey)
    return () => {
      document.body.style.overflow = prev
      window.removeEventListener('keydown', onKey)
    }
  }, [project, onClose])

  return (
    <AnimatePresence>
      {project && (
        <motion.div
          className="fixed inset-0 z-[100] flex items-end justify-center sm:items-center sm:p-6"
          role="dialog"
          aria-modal="true"
          aria-labelledby="project-modal-title"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.22 }}
        >
          <motion.button
            type="button"
            className="absolute inset-0 bg-[#1a1f2e]/55 backdrop-blur-[6px]"
            aria-label="Cerrar"
            onClick={onClose}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          />

          <motion.div
            className="project-modal-panel relative z-10 flex max-h-[92dvh] w-full flex-col overflow-hidden rounded-t-[28px] bg-white shadow-[0_-8px_60px_rgba(26,31,46,0.18)] sm:max-h-[88vh] sm:max-w-2xl sm:rounded-[28px]"
            initial={{ y: '100%', opacity: 0.9 }}
            animate={{ y: 0, opacity: 1 }}
            exit={{ y: '100%', opacity: 0.9 }}
            transition={{ type: 'spring', damping: 32, stiffness: 340 }}
          >
            <div className="relative aspect-[16/10] shrink-0 overflow-hidden bg-dlci-bg sm:aspect-[16/9]">
              <img
                src={project.image}
                alt={project.name}
                className="h-full w-full object-cover"
                width={1200}
                height={675}
              />
              <div className="absolute inset-0 bg-gradient-to-t from-[#1a1f2e]/85 via-[#1a1f2e]/15 to-transparent" />

              <button
                type="button"
                onClick={onClose}
                className="absolute right-4 top-4 flex h-10 w-10 items-center justify-center rounded-full bg-white/95 text-dlci-dark shadow-md transition hover:bg-white"
                aria-label="Cerrar proyecto"
              >
                <X size={20} />
              </button>

              {project.years && (
                <span className="absolute left-4 top-4 inline-flex items-center gap-1.5 rounded-full bg-white/95 px-3 py-1.5 text-xs font-semibold text-dlci-blue shadow-sm">
                  <Calendar size={13} aria-hidden />
                  {project.years}
                </span>
              )}

              <div className="absolute bottom-0 left-0 right-0 p-5 sm:p-6">
                <p className="font-mono-accent text-[10px] uppercase tracking-[0.22em] text-white/65">Proyecto DLCI</p>
                <h2 id="project-modal-title" className="font-display mt-1 text-2xl font-bold text-white sm:text-3xl">
                  {project.name}
                </h2>
              </div>
            </div>

            <div className="flex-1 overflow-y-auto overscroll-contain px-5 py-6 sm:px-8 sm:py-7">
              <div className="flex flex-wrap gap-4 text-sm text-dlci-dark/80">
                <p className="inline-flex items-center gap-2">
                  <MapPin size={16} className="shrink-0 text-dlci-accent" aria-hidden />
                  {project.location}
                </p>
                {project.details && (
                  <p className="w-full text-xs font-medium uppercase tracking-[0.12em] text-dlci-dark/50">
                    {project.details}
                  </p>
                )}
              </div>

              <p className="mt-5 text-base leading-relaxed text-dlci-dark/85">{project.description}</p>

              <div className="mt-6 rounded-2xl border border-[#E8ECF1] bg-dlci-bg/80 p-5">
                <p className="font-display text-xs font-semibold uppercase tracking-wider text-dlci-blue">
                  Alcance del trabajo
                </p>
                <p className="mt-2 text-sm leading-relaxed text-dlci-dark/80">{project.scope}</p>
              </div>

              <div className="mt-6">
                <p className="font-display text-xs font-semibold uppercase tracking-wider text-dlci-blue">
                  Servicios realizados
                </p>
                <ul className="mt-3 flex flex-wrap gap-2">
                  {project.services.map((service) => (
                    <li
                      key={service}
                      className="rounded-full border border-dlci-blue/15 bg-white px-3.5 py-1.5 text-xs font-medium text-dlci-blue shadow-[0_1px_0_rgba(49,61,94,0.06)]"
                    >
                      {service}
                    </li>
                  ))}
                </ul>
              </div>

              <a
                href={whatsappUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="btn-primary mt-8 w-full sm:w-auto"
              >
                Consultar proyecto similar
                <ArrowRight size={18} aria-hidden />
              </a>
            </div>

            <div className="hidden h-1 w-12 shrink-0 self-center rounded-full bg-dlci-dark/15 sm:mb-2 sm:block" aria-hidden />
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
