import { company } from '../data/dlci'

const toDigits = (phone: string) => phone.replace(/\D/g, '')

export const whatsappUrl = `https://wa.me/${toDigits(company.representative.phone)}?text=${encodeURIComponent(company.whatsappMessage)}`

export const telOfficeUrl = `tel:${company.office.phone}`

export const telMobileUrl = `tel:${company.representative.phone}`

/** Llamada principal: oficina */
export const telUrl = telOfficeUrl

export const mailtoOfficeUrl = `mailto:${company.office.email}?subject=${encodeURIComponent('Consulta proyecto eléctrico - DLCI')}`

export const mailtoRepresentativeUrl = `mailto:${company.representative.email}?subject=${encodeURIComponent('Consulta proyecto eléctrico - DLCI')}`

export const mailtoUrl = mailtoOfficeUrl
