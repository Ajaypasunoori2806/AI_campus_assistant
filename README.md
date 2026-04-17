# 🎓 AI Campus Assistant

An AI-powered backend service built using FastAPI and deployed using a complete DevOps pipeline with Docker and CI/CD automation.


## 🧠 Project Objective

This project demonstrates how to:

* Build a backend application
* Containerize using Docker
* Automate deployment using CI/CD
* Deploy to cloud (AWS EC2)

---

## 🏗️ Architecture

```
GitHub → GitHub Actions → AWS EC2 → Docker → FastAPI App
```

---

# ⚙️ 1. Local Development Setup

Clone the repository:

```bash
git clone https://github.com/Ajaypasunoori2806/AI_campus_assistant.git
cd AI_campus_assistant
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
uvicorn app.main:app --reload
```

---

# 🐳 2. Docker Setup

Build Docker image:

```bash
docker build -t ai-campus .
```

Run container:

```bash
docker run -d -p 8000:8000 ai-campus
```

Check running containers:

```bash
docker ps
```

---

# ☁️ 3. AWS EC2 Setup (Manual - One Time)

Connect to EC2:

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

Install Docker:

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

Verify Docker:

```bash
docker --version
```

---

# 🔐 4. GitHub Secrets Setup

In your repo (Settings → Secrets), add:

```
EC2_HOST=your-ec2-ip
EC2_USER=ubuntu
EC2_KEY=your-private-key
```

---

# 🔄 5. CI/CD Pipeline (GitHub Actions)

Pipeline file:

```
.github/workflows/ci.yml
```

### Pipeline Steps:

1. Code pushed to GitHub
2. Build Docker image
3. Save image as `.tar`
4. Copy to EC2 using SCP
5. SSH into EC2
6. Stop old container
7. Run new container

---

# ▶️ 6. Deployment Flow (Automatic)

Push code:

```bash
git add .
git commit -m "update"
git push
```

GitHub Actions will:

* Build Docker image
* Transfer to EC2
* Deploy automatically

---

# 🔍 7. Debugging Commands (VERY IMPORTANT)

Check running containers:

```bash
docker ps -a
```

Check logs:

```bash
docker logs ai-campus
```

Stop container:

```bash
docker stop ai-campus
```

Remove container:

```bash
docker rm ai-campus
```

---

# 📦 Project Structure

```
app/        → Application code  
tests/      → Test cases  
Dockerfile  → Container setup  
ci.yml      → CI/CD pipeline  
```

---

# 🧠 Key DevOps Highlights

* Dockerized FastAPI application
* CI/CD pipeline using GitHub Actions
* Automated deployment to AWS EC2
* SSH-based deployment strategy

---

# 📌 Future Improvements

* Kubernetes deployment
* Terraform automation
* Monitoring (Prometheus, Grafana)

---

# 📞 Contact

GitHub: [https://github.com/Ajaypasunoori2806](https://github.com/Ajaypasunoori2806)

---
