pipeline {
    agent any

    environment {
        // Reference a secret in Jenkins credentials instead of hardcoding
        PDFCO_API_KEY = credentials('PDFCO_API_KEY')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/hemananthDev/doc2pdf-flask-app.git'
            }
        }

        stage('Install Requirements') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    nohup python3 app.py > flask.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployed with PDF.co integration"
        }
        failure {
            echo "❌ Deployment failed"
        }
    }
}
