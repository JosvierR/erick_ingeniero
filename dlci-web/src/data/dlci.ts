import contact from './contact.json'

/** URL pública del sitio (Netlify: variable VITE_SITE_URL). Ver .env.example */
export const siteUrl = (import.meta.env.VITE_SITE_URL as string | undefined)?.replace(/\/$/, '') ?? ''

export const company = {
  name: 'DLCI Electricidad',
  legalName: 'DLCI Electricidad SRL',
  tagline: 'Sus proyectos eléctricos, en las mejores manos',
  badge: 'Ingeniería eléctrica en República Dominicana',
  subtitle:
    'Diseño, gestión, supervisión y ejecución de proyectos eléctricos para construcción, comercio e industria.',
  founded: 2008,
  foundedPlace: 'Santiago de los Caballeros',
  experienceYears: 15,
  country: 'República Dominicana',
  office: contact.office,
  representative: contact.representative,
  phone: contact.representative.phone,
  phoneDisplay: contact.representative.phoneDisplay,
  email: contact.office.email,
  website: contact.website,
  address: contact.address,
  streetAddress: contact.streetAddress,
  postalCode: contact.postalCode,
  mapsUrl: contact.mapsUrl,
  whatsappMessage: contact.whatsappMessage,
  instagram: contact.instagram,
  facebook: contact.facebook,
  vcardPath: '/dlci-contact.vcf',
  assets: {
    logo: '/dlci/logo-transparent.png',
    logoLight: '/dlci/logo-light.png',
    logoOriginal: '/dlci/logo-original.png',
    hero: '/dlci/hero-project.jpg',
    heroBackground: '/dlci/hero-bg.jpg',
    ogImage: '/dlci/hero-project.jpg',
  },
} as const

/** Imagen OG absoluta cuando VITE_SITE_URL está configurada en Netlify */
export function absoluteAsset(path: string) {
  if (!siteUrl) return path
  return `${siteUrl}${path.startsWith('/') ? path : `/${path}`}`
}

export const aboutText =
  'DLCI Electricidad es una empresa especializada en ingeniería eléctrica, dedicada al diseño y ejecución de proyectos del sector construcción, comercial e industrial. Con más de 15 años de trayectoria, la empresa se ha caracterizado por su compromiso, responsabilidad, calidad y entrega ante sus clientes en toda la República Dominicana.'

export const timeline = [
  { year: '2008', label: 'Fundación en Santiago de los Caballeros' },
  { year: '+15 años', label: 'De experiencia en ingeniería eléctrica' },
  { year: 'Multisector', label: 'Proyectos residenciales, comerciales e industriales' },
  { year: 'Confianza', label: 'Crecimiento basado en calidad, seguridad y confianza' },
] as const

export const stats = [
  { value: '+15', label: 'Años en el mercado' },
  { value: '+88', label: 'Proyectos construcción' },
  { value: '+22', label: 'Proyectos industriales' },
  { value: 'MT/BT', label: 'Media y baja tensión' },
  { value: 'RD', label: 'Cobertura nacional' },
  { value: '100%', label: 'Cumplimiento normativo' },
] as const

export const services = [
  {
    id: 'diseno',
    title: 'Diseño eléctrico',
    description: 'Ingeniería integral para instalaciones seguras y eficientes.',
    icon: 'blueprint',
    scope: [
      'Diseño en baja y media tensión',
      'Cálculo y dimensionamiento de cargas',
      'Diagramas unifilares y tableros',
      'Iluminación interior/exterior',
      'Puesta a tierra y protección contra sobretensiones',
    ],
  },
  {
    id: 'gestion',
    title: 'Gestión y aprobación de planos',
    description: 'Tramitación y coordinación con entidades reguladoras.',
    icon: 'clipboard',
    scope: ['Edenorte', 'Edesur', 'Edeeste', 'MIVED', 'CODIA Regional Norte'],
  },
  {
    id: 'baja',
    title: 'Ejecución en baja tensión',
    description: 'Instalación certificada para comercio, industria y vivienda.',
    icon: 'zap',
    scope: [
      'Canalización EMT/PVC',
      'Cableado certificado',
      'Tableros y protecciones',
      'Iluminación comercial e industrial',
      'Generadores y transferencia automática',
      'Mallas de puesta a tierra',
    ],
  },
  {
    id: 'media',
    title: 'Proyectos en media tensión',
    description: 'Soluciones de distribución y medición de alto estándar.',
    icon: 'factory',
    scope: [
      'Transformadores',
      'Celdas y equipos de media tensión',
      'Módulos de medición y transferencia',
      'Conductores especializados',
      'Coordinación de energización',
      'Pruebas y puesta en servicio',
    ],
  },
  {
    id: 'supervision',
    title: 'Supervisión y dirección técnica',
    description: 'Control de calidad y cumplimiento en obra.',
    icon: 'hard-hat',
    scope: [
      'Supervisión especializada en obra',
      'Control de calidad',
      'Coordinación multidisciplinaria',
      'Seguimiento de cronograma',
      'Verificación de planos y especificaciones',
    ],
  },
  {
    id: 'suministro',
    title: 'Suministro e instalación de equipos',
    description: 'Equipos eléctricos seleccionados e instalados por personal calificado.',
    icon: 'package',
    scope: [
      'Tableros y protecciones',
      'Equipos de medición',
      'Iluminación técnica',
      'Sistemas de respaldo',
      'Puesta en servicio',
    ],
  },
] as const

export const processSteps = [
  { step: 1, title: 'Diagnóstico técnico', description: 'Evaluación de necesidades, cargas y condiciones del proyecto.' },
  { step: 2, title: 'Diseño y planificación', description: 'Ingeniería detallada, planos y especificaciones técnicas.' },
  { step: 3, title: 'Gestión de aprobaciones', description: 'Coordinación con distribuidoras y entidades reguladoras.' },
  { step: 4, title: 'Ejecución / instalación', description: 'Montaje certificado según normativa vigente.' },
  { step: 5, title: 'Supervisión y control', description: 'Seguimiento de calidad, plazos y especificaciones.' },
  { step: 6, title: 'Puesta en servicio', description: 'Pruebas, energización y entrega documentada.' },
] as const

export const projects = [
  {
    id: 'torre-soria',
    name: 'Torre Soria',
    location: 'Santiago de los Caballeros, Villa Olga',
    years: '2021–2023',
    details: '14 niveles · Apartamentos 132 m² – 200 m²',
    description:
      'Proyecto residencial de gran escala con diseño e instalaciones eléctricas completas.',
    scope:
      'Ingeniería eléctrica integral para torre de 14 niveles: dimensionamiento de cargas, tableros por zona, iluminación de áreas comunes y apartamentos, más supervisión en obra hasta la puesta en servicio.',
    services: ['Diseño eléctrico', 'Ejecución', 'Supervisión', 'Instalaciones eléctricas'],
    image: '/dlci/projects/torre-soria.jpg',
  },
  {
    id: 'biventi-iii',
    name: 'Biventi III',
    location: 'Santiago de los Caballeros, Villa Olga',
    years: '2021–2023',
    details: '10 niveles · Apartamentos 140 m² – 175 m²',
    description: 'Complejo residencial con infraestructura eléctrica de alta densidad.',
    scope:
      'Diseño y ejecución de sistemas en baja tensión para edificio de 10 niveles, incluyendo canalizaciones, protecciones, iluminación y coordinación con otras disciplinas en obra.',
    services: ['Diseño eléctrico', 'Ejecución', 'Supervisión', 'Instalaciones eléctricas'],
    image: '/dlci/projects/biventi-iii.jpg',
  },
  {
    id: 'residencial-sorrento',
    name: 'Residencial Sorrento',
    location: 'Santiago de los Caballeros, Villa Olga',
    years: '2019–2022',
    details: 'Dos edificios de 6 niveles · 24 apartamentos · 118 m² – 136 m²',
    description: 'Desarrollo residencial con dos torres y sistemas eléctricos integrados.',
    scope:
      'Dos edificios de 6 niveles con 24 unidades: planificación eléctrica unificada, aprobaciones y montaje de instalaciones con control de calidad en ambas torres.',
    services: ['Diseño eléctrico', 'Ejecución', 'Supervisión', 'Instalaciones eléctricas'],
    image: '/dlci/projects/residencial-sorrento.jpg',
  },
  {
    id: 'torre-bonsai',
    name: 'Torre Bonsai',
    location: 'Santiago de los Caballeros, Cerros de Gurabo III',
    years: '2019–2021',
    details: '11 niveles · Un apartamento por nivel · 114 m²',
    description: 'Torre residencial con instalaciones eléctricas de precisión por nivel.',
    scope:
      'Torre de 11 niveles con un apartamento por piso: diseño detallado por nivel, tableros individuales y supervisión técnica durante la ejecución.',
    services: ['Diseño eléctrico', 'Ejecución', 'Supervisión', 'Instalaciones eléctricas'],
    image: '/dlci/projects/torre-bonsai.jpg',
  },
  {
    id: 'torre-murcia',
    name: 'Torre Murcia',
    location: 'Santiago de los Caballeros, La Esmeralda',
    years: '2020–2021',
    details: '10 niveles · Apartamentos 80 m² – 108 m²',
    description: 'Proyecto vertical con optimización de cargas y tableros por zona.',
    scope:
      'Edificio de 10 niveles en La Esmeralda: optimización de cargas, distribución por zonas y entrega de instalaciones certificadas con documentación de cierre.',
    services: ['Diseño eléctrico', 'Ejecución', 'Supervisión', 'Instalaciones eléctricas'],
    image: '/dlci/projects/torre-murcia.jpg',
  },
  {
    id: 'residencial-dj',
    name: 'Residencial DJ',
    location: 'Santiago de los Caballeros',
    years: '',
    details: 'Proyecto residencial',
    description: 'Desarrollo residencial con soluciones eléctricas integrales DLCI.',
    scope:
      'Acompañamiento eléctrico completo en desarrollo residencial: desde el diseño y tramitación hasta la ejecución y verificación final de instalaciones.',
    services: ['Diseño eléctrico', 'Ejecución', 'Supervisión', 'Instalaciones eléctricas'],
    image: '/dlci/projects/residencial-dj.jpg',
  },
] as const

export type Project = (typeof projects)[number]

export const clients = [
  'Constructora Colón & Genao',
  'Ingeniería Infante Curiel',
  'JRI Inversiones',
  'Ingeniería Infante Pichardo',
  'Constructora Ortefil',
  'Ingeniería Colizma',
  'Zona Franca Santiago',
] as const

export const providers = [
  'Ferretería 8A',
  'Ferretería Bellón',
  'Ilumeyco',
  'Montan y Asociados',
] as const

export const missionVision = {
  mission:
    'Ofrecer soluciones de ingeniería eléctrica con calidad, seguridad y eficiencia para el sector construcción e industrial.',
  vision:
    'Ser una empresa líder en ingeniería eléctrica en República Dominicana, reconocida por su excelencia e innovación.',
  values: [
    'Responsabilidad',
    'Calidad',
    'Seguridad',
    'Integridad',
    'Innovación',
    'Trabajo en equipo',
    'Compromiso con el cliente',
  ],
} as const

export const navLinks = [
  { href: '#inicio', label: 'Inicio' },
  { href: '#nosotros', label: 'Nosotros' },
  { href: '#servicios', label: 'Servicios' },
  { href: '#proyectos', label: 'Proyectos' },
  { href: '#contacto', label: 'Contacto' },
] as const

export const projectTypes = [
  'Residencial',
  'Comercial',
  'Industrial',
  'Media tensión',
  'Otro',
] as const
