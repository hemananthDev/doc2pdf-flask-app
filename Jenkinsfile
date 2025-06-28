pipeline {
    agent any

    environment {
        PDFCO_API_KEY = credentials('PDFCO_API_KEY')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t doc2pdf-flask-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker stop doc2pdf || true
                    docker rm doc2pdf || true
                    docker run -d --name doc2pdf -p 5000:5000 -e PDFCO_API_KEY=$PDFCO_API_KEY doc2pdf-flask-app
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Dockerized app deployed successfully!'
        }
        failure {
            echo '❌ Dockerized deployment failed.'
        }
    }
}
