# 🎯 AI Attendance System

An AI-powered Attendance Management System built using Python, Streamlit, DeepFace, OpenCV, TensorFlow, and Supabase for real-time face recognition and automated attendance tracking. The system enables secure student authentication, intelligent attendance marking, and seamless database management with a modern interactive UI. Successfully deployed on Render with cloud-based hosting and integrated AI-driven facial recognition capabilities.

🌐 Live Demo:
https://ai-attendance-system-fxhl.onrender.com

## 🚀 Features

- Real-Time Face Recognition
- Teacher & Student Authentication
- AI-Based Attendance Tracking
- Voice Embedding Support
- Supabase Cloud Database Integration
- Modern Streamlit UI
- Persistent Attendance Logs


## 🛠️ Tech Stack

- Python
- Streamlit
- DeepFace
- OpenCV
- Scikit-learn
- Supabase
- NumPy
- Pandas
- Librosa


## ⚙️ Installation

```bash
git clone https://github.com/your-username/AI_Attendance.git

cd AI_Attendance

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```


## ☁️ Supabase Setup

Create `.streamlit/secrets.toml`

```toml
SUPABASE_URL = "YOUR_SUPABASE_URL"

SUPABASE_KEY = "YOUR_SUPABASE_KEY"
```

## ▶️ Run Project

```bash
streamlit run app.py
```


## 🔒 Security

- API keys secured using `.gitignore`
- Cloud database integration with Supabase
