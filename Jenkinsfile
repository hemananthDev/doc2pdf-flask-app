pipeline {
    agent any

    environment {
        PDFCO_API_KEY = "hemananthdev@gmail.com_KYQ2fYiogUb7UHBiYHZ70X6J9B33Abf2S1JXAo2w2sLpRMD7QvDdVoVC9fM5OKvE"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/hemananthDev/doc2pdf-flask-app.git'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup python app.py &'
            }
        }
    }

    post {
        success {
            echo "✅ Deployed with PDF.co integration"
        }
    }
}
