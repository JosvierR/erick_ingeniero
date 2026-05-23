import { useCallback, useState } from 'react'
import { motion } from 'framer-motion'
import { ArrowUpRight, MapPin } from 'lucide-react'
import {
  activeProjects,
  assetUrl,
  moreProjects,
  recentProjects,
  type Project,
} from '../data/dlci'
import { ProjectModal } from './ProjectModal'
import { SectionHeading } from './SectionHeading'

type ProjectGridProps = {
  items: readonly Project[]
  offset?: number
  onOpen: (project: Project) => void
}

function ProjectGrid({ items, offset = 0, onOpen }: ProjectGridProps) {
  return (
    <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3 lg:gap-7">
      {items.map((project, i) => (
        <motion.article
          key={project.id}
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-50px' }}
          transition={{ delay: ((offset + i) % 3) * 0.05 }}
        >
          <button
            type="button"
            onClick={() => onOpen(project)}
            className="project-card group w-full touch-manipulation text-left active:scale-[0.995]"
            aria-label={`Ver proyecto ${project.name}`}
          >
            <div className="relative aspect-[16/9] overflow-hidden bg-[#e8ecf1]">
              <img
                src={assetUrl(project.image)}
                alt={`${project.name} — ${project.location}`}
                loading="lazy"
                decoding="async"
                className="h-full w-full object-cover transition duration-700 ease-out group-hover:scale-[1.04]"
                width={1200}
                height={900}
              />
              <div className="absolute inset-0 bg-gradient-to-t from-[#252b3d]/90 via-[#252b3d]/20 to-transparent opacity-90 transition group-hover:opacity-95" />

              <div className="absolute right-3 top-3 flex flex-col items-end gap-1.5">
                {'badge' in project && project.badge && (
                  <span className="rounded-full border border-white/20 bg-dlci-accent/95 px-3 py-1 text-[10px] font-semibold uppercase tracking-wide text-white backdrop-blur-sm">
                    {project.badge}
                  </span>
                )}
                {project.years && (
                  <span className="rounded-full border border-white/20 bg-white/95 px-3 py-1 text-[11px] font-semibold tracking-wide text-dlci-blue backdrop-blur-sm">
                    {project.years}
                  </span>
                )}
              </div>

              <div className="absolute bottom-0 left-0 right-0 p-4 sm:p-5">
                <h3 className="font-display text-lg font-bold leading-tight text-white sm:text-xl">
                  {project.name}
                </h3>
                <p className="mt-1 flex items-center gap-1 text-xs text-white/75">
                  <MapPin size={12} aria-hidden />
                  <span className="line-clamp-1">{project.location}</span>
                </p>
              </div>
            </div>

            <div className="p-5">
              {project.details && (
                <p className="text-[11px] font-medium uppercase tracking-[0.14em] text-dlci-dark/45">
                  {project.details}
                </p>
              )}
              <p className="mt-2 line-clamp-2 text-sm leading-relaxed text-dlci-dark/72">
                {project.description}
              </p>

              <div className="mt-4 flex flex-wrap gap-1.5">
                {project.services.slice(0, 3).map((s) => (
                  <span key={s} className="service-chip">
                    {s}
                  </span>
                ))}
                {project.services.length > 3 && (
                  <span className="service-chip service-chip--muted">+{project.services.length - 3}</span>
                )}
              </div>

              <span className="project-card-cta">
                Ver proyecto
                <ArrowUpRight
                  size={15}
                  className="transition group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
                  aria-hidden
                />
              </span>
            </div>
          </button>
        </motion.article>
      ))}
    </div>
  )
}

export function Projects() {
  const [activeProject, setActiveProject] = useState<Project | null>(null)

  const openProject = useCallback((project: Project) => {
    setActiveProject(project)
  }, [])

  const closeProject = useCallback(() => {
    setActiveProject(null)
  }, [])

  return (
    <section id="proyectos" className="section-pad bg-white">
      <div className="mx-auto max-w-6xl">
        <SectionHeading
          eyebrow="Proyectos"
          title="Proyectos recientes"
          subtitle="Toque un proyecto para ver ubicación, alcance y servicios ejecutados."
        />

        <ProjectGrid items={recentProjects} onOpen={openProject} />

        {moreProjects.length > 0 && (
          <div className="mt-14">
            <h3 className="mb-6 font-display text-xl font-bold text-dlci-blue sm:text-2xl">
              Más proyectos
            </h3>
            <ProjectGrid
              items={moreProjects}
              offset={recentProjects.length}
              onOpen={openProject}
            />
          </div>
        )}

        {activeProjects.length > 0 && (
          <div className="mt-14">
            <h3 className="mb-6 font-display text-xl font-bold text-dlci-blue sm:text-2xl">
              En ejecución
            </h3>
            <ProjectGrid
              items={activeProjects}
              offset={recentProjects.length + moreProjects.length}
              onOpen={openProject}
            />
          </div>
        )}
      </div>

      <ProjectModal project={activeProject} onClose={closeProject} />
    </section>
  )
}
