# DOC2PDF Flask App

A lightweight web application that allows users to upload DOC/DOCX files and convert them to PDF format using LibreOffice.

## Features

- Upload `.doc` or `.docx` files via a clean web interface
- Converts to PDF using LibreOffice backend
- Instant download of converted PDF
- Dockerized for portability
- CI/CD pipeline via Jenkins

## Tech Stack

- Python 3.11
- Flask
- LibreOffice (CLI mode)
- Docker
- Jenkins
- GitHub Webhooks

## Getting Started (Local)

1. Clone the repository  
   `git clone https://github.com/hemananthDev/doc2pdf-flask-app.git`

2. Install requirements  
   `pip install -r requirements.txt`

3. Run the app  
   `python app.py`

## Docker

```bash
docker build -t doc2pdf-flask-app .
docker run -p 5000:5000 doc2pdf-flask-app
