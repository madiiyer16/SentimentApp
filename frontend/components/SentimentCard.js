export default function SentimentCard({ result }) {
  const config = {
    positive: { emoji: "😊", color: "text-green-500", bg: "bg-green-50", border: "border-green-200" },
    negative: { emoji: "😞", color: "text-red-500", bg: "bg-red-50", border: "border-red-200" },
    neutral:  { emoji: "😐", color: "text-gray-500", bg: "bg-gray-50", border: "border-gray-200" },
  }

  const { emoji, color, bg, border } = config[result.sentiment]

  return (
    <div className={`mt-6 p-6 rounded-xl border ${bg} ${border} animate-fade-in`}>
      <div className="flex items-center gap-3 mb-3">
        <span className="text-4xl">{emoji}</span>
        <span className={`text-2xl font-bold capitalize ${color}`}>
          {result.sentiment}
        </span>
      </div>
      <p className="text-gray-500 text-sm">
        {Math.round(result.confidence * 100)}% confident
      </p>
      <p className="text-gray-400 text-xs mt-2 italic">
        "{result.input_text}"
      </p>
    </div>
  )
}