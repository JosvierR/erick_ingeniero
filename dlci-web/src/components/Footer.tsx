import { company, navLinks } from '../data/dlci'
import { Logo } from './Logo'

export function Footer() {
  const year = new Date().getFullYear()

  return (
    <footer className="border-t border-[#E5E7EB] bg-white">
      <div className="mx-auto max-w-6xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="flex flex-col gap-8 md:flex-row md:items-start md:justify-between">
          <div className="max-w-sm">
            <Logo variant="dark" className="!h-10" />
            <p className="font-mono-accent mt-3 text-xs uppercase tracking-widest text-dlci-accent">{company.tagline}</p>
            <p className="mt-4 text-sm text-dlci-dark/70">{company.address}</p>
            <p className="mt-2 text-sm text-dlci-dark/70">
              Oficina:{' '}
              <a href={`tel:${company.office.phone}`} className="text-dlci-blue hover:underline">
                {company.office.phoneDisplay}
              </a>
              {' · '}
              <a href={`mailto:${company.office.email}`} className="text-dlci-blue hover:underline">
                {company.office.email}
              </a>
            </p>
            <div className="mt-4 flex flex-col gap-1 text-sm">
              <a href={company.instagram.url} target="_blank" rel="noopener noreferrer" className="text-dlci-blue hover:underline">
                Instagram: {company.instagram.handle}
              </a>
              <a href={company.facebook.url} target="_blank" rel="noopener noreferrer" className="text-dlci-blue hover:underline">
                Facebook: {company.facebook.name}
              </a>
            </div>
          </div>

          <nav aria-label="Enlaces rápidos">
            <p className="font-display text-sm font-semibold text-dlci-blue">Enlaces</p>
            <ul className="mt-3 space-y-2">
              {navLinks.map((link) => (
                <li key={link.href}>
                  <a href={link.href} className="text-sm text-dlci-dark/75 transition hover:text-dlci-blue">
                    {link.label}
                  </a>
                </li>
              ))}
            </ul>
          </nav>
        </div>

        <div className="mt-10 border-t border-[#E5E7EB] pt-6 text-center text-xs text-dlci-dark/55">
          © {year} {company.legalName}. Todos los derechos reservados.
        </div>
      </div>
    </footer>
  )
}
