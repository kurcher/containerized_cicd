💧 Water Reminder Telegram Bot

A simple Telegram bot that reminds users to drink water every 2.5 hours and tracks their daily water intake.  
The project is containerized using Docker and uses GitHub Actions for CI/CD automation.

---

 🚀 Features

- ⏰ Sends a reminder every 2.5 hours
- 💬 Allows users to input how much water they’ve drunk
- 📊 Displays daily progress with `/progress`
- 🔄 Resets tracking at midnight every day

---

 🧾 Project Structure

water-reminder-bot/
├── app/
│ └── main.py # Telegram bot logic
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image build instructions
├── .github/
│ └── workflows/
│ └── ci-cd.yml # GitHub Actions CI/CD workflow
└── README.md


---

## 🐳 Running the Bot with Docker

### 1. Build the Docker image

bash:
docker build -t water-bot .
2. Run the container:
docker run -d \
  -e BOT_TOKEN=your_telegram_bot_token \
  water-bot
🔁 CI/CD with GitHub Actions
The project includes a GitHub Actions workflow (.github/workflows/ci-cd.yml) that performs the following on every push to main:

🧱 Build the Docker image

🔐 Authenticate with Docker Hub

☁️ Push the image to Docker Hub

🧪 Optionally run the image (test deployment)

⚠️ GitHub Actions is not suitable for permanent hosting.
Use a VPS or a cloud service for production deployment.

🔐 GitHub Secrets Required
Set the following repository secrets under
Settings → Secrets and variables → Actions:

Secret Name	Description
BOT_TOKEN	Your Telegram bot token
DOCKER_USERNAME	Your Docker Hub username
DOCKER_PASSWORD	Your Docker Hub password or token

⚙️ Example GitHub Actions Workflow:
name: CI/CD for Telegram Bot

on:
  push:
    branches: [ master ]

jobs:
  build-push-run:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Log in to Docker Hub
      run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

    - name: Build Docker image
      run: docker build -t ${{ secrets.DOCKER_USERNAME }}/water-reminder-bot:latest .

    - name: Push Docker image
      run: docker push ${{ secrets.DOCKER_USERNAME }}/water-reminder-bot:latest
🚀 Deploying to a Server (VPS)
To run the bot permanently, use a VPS or cloud instance and:

Clone this repo

Set up Docker and docker-compose

Start the bot in detached mode

(Optional) Use systemd or similar to auto-restart on reboot

📦 Docker Hub Image
You can pull the published image from Docker Hub:

docker pull your_dockerhub_username/water-reminder-bot:latest
📬 Contact

Docker Hub: https://hub.docker.com/u/kurch1k

