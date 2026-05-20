import { useCallback, useState } from 'react'
import { motion } from 'framer-motion'
import { ArrowUpRight, MapPin } from 'lucide-react'
import { projects, type Project } from '../data/dlci'
import { ProjectModal } from './ProjectModal'
import { SectionHeading } from './SectionHeading'

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
          title="Experiencia en obras reales"
          subtitle="Toque un proyecto para ver ubicación, alcance y servicios ejecutados."
        />

        <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3 lg:gap-6">
          {projects.map((project, i) => (
            <motion.article
              key={project.id}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '-50px' }}
              transition={{ delay: (i % 3) * 0.05 }}
            >
              <button
                type="button"
                onClick={() => openProject(project)}
                className="project-card group w-full text-left"
                aria-label={`Ver proyecto ${project.name}`}
              >
                <div className="relative aspect-[5/4] overflow-hidden bg-[#e8ecf1]">
                  <img
                    src={project.image}
                    alt=""
                    loading="lazy"
                    decoding="async"
                    className="h-full w-full object-cover transition duration-700 ease-out group-hover:scale-[1.04]"
                    width={1080}
                    height={1080}
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#252b3d]/90 via-[#252b3d]/20 to-transparent opacity-90 transition group-hover:opacity-95" />

                  {project.years && (
                    <span className="absolute right-3 top-3 rounded-full border border-white/20 bg-white/95 px-3 py-1 text-[11px] font-semibold tracking-wide text-dlci-blue backdrop-blur-sm">
                      {project.years}
                    </span>
                  )}

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
                    <ArrowUpRight size={15} className="transition group-hover:translate-x-0.5 group-hover:-translate-y-0.5" aria-hidden />
                  </span>
                </div>
              </button>
            </motion.article>
          ))}
        </div>
      </div>

      <ProjectModal project={activeProject} onClose={closeProject} />
    </section>
  )
}
