# MoodBasedSongProject

🎧 Mood-Based Song Recommender (Azure Full-Stack Project)
Overview

The Mood-Based Song Recommender is a full-stack web application that suggests songs based on a user’s selected mood. When the user clicks on a mood (e.g., Happy, Sad, Chill), the app fetches matching songs from a cloud database and displays them instantly — each song linking directly to its YouTube video.

This project demonstrates how to integrate Azure Static Web Apps, Azure Functions, and Azure Cosmos DB into one cohesive serverless architecture.

🔧 Tech Stack

Frontend: HTML, CSS, JavaScript (hosted on Azure Static Web Apps)

Backend: Python (Azure Functions)

Database: Azure Cosmos DB (NoSQL JSON documents)

Cloud Platform: Microsoft Azure

Deployment & CI/CD: GitHub + Azure Static Web Apps Actions

💡 Features

🎭 Users can select a mood, and the app dynamically retrieves matching songs.

🎵 Each song includes a title, artist, genre, and a clickable YouTube link.

⚡ Fully serverless architecture—no traditional servers to manage.

🔐 Secure backend connection using environment variables and Function App configuration.

🔄 Automatic GitHub Actions deployment for both frontend and backend.
