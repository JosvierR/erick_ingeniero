import { Download, MessageCircle, Phone } from 'lucide-react'
import { company } from '../data/dlci'
import { telUrl, whatsappUrl } from '../lib/links'

export function StickyMobileCTA() {
  return (
    <div
      className="fixed inset-x-0 bottom-0 z-50 border-t border-[#E5E7EB] bg-white/95 px-2 pt-2 pb-[max(0.5rem,env(safe-area-inset-bottom))] backdrop-blur-md md:hidden"
      role="navigation"
      aria-label="Acciones rápidas móvil"
    >
      <div className="mx-auto grid max-w-lg grid-cols-3 gap-2">
        <a
          href={whatsappUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="flex min-h-[3rem] flex-col items-center justify-center gap-1 rounded-xl bg-[#25D366] px-2 py-2.5 text-white"
        >
          <MessageCircle size={20} aria-hidden />
          <span className="text-[11px] font-semibold">WhatsApp</span>
        </a>
        <a
          href={telUrl}
          className="flex min-h-[3rem] flex-col items-center justify-center gap-1 rounded-xl bg-dlci-blue px-2 py-2.5 text-white"
        >
          <Phone size={20} aria-hidden />
          <span className="text-[11px] font-semibold">Llamar</span>
        </a>
        <a
          href={company.vcardPath}
          download
          className="flex min-h-[3rem] flex-col items-center justify-center gap-1 rounded-xl border border-[#E5E7EB] bg-dlci-bg px-2 py-2.5 text-dlci-blue"
        >
          <Download size={20} aria-hidden />
          <span className="text-[11px] font-semibold">Guardar</span>
        </a>
      </div>
    </div>
  )
}
