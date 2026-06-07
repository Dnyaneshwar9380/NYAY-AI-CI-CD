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

---

## 🐳 Docker Commands

### Build Image

```bash
docker build -t nyay-ai .
```

### Run Container

```bash
docker run -p 5000:5000 nyay-ai
```

### Push Image

```bash
docker push dnyaneshwar9380/nyay-ai-cicd:latest
```

---

## ☁️ AWS EC2 Deployment

### Security Group Configuration

| Port | Purpose |
|------|----------|
| 22 | SSH |
| 80 | HTTP |
| 5000 | Application |

### Deployment Process

```bash
docker pull dnyaneshwar9380/nyay-ai-cicd:latest

docker stop nyay-ai || true
docker rm nyay-ai || true

docker run -d \
-p 5000:5000 \
--name nyay-ai \
dnyaneshwar9380/nyay-ai-cicd:latest
```

---

## 🔐 GitHub Secrets

Configure the following secrets in:

Repository → Settings → Secrets and Variables → Actions

| Secret Name | Description |
|------------|-------------|
| DOCKER_USERNAME | Docker Hub Username |
| DOCKER_PASSWORD | Docker Hub Access Token |
| EC2_HOST | EC2 Public IP |
| EC2_USERNAME | EC2 User |
| EC2_SSH_KEY | Private SSH Key |
| GROQ_API_KEY | Groq API Key |

---

## 🖥️ Local Setup

### Clone Repository

```bash
git clone https://github.com/Dnyaneshwar9380/NYAY-AI-CI-CD.git

cd NYAY-AI-CI-CD
```

### Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
python app.py
```

Open in browser:

```text
http://localhost:5000
```

---

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

---

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

AWS | Docker | GitHub Actions | Python | Linux | Devops 

---

## 📄 License

This project is licensed under the Apache 2.0 License.
