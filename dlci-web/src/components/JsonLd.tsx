import { absoluteAsset, company } from '../data/dlci'

const schema = {
  '@context': 'https://schema.org',
  '@type': 'ProfessionalService',
  name: company.name,
  legalName: company.legalName,
  description: company.subtitle,
  slogan: company.tagline,
  url: company.website,
  telephone: company.office.phone,
  email: [company.office.email, company.representative.email],
  image: absoluteAsset(company.assets.ogImage),
  address: {
    '@type': 'PostalAddress',
    streetAddress: company.streetAddress || company.address,
    addressLocality: 'Santiago de los Caballeros',
    postalCode: company.postalCode || undefined,
    addressCountry: 'DO',
  },
  areaServed: {
    '@type': 'Country',
    name: company.country,
  },
  sameAs: [company.instagram.url, company.facebook.url],
  foundingDate: String(company.founded),
  serviceType: [
    'Diseño eléctrico',
    'Ejecución en baja tensión',
    'Proyectos en media tensión',
    'Supervisión técnica',
  ],
}

export function JsonLd() {
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
    />
  )
}
