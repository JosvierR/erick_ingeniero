import { About } from './components/About'
import { Clients } from './components/Clients'
import { Contact } from './components/Contact'
import { Footer } from './components/Footer'
import { Hero } from './components/Hero'
import { JsonLd } from './components/JsonLd'
import { SeoHead } from './components/SeoHead'
import { MissionVision } from './components/MissionVision'
import { Navbar } from './components/Navbar'
import { Process } from './components/Process'
import { Projects } from './components/Projects'
import { QuickActions } from './components/QuickActions'
import { Services } from './components/Services'
import { Stats } from './components/Stats'
import { StickyMobileCTA } from './components/StickyMobileCTA'

function App() {
  return (
    <>
      <JsonLd />
      <SeoHead />
      <Navbar />
      <main className="pb-20 md:pb-0">
        <Hero />
        <QuickActions />
        <About />
        <Stats />
        <Services />
        <Process />
        <Projects />
        <Clients />
        <MissionVision />
        <Contact />
      </main>
      <Footer />
      <StickyMobileCTA />
    </>
  )
}

export default App
