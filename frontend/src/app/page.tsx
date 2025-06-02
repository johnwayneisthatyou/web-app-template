'use client'

import { useEffect, useState } from 'react'
import Image from "next/image";

export default function Home() {
  const [apiStatus, setApiStatus] = useState<string>('Loading...')

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/health`)
      .then(res => res.json())
      .then(data => setApiStatus(data.status))
      .catch(err => setApiStatus('Error: ' + err.message))
  }, [])

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-8">Web App Template</h1>
      <div className="border rounded-lg p-4">
        <p>Backend API Status: <span className="font-mono">{apiStatus}</span></p>
      </div>
    </main>
  )
}
