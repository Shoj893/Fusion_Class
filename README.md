# 🚀 FusionClass – AI-Powered Smart Attendance System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white">
  <img src="https://img.shields.io/badge/AI-Face%20%26%20Voice%20Recognition-blue?style=for-the-badge">
</p>

<p align="center">
<b>FusionClass</b> is an intelligent attendance management platform that automates classroom attendance using <b>Face Recognition</b> and <b>Voice Recognition</b>. It provides a seamless experience for teachers and students while reducing manual effort, preventing proxy attendance, and maintaining secure attendance records.
</p>

---

# ✨ Key Highlights

- 🤖 AI-powered attendance using **Face Recognition**
- 🎙️ Voice Recognition as an alternative attendance method
- 👨‍🏫 Dedicated Teacher Dashboard
- 🎓 Dedicated Student Dashboard
- 📱 QR Code based classroom joining
- 🔐 Secure Authentication
- ☁️ Cloud Database using Supabase
- 📊 Attendance History & Reports
- ⚡ Fast and accurate recognition using Machine Learning

---

# 📸 System Overview

```
Teacher
   │
   ├── Create Subject
   ├── Share QR Code / Join Code
   │
Students
   │
   ├── Register Face
   ├── Register Voice
   └── Join Subject
        │
        ▼
AI Recognition Engine
(Face + Voice)
        │
        ▼
Attendance Verification
        │
        ▼
Supabase Database
        │
        ▼
Attendance Dashboard
```

---

# 🚀 Features

## 👨‍🏫 Teacher Module

- Secure Login & Authentication
- Create and Manage Subjects
- Generate Join Codes
- Share QR Codes for instant enrollment
- Take Attendance using:
  - 📷 Face Recognition
  - 🎤 Voice Recognition
- View Attendance History
- Track Student Attendance
- Manage Classroom Records

---

## 🎓 Student Module

- Student Login
- Join Subjects via Join Code
- Register Face Embeddings
- Register Voice Embeddings
- View Attendance History
- Track Attendance Percentage

---

## 🤖 AI Attendance Engine

### Face Recognition

- Face Detection using **dlib**
- 128-Dimensional Face Embeddings
- SVM-based Classification
- Fast Face Matching
- Multiple Face Detection

### Voice Recognition

- Speaker Embeddings using **Resemblyzer**
- Audio Feature Extraction
- Cosine Similarity Matching
- High-quality Speaker Verification

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Database | Supabase |
| Authentication | bcrypt |
| Face Recognition | dlib, face_recognition_models |
| Voice Recognition | Resemblyzer, Librosa |
| Machine Learning | scikit-learn |
| Image Processing | Pillow |
| Data Processing | NumPy, Pandas |
| QR Code Generation | Segno |

---

# 📂 Project Structure

```
FusionClass/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   │
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   └── ui/
│
├── public/
│
└── .streamlit/
```

---

# 📋 Database Tables

The project uses the following tables:

```
teachers

students

subjects

subject_students

attendance_logs
```

---

# 🧠 How Face Recognition Works

1. Student registers their face.
2. Face embedding is generated.
3. Embeddings are stored securely.
4. During attendance:
   - Face detected
   - Embedding extracted
   - Compared with stored embeddings
5. Attendance is marked automatically.

---

# 🎤 How Voice Recognition Works

1. Student records a voice sample.
2. Voice embeddings are generated.
3. Embeddings are stored.
4. During attendance:
   - Voice captured
   - Speaker embedding extracted
   - Cosine similarity used for matching
5. Attendance recorded.

---

# 🔄 Workflow

```
Teacher Login
      │
Create Subject
      │
Generate QR Code
      │
Students Join
      │
Register Face & Voice
      │
Teacher Starts Attendance
      │
AI Recognition
      │
Attendance Saved
      │
Dashboard Updated
```

---

# 🎯 Advantages

✅ Saves classroom time

✅ Eliminates manual attendance

✅ Reduces proxy attendance

✅ Secure biometric verification

✅ Easy classroom management

✅ Cloud-based storage

✅ Fast attendance processing

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates further development and helps others discover the project.

---

# 👨‍💻 Author

**Shobhit Jaiswal**

AI • Machine Learning • Python • Data Science

GitHub: **[https://github.com/ShobhitJaiswal](https://github.com/Shoj893))**

LinkedIn: **[https://linkedin.com/in/ShobhitJaiswal](https://www.linkedin.com/in/shobhitjaiswal2607/)**

---

<p align="center">
<b>FusionClass</b><br>
Making Attendance Smarter with Artificial Intelligence 🚀
</p>
