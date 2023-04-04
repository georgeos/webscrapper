import { Inter } from 'next/font/google'
import Scrape from '../components/Scrape'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Scrape></Scrape>
    </>
  )
}
