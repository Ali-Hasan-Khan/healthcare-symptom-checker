import { useState } from "react";
import { checkSymptoms } from "./services/api";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";

function App() {
  const [symptoms, setSymptoms] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleCheck = async () => {
    if (!symptoms.trim()) return;
    setLoading(true);
    const response = await checkSymptoms(symptoms);
    setResult(response);
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-background px-4">
      <div className="bg-card border border-border shadow-lg rounded-lg p-8 max-w-screen-lg">
        <div className="flex gap-4">
          <div className="">
            <h1 className="text-2xl font-bold mb-4 text-center text-foreground">
              Healthcare Symptom Checker
            </h1>

            <Textarea
              value={symptoms}
              onChange={(e) => setSymptoms(e.target.value)}
              placeholder="Describe your symptoms..."
              rows={4}
            ></Textarea>

            <Button
              variant="secondary"
              onClick={handleCheck}
              disabled={loading}
              className="mt-4 w-full py-2 rounded-md transition-colors duration-200"
            >
              {loading ? "Analyzing..." : "Check Symptoms"}
            </Button>
          </div>

          {result && (
            <div className="mt-6 bg-muted border border-border rounded-lg p-4">
              <h2 className="font-semibold mb-2 text-foreground">Results:</h2>
              <p className="text-muted-foreground whitespace-pre-wrap">
                {result}
              </p>
            </div>
          )}
        </div>
        <div>
          <p className="text-xs text-muted-foreground mt-4 text-center">
            This tool is for educational purposes only and not a substitute for
            professional medical advice.
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;
