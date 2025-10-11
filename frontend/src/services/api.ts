import axios from "axios";

const API_URL =
  import.meta.env.VITE_API_URL || "http://localhost:8000/api/check";

export const checkSymptoms = async (symptoms: string): Promise<string> => {
  try {
    const response = await axios.post(API_URL, { symptoms });
    console.log("response:", response.data);
    return response.data.result;
  } catch (error: any) {
    console.error("Error calling API:", error);
    return "Sorry, something went wrong while checking your symptoms.";
  }
};
