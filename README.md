# 🤖 Lumina AI | The Intelligent Study Companion
> **Demo Day Project: A Modern Full-Stack AI Tutoring System**

Lumina AI is a specialized tutoring platform designed to provide instant, academic-focused guidance. Built with a robust **Python REST API**, a structured **SQL backend**, and a sleek **Glassmorphism UI**, Lumina demonstrates the power of integrating logic, data, and design.

---

## 🚀 Key Features
- **🧠 Context-Aware Tutoring:** A Python logic engine that processes student queries.
- **🗄️ Persistent Memory:** Every interaction is logged into a structured SQL database for history tracking.
- **⚡ Real-time Communication:** REST API architecture for seamless frontend-to-backend data flow.
- **🎨 Modern UI:** A responsive, intuitive chat interface built with pure CSS and Vanilla JS.

---

## 🛠️ The Tech Stack
| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend** | `HTML5`, `CSS3`, `JavaScript` | User Interface & API Fetching |
| **Backend** | `Python`, `Flask` | REST API Development & Logic |
| **Database** | `SQLite3` | Relational Data Storage (Users & Chats) |
| **Protocol** | `REST / JSON` | Communication Bridge |

---

## 📂 Project Architecture
```text
ai-tutor-project/
│
├── backend/
│   ├── app.py               # Flask REST API Server
│   ├── database.py          # SQL Schema & Initialization
│   ├── tutor.db             # SQLite Database (Auto-generated)
│   └── requirements.txt     # Dependency List
│
├── frontend/
│   ├── index.html           # Main Application UI
│   ├── style.css            # Custom Styling & Animations
│   └── script.js            # Frontend Logic & API Integration
│
└── README.md                # Project Documentation