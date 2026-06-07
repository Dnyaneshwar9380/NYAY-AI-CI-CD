# ⚖️ Nyay AI - End-to-End CI/CD Deployment

Nyay AI is an AI-powered Indian Legal Assistant that provides legal guidance, explains IPC sections, summarizes landmark judgments, and answers law-related queries through a simple web interface.

This project demonstrates a complete DevOps workflow using GitHub Actions, Docker, Docker Hub, and AWS EC2 for automated deployment.

---

## 🚀 Features

- AI-powered legal assistance
- Interactive web interface
- Dockerized application
- Automated CI/CD pipeline
- Docker Hub integration
- AWS EC2 deployment
- GitHub Actions automation

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### AI Integration
- Groq API

### DevOps
- Docker
- Docker Hub
- GitHub Actions
- AWS EC2

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
NYAY-AI-CI-CD
│
├── .github/
│   └── workflows/
│       └── cicd.yml
│
├── templates/
├── screenshots/
│
├── Dockerfile
├── app.py
├── requirements.txt
├── Questions.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ CI/CD Workflow

The CI/CD pipeline is triggered automatically whenever code is pushed to GitHub.

### Pipeline Stages

1. Continuous Integration
   - Checkout source code
   - Install dependencies
   - Validate application

2. Build & Push Docker Image
   - Build Docker image
   - Push image to Docker Hub

3. Deploy to AWS EC2
   - Connect to EC2 using SSH
   - Pull latest Docker image
   - Stop old container
   - Deploy updated container


## 📈 CI/CD Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Continuous Integration
    ├── Build Docker Image
    ├── Push to Docker Hub
    │
    ▼
Docker Hub
    │
    ▼
AWS EC2
    │
    ▼
Docker Container
    │
    ▼
Nyay AI Application
```


## 🎯 Project Highlights

- End-to-End CI/CD Pipeline
- Dockerized Deployment
- Automated GitHub Actions Workflow
- AWS EC2 Hosting
- Docker Hub Integration
- AI-Powered Legal Assistant
- Production-Ready DevOps Workflow

---

## 👨‍💻 Author

**Dnyaneshwar Mirgude**

AWS | Docker | GitHub Actions | Python | Linux  |  DevOps

---

## 📄 License

This project is licensed under the Apache 2.0 License.
