import { useState } from "react";
import { checkSymptoms } from "./services/api";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import ReactMarkdown from "react-markdown";
import { Send, Bot, RotateCcw } from "lucide-react";

function App() {
  const [symptoms, setSymptoms] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!symptoms.trim()) return;

    setLoading(true);

    try {
      const response = await checkSymptoms(symptoms);
      setResult(response);
    } catch (error) {
      setResult("Sorry, I couldn't process your request. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  const handleNewQuery = () => {
    setSymptoms("");
    setResult("");
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-background flex flex-col">
      {/* Header */}
      <div className="border-b border-border bg-card px-4 py-3">
        <h1 className="text-xl font-semibold text-foreground flex items-center gap-2">
          <Bot className="w-6 h-6 text-primary" />
          Healthcare Symptom Checker
        </h1>
        <p className="text-sm text-muted-foreground mt-1">
          Describe your symptoms and get educational health information
        </p>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-y-auto p-4 max-w-4xl mx-auto w-full">
        {/* Welcome State - Centered */}
        {!result && !loading && (
          <div className="flex flex-col items-center justify-center min-h-[calc(100vh-200px)]">
            <div className="text-center text-muted-foreground mb-8">
              <Bot className="w-12 h-12 mx-auto mb-4 text-muted-foreground/50" />
              <h2 className="text-lg font-medium mb-2">
                Welcome to Healthcare Symptom Checker
              </h2>
              <p className="text-sm mb-4">
                Describe your symptoms below and I'll provide educational
                information about possible conditions.
              </p>
            </div>

            {/* Centered Input Form */}
            <div className="w-full max-w-2xl">
              <form onSubmit={handleSubmit} className="flex gap-2">
                <div className="flex-1">
                  <Textarea
                    value={symptoms}
                    onChange={(e) => setSymptoms(e.target.value)}
                    onKeyPress={handleKeyPress}
                    placeholder="Describe your symptoms in detail..."
                    className="min-h-[80px] max-h-40 resize-none focus:outline-none focus:ring-0 focus:ring-offset-0 focus:border-input focus-visible:ring-0 focus-visible:ring-offset-0"
                  />
                </div>
                <Button
                  type="submit"
                  disabled={!symptoms.trim()}
                  className="h-[80px] px-6 flex-shrink-0 gap-2"
                >
                  <Send className="w-4 h-4" />
                  Analyze
                </Button>
              </form>
            </div>
          </div>
        )}

        {/* Loading State */}
        {loading && (
          <div className="space-y-6 mt-8">
            {/* User Query Display */}
            <div className="bg-muted/50 rounded-lg p-4">
              <h3 className="font-medium mb-2">Your Symptoms:</h3>
              <p className="text-sm text-muted-foreground whitespace-pre-wrap">
                {symptoms}
              </p>
            </div>

            {/* Loading Animation */}
            <div className="bg-card border rounded-lg p-6">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center">
                  <Bot className="w-4 h-4 text-primary" />
                </div>
                <span className="font-medium">Analyzing your symptoms...</span>
              </div>
              <div className="flex items-center gap-2 text-sm text-muted-foreground">
                <div className="flex space-x-1">
                  <div className="w-2 h-2 bg-primary/60 rounded-full animate-bounce [animation-delay:-0.3s]"></div>
                  <div className="w-2 h-2 bg-primary/60 rounded-full animate-bounce [animation-delay:-0.15s]"></div>
                  <div className="w-2 h-2 bg-primary/60 rounded-full animate-bounce"></div>
                </div>
                This may take a few seconds...
              </div>
            </div>
          </div>
        )}

        {/* Result State */}
        {result && !loading && (
          <div className="space-y-6 mt-8">
            {/* User Query Display */}
            <div className="bg-muted/50 rounded-lg p-4">
              <h3 className="font-medium mb-2">Your Symptoms:</h3>
              <p className="text-sm text-muted-foreground whitespace-pre-wrap">
                {symptoms}
              </p>
            </div>

            {/* Bot Response */}
            <div className="bg-card border rounded-lg p-6">
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center">
                    <Bot className="w-4 h-4 text-primary" />
                  </div>
                  <span className="font-medium">Health Information</span>
                </div>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={handleNewQuery}
                  className="gap-2"
                >
                  <RotateCcw className="w-4 h-4" />
                  New Query
                </Button>
              </div>

              <div className="prose prose-sm dark:prose-invert max-w-none">
                <ReactMarkdown
                  components={{
                    p: ({ children }) => (
                      <p className="mb-3 last:mb-0 leading-relaxed">
                        {children}
                      </p>
                    ),
                    strong: ({ children }) => (
                      <strong className="font-semibold text-foreground">
                        {children}
                      </strong>
                    ),
                    ul: ({ children }) => (
                      <ul className="list-disc list-inside mb-3 space-y-1">
                        {children}
                      </ul>
                    ),
                    li: ({ children }) => (
                      <li className="text-sm">{children}</li>
                    ),
                    h1: ({ children }) => (
                      <h1 className="text-lg font-semibold mt-4 mb-2 first:mt-0">
                        {children}
                      </h1>
                    ),
                    h2: ({ children }) => (
                      <h2 className="text-base font-semibold mt-4 mb-2 first:mt-0">
                        {children}
                      </h2>
                    ),
                  }}
                >
                  {result}
                </ReactMarkdown>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Footer */}
      <div className="border-t border-border bg-card px-4 py-3">
        <p className="text-xs text-muted-foreground text-center">
          This tool is for educational purposes only and not a substitute for
          professional medical advice.
        </p>
      </div>
    </div>
  );
}

export default App;
