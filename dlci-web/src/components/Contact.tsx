import { useEffect, useState, type FormEvent } from 'react'
import { motion } from 'framer-motion'
import {
  CheckCircle2,
  Download,
  Loader2,
  Mail,
  MapPin,
  MessageCircle,
  Phone,
  Send,
  User,
} from 'lucide-react'
import { company, projectTypes } from '../data/dlci'
import {
  mailtoOfficeUrl,
  mailtoRepresentativeUrl,
  telMobileUrl,
  telOfficeUrl,
  whatsappUrl,
} from '../lib/links'
import { SectionHeading } from './SectionHeading'

const NETLIFY_FORM_NAME = 'dlci-contacto'

type FormStatus = 'idle' | 'sending' | 'success' | 'error'

export function Contact() {
  const [status, setStatus] = useState<FormStatus>('idle')

  useEffect(() => {
    const params = new URLSearchParams(window.location.search)
    if (params.get('contacto') === 'enviado') {
      setStatus('success')
      window.history.replaceState({}, '', `${window.location.pathname}#contacto`)
    }
  }, [])

  const submitToNetlify = async (form: HTMLFormElement) => {
    const fd = new FormData(form)
    const body = new URLSearchParams()
    body.append('form-name', NETLIFY_FORM_NAME)
    fd.forEach((value, key) => {
      if (key !== 'form-name') body.append(key, String(value))
    })

    const res = await fetch('/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: body.toString(),
    })
    return res.ok
  }

  const fallbackMailto = (form: HTMLFormElement) => {
    const fd = new FormData(form)
    const body = [
      `Nombre: ${fd.get('nombre')}`,
      fd.get('empresa') ? `Empresa: ${fd.get('empresa')}` : '',
      `Teléfono: ${fd.get('telefono')}`,
      `Tipo de proyecto: ${fd.get('tipo')}`,
      '',
      String(fd.get('mensaje') ?? ''),
    ]
      .filter(Boolean)
      .join('\n')

    window.location.href = `mailto:${company.office.email}?subject=${encodeURIComponent('Solicitud web - Proyecto eléctrico')}&body=${encodeURIComponent(body)}`
  }

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const form = e.currentTarget
    setStatus('sending')

    try {
      const ok = await submitToNetlify(form)
      if (ok) {
        form.reset()
        setStatus('success')
        return
      }
    } catch {
      /* Netlify no disponible en local */
    }

    setStatus('error')
    fallbackMailto(form)
  }

  return (
    <section id="contacto" className="section-pad bg-dlci-blue text-white">
      <div className="mx-auto max-w-6xl">
        <SectionHeading
          light
          eyebrow="Contacto"
          title="¿Tienes un proyecto eléctrico en desarrollo?"
          subtitle="DLCI Electricidad puede acompañarte desde el diseño y aprobación hasta la ejecución, supervisión y puesta en servicio."
        />

        <div className="mb-10 grid gap-4 sm:grid-cols-2">
          <motion.div
            initial={{ opacity: 0, y: 12 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="contact-card"
          >
            <p className="font-mono-accent text-[10px] uppercase tracking-[0.2em] text-white/50">
              {company.office.label}
            </p>
            <div className="mt-4 space-y-3">
              <a href={telOfficeUrl} className="contact-card-link">
                <Phone size={18} aria-hidden />
                <span>
                  <span className="block text-xs text-white/55">Teléfono</span>
                  <span className="font-semibold">{company.office.phoneDisplay}</span>
                </span>
              </a>
              <a href={mailtoOfficeUrl} className="contact-card-link">
                <Mail size={18} aria-hidden />
                <span>
                  <span className="block text-xs text-white/55">Correo</span>
                  <span className="font-semibold">{company.office.email}</span>
                </span>
              </a>
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 12 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.06 }}
            className="contact-card contact-card--highlight"
          >
            <p className="font-mono-accent text-[10px] uppercase tracking-[0.2em] text-white/50">
              {company.representative.name}
            </p>
            <div className="mt-4 space-y-3">
              <a href={telMobileUrl} className="contact-card-link">
                <Phone size={18} aria-hidden />
                <span>
                  <span className="block text-xs text-white/55">Celular</span>
                  <span className="font-semibold">{company.representative.phoneDisplay}</span>
                </span>
              </a>
              <a href={mailtoRepresentativeUrl} className="contact-card-link">
                <Mail size={18} aria-hidden />
                <span>
                  <span className="block text-xs text-white/55">Correo</span>
                  <span className="font-semibold">{company.representative.email}</span>
                </span>
              </a>
            </div>
          </motion.div>
        </div>

        <div className="mb-8 flex flex-wrap justify-center gap-2.5 sm:gap-3">
          <a
            href={whatsappUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="btn-primary bg-[#25D366] text-white hover:bg-[#20bd5a]"
          >
            <MessageCircle size={18} aria-hidden />
            WhatsApp
          </a>
          <a href={telOfficeUrl} className="btn-ghost-light">
            <Phone size={18} aria-hidden />
            Oficina
          </a>
          <a href={telMobileUrl} className="btn-ghost-light">
            <User size={18} aria-hidden />
            Ing. Máximo
          </a>
          <a href={company.mapsUrl} target="_blank" rel="noopener noreferrer" className="btn-ghost-light">
            <MapPin size={18} aria-hidden />
            Ubicación
          </a>
          <a href={company.vcardPath} download className="btn-ghost-light">
            <Download size={18} aria-hidden />
            Guardar contacto
          </a>
        </div>

        <motion.form
          name={NETLIFY_FORM_NAME}
          method="POST"
          data-netlify="true"
          data-netlify-honeypot="bot-field"
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          onSubmit={handleSubmit}
          className="contact-form mx-auto max-w-xl"
        >
          <input type="hidden" name="form-name" value={NETLIFY_FORM_NAME} />

          <p className="hidden" aria-hidden>
            <label>
              No completar: <input name="bot-field" tabIndex={-1} autoComplete="off" />
            </label>
          </p>

          <p className="mb-6 text-center text-sm text-white/75">
            Envíenos su consulta. Le responderemos desde{' '}
            <strong className="text-white">{company.office.email}</strong>.
          </p>

          <div className="grid gap-4 sm:grid-cols-2">
            <label className="block sm:col-span-1">
              <span className="mb-1.5 block text-xs font-medium text-white/80">Nombre *</span>
              <input
                name="nombre"
                required
                disabled={status === 'sending'}
                className="contact-input"
                placeholder="Su nombre"
              />
            </label>
            <label className="block sm:col-span-1">
              <span className="mb-1.5 block text-xs font-medium text-white/80">Empresa</span>
              <input
                name="empresa"
                disabled={status === 'sending'}
                className="contact-input"
                placeholder="Nombre de empresa"
              />
            </label>
            <label className="block sm:col-span-1">
              <span className="mb-1.5 block text-xs font-medium text-white/80">Teléfono *</span>
              <input
                name="telefono"
                type="tel"
                required
                disabled={status === 'sending'}
                className="contact-input"
                placeholder={company.office.phoneDisplay}
              />
            </label>
            <label className="block sm:col-span-1">
              <span className="mb-1.5 block text-xs font-medium text-white/80">Tipo de proyecto *</span>
              <select
                name="tipo"
                required
                disabled={status === 'sending'}
                className="contact-input"
                defaultValue=""
              >
                <option value="" disabled>
                  Seleccionar
                </option>
                {projectTypes.map((t) => (
                  <option key={t} value={t}>
                    {t}
                  </option>
                ))}
              </select>
            </label>
            <label className="block sm:col-span-2">
              <span className="mb-1.5 block text-xs font-medium text-white/80">Mensaje *</span>
              <textarea
                name="mensaje"
                required
                rows={4}
                disabled={status === 'sending'}
                className="contact-input resize-y"
                placeholder="Cuéntenos sobre su proyecto..."
              />
            </label>
          </div>

          <button
            type="submit"
            disabled={status === 'sending' || status === 'success'}
            className="btn-primary mt-6 w-full bg-white text-dlci-blue hover:bg-white/90 disabled:cursor-not-allowed disabled:opacity-70"
          >
            {status === 'sending' ? (
              <>
                <Loader2 size={18} className="animate-spin" aria-hidden />
                Enviando…
              </>
            ) : status === 'success' ? (
              <>
                <CheckCircle2 size={18} aria-hidden />
                Mensaje enviado
              </>
            ) : (
              <>
                <Send size={18} aria-hidden />
                Solicitar contacto
              </>
            )}
          </button>

          {status === 'success' && (
            <p className="mt-4 text-center text-sm text-white/85" role="status">
              Gracias. Hemos recibido su solicitud y le contactaremos pronto.
            </p>
          )}

          {status === 'error' && (
            <p className="mt-4 text-center text-sm text-white/70" role="status">
              No se pudo enviar al servidor. Se abrió su correo como alternativa.
            </p>
          )}

          <p className="mt-4 text-center text-[11px] text-white/45">
            Formulario seguro vía Netlify. En desarrollo local puede usar correo alternativo.
          </p>
        </motion.form>
      </div>
    </section>
  )
}
