import { readFileSync, writeFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'

const root = join(dirname(fileURLToPath(import.meta.url)), '..')
const contact = JSON.parse(readFileSync(join(root, 'src/data/contact.json'), 'utf8'))

const vcard = `BEGIN:VCARD
VERSION:3.0
FN:DLCI Electricidad
ORG:DLCI Electricidad SRL
TITLE:Ingeniería eléctrica
TEL;TYPE=WORK,VOICE:${contact.office.phone}
EMAIL;TYPE=WORK:${contact.office.email}
EMAIL;TYPE=INTERNET:${contact.representative.email}
URL:${contact.website}
ADR:;;${contact.streetAddress || contact.address};;;;
NOTE:${contact.representative.name} · WhatsApp ${contact.office.phoneDisplay}
X-SOCIALPROFILE;type=instagram:${contact.instagram.url}
X-SOCIALPROFILE;type=facebook:${contact.facebook.url}
END:VCARD
`

writeFileSync(join(root, 'public/dlci-contact.vcf'), vcard, 'utf8')
console.log('✓ public/dlci-contact.vcf generado desde src/data/contact.json')
