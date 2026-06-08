import { useState } from 'react'
import SentimentCard from '../components/SentimentCard'

const EXAMPLES = [
  "I love this airline, the staff were so kind and helpful!",
  "Flight delayed 3 hours with zero communication. Absolutely terrible.",
  "The flight was fine, nothing special but got there on time.",
]

export default function Home() {
  const [text, setText] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  async function analyze() {
    if (!text.trim()) return
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/predict`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      })

      if (!res.ok) throw new Error('API error')
      const data = await res.json()
      setResult(data)
    } catch (err) {
      setError('Something went wrong. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
      <div className="bg-white rounded-2xl shadow-md p-8 w-full max-w-lg">
        
        <h1 className="text-2xl font-bold text-gray-800 mb-1">
          Sentiment Analyzer
        </h1>
        <p className="text-gray-400 text-sm mb-6">
          Powered by a Logistic Regression model trained on 14k airline tweets
        </p>

        {/* Example buttons */}
        <div className="flex flex-col gap-2 mb-4">
          {EXAMPLES.map((ex, i) => (
            <button
              key={i}
              onClick={() => setText(ex)}
              className="text-left text-xs text-blue-500 hover:text-blue-700 truncate"
            >
              Try: {ex}
            </button>
          ))}
        </div>

        {/* Text input */}
        <textarea
          className="w-full border border-gray-200 rounded-xl p-4 text-sm text-gray-700 
                     focus:outline-none focus:ring-2 focus:ring-blue-300 resize-none"
          rows={4}
          placeholder="Type or paste text here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        {/* Analyze button */}
        <button
          onClick={analyze}
          disabled={loading}
          className="mt-4 w-full bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300 
                     text-white font-semibold py-3 rounded-xl transition-colors"
        >
          {loading ? 'Analyzing...' : 'Analyze'}
        </button>

        {/* Error state */}
        {error && (
          <p className="mt-4 text-red-400 text-sm text-center">{error}</p>
        )}

        {/* Result card */}
        {result && <SentimentCard result={result} />}

      </div>
    </main>
  )
}