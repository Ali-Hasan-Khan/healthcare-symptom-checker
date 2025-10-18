# Healthcare Symptom Checker

A modern symptom checker application that helps users explore possible conditions based on reported symptoms. This project features a FastAPI backend with LLM integration and a React frontend.

## Features

- **AI-Powered Analysis**: Uses OpenRouter API with GPT models for intelligent symptom analysis
- **Responsive UI**: Modern React frontend with Tailwind CSS and shadcn/ui components
- **Database Logging**: SQLite database for query history and analytics
- **Health Monitoring**: Built-in health check endpoints for deployment monitoring
- **Educational Focus**: Designed for learning and prototyping (not medical advice)

## Directory Structure

```
healthcare-symptom-checker/
├── backend/           # FastAPI server and LLM integration
│   ├── app/
│   │   ├── main.py           # FastAPI application
│   │   ├── llm_service.py    # OpenRouter/OpenAI integration
│   │   ├── database.py       # SQLite database operations
│   │   └── config.py         # Environment configuration
│   ├── requirements.txt      # Python dependencies
│   └── README.md            # Backend documentation
├── frontend/          # React application
│   ├── src/
│   │   ├── App.tsx          # Main application component
│   │   ├── services/api.ts  # API communication (streaming)
│   │   └── components/      # UI components
│   ├── package.json         # Node.js dependencies
│   └── README.md           # Frontend documentation
└── README.md         # Project overview
```

## Tech Stack

### Backend

- **FastAPI** - Modern Python web framework
- **OpenRouter API** - LLM integration (GPT-3.5-turbo)
- **SQLite** - Lightweight database for logging
- **Uvicorn** - ASGI server
- **Python 3.8+** - Runtime environment

### Frontend

- **React 18** - UI framework
- **TypeScript** - Type-safe JavaScript
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **shadcn/ui** - Modern UI component library
- **React Markdown** - Markdown rendering
- **Lucide React** - Icon library

## Prerequisites

- **Python 3.8+**
- **Node.js 16+**
- **npm or yarn**
- **OpenRouter API Key** (get from [openrouter.ai](https://openrouter.ai))

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Ali-Hasan-Khan/healthcare-symptom-checker.git
cd healthcare-symptom-checker
```

### 2. Setup Backend

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Create .env file with your API credentials
echo "OPENROUTER_API_KEY=your_api_key_here" > .env
echo "OPENROUTER_BASE_URL=https://openrouter.ai/api/v1" >> .env

# Initialize database
python -c "from app.database import init_db; init_db()"

# Start the FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: `http://localhost:8000`

### 3. Setup Frontend

```bash
# Open new terminal and navigate to frontend
cd frontend

# Install Node.js dependencies
npm install

# Create .env file for API URL
echo "VITE_API_URL=http://localhost:8000/api/check" > .env

# Start the development server
npm run dev
```

Frontend will be available at: `http://localhost:5173`

## API Endpoints

- `POST /api/check` - Analyze symptoms 
- `GET /health` - Health check endpoint
- `GET /api/history` - Query history (admin)
- `GET /docs` - Interactive API documentation

## Important Disclaimers

- **This is for educational purposes only**
- **Not a substitute for professional medical advice**
- **Always consult healthcare providers for medical concerns**
- **Do not use for emergency situations**
