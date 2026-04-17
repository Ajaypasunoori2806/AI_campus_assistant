# 🎓 AI Campus Assistant

An AI-powered assistant designed for campus environments that can understand and respond to student and staff queries via text, voice, and images.

---

## 🚀 Features

- 💬 Conversational AI chatbot
- 🧠 Context-aware memory (remembers previous messages)
- 🖼️ Image-based query support (OCR ready)
- 📚 Handles:
  - Course information
  - Timetables
  - Events
  - Staff directory
- 🔐 Ready for secure student-specific data (future scope)

## 🏗️ Project Structure

    ai-campus-assistant/
    │
    ├── app/
    │   ├── main.py              # FastAPI entry point
    │   ├── config.py            # Environment config
    │   ├── data/                # Static campus data
    │   │   └── college_data.py
    │   ├── routes/
    │   │   └── chat.py          # API endpoints
    │   ├── services/
    │   │   ├── ai_engine.py     # AI logic
    │   │   ├── ocr.py           # Image text extraction
    │   │   └── memory.py        # Conversation memory
    │   └── models/
    │       └── schemas.py
    │
    ├── tests/
    │   └── test_chat.py
    │
    ├── requirements.txt
    ├── Dockerfile
    ├── docker-compose.yml
    ├── .env
    └── README.md


## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo



### 2️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate



### 3️⃣ Install dependencies

pip install -r requirements.txt


### 4️⃣ Add environment variables

Create a `.env` file:

env
OPENAI_API_KEY=your_api_key_here


##▶️ Run the Application

```bash
uvicorn app.main:app --reload


## 🌐 API Documentation

Once running, open:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI will appear.

---

## 🧪 Example API Request

### POST `/chat`

```json
{
  "user_id": "1",
  "message": "What are today's classes?"
}
```

---

## 🐳 Run with Docker (Optional)

```bash
docker-compose up --build
```

---

## 🛠️ Tech Stack

* ⚡ FastAPI
* 🤖 OpenAI API
* 🧠 Python
* 🐳 Docker
* 🗂️ Modular architecture

---

## 📌 Future Enhancements

* 🎤 Voice input & speech output
* 🗄️ Database integration (PostgreSQL)
* 🔐 Authentication (JWT login)
* 📊 Admin dashboard
* 🌐 Frontend UI (React)

---

## 🤝 Contribution

Feel free to fork this repo and contribute!

---

## 📄 License

This project is for educational and demonstration purposes.

---

## 👨‍💻 Author

**Ajay Kumar Pasunoori**
DevOps Engineer
📧 [pasunoori.a1@gmail.com](mailto:pasunoori.a1@gmail.com)
🔗 [https://github.com/Ajaypasunoori2806](https://github.com/Ajaypasunoori2806)
