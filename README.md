# Water Reminder Telegram Bot

This project is a Telegram bot that helps users stay hydrated by sending them water drinking reminders every 2.5 hours. The bot also tracks each user's daily water intake and resets the counter automatically at midnight.

The application is written in Python and containerized using Docker.  
A CI/CD pipeline is implemented using GitHub Actions to:

- Build the Docker image
- Run the bot container to test it
- Push the image to Docker Hub

> The CI/CD pipeline is triggered automatically **on each push to the `master` branch**.

---

## Technologies Used

- **Python 3**
- **Telegram Bot API** (`pyTelegramBotAPI`)
- **Docker**
- **GitHub Actions** for CI/CD

---

## Docker Hub

The Docker image is published at:  
👉 [https://hub.docker.com/r/your-dockerhub-username/water-reminder-bot](https://hub.docker.com/r/your-dockerhub-username/water-reminder-bot)

> Replace `your-dockerhub-username` with your actual Docker Hub username.
