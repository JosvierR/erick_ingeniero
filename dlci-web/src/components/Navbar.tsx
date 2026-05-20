import { useEffect, useState } from 'react'
import { Menu, X } from 'lucide-react'
import { navLinks } from '../data/dlci'
import { Logo } from './Logo'

export function Navbar() {
  const [open, setOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 48)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  const onHero = !scrolled

  return (
    <header
      className={`fixed inset-x-0 top-0 z-50 transition-all duration-300 ${
        onHero
          ? 'bg-gradient-to-b from-[#1a2236]/95 via-[#1a2236]/70 to-transparent'
          : 'border-b border-[#E8ECF1] bg-white/98 shadow-[0_1px_0_rgba(49,61,94,0.06)] backdrop-blur-md'
      }`}
    >
      <nav className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3.5 sm:px-6 lg:px-8">
        <a href="#inicio" className="shrink-0" aria-label="DLCI Electricidad inicio">
          <Logo variant={onHero ? 'light' : 'dark'} />
        </a>

        <ul className="hidden items-center gap-0.5 md:flex">
          {navLinks.map((link) => (
            <li key={link.href}>
              <a
                href={link.href}
                className={
                  onHero
                    ? 'rounded-lg px-3.5 py-2 text-[13px] font-medium tracking-wide text-white/92 transition hover:bg-white/10 hover:text-white'
                    : 'rounded-lg px-3.5 py-2 text-[13px] font-medium text-dlci-dark/80 transition hover:bg-[#f0f2f6] hover:text-dlci-blue'
                }
              >
                {link.label}
              </a>
            </li>
          ))}
        </ul>

        <button
          type="button"
          className={`inline-flex rounded-lg p-2 md:hidden ${onHero ? 'text-white' : 'text-dlci-blue'}`}
          aria-label={open ? 'Cerrar menú' : 'Abrir menú'}
          aria-expanded={open}
          onClick={() => setOpen(!open)}
        >
          {open ? <X size={22} /> : <Menu size={22} />}
        </button>
      </nav>

      {open && (
        <div
          className={`border-t px-4 py-4 md:hidden ${
            onHero ? 'border-white/12 bg-[#1a2236]/98 backdrop-blur-xl' : 'border-[#E8ECF1] bg-white'
          }`}
        >
          <ul className="flex flex-col gap-0.5">
            {navLinks.map((link) => (
              <li key={link.href}>
                <a
                  href={link.href}
                  className={
                    onHero
                      ? 'block rounded-lg px-3 py-2.5 text-sm font-medium text-white/92 hover:bg-white/10'
                      : 'block rounded-lg px-3 py-2.5 text-sm font-medium text-dlci-dark hover:bg-[#f0f2f6]'
                  }
                  onClick={() => setOpen(false)}
                >
                  {link.label}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </header>
  )
}
