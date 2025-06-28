pipeline {
    agent any

    environment {
        PDFCO_API_KEY = credentials('PDFCO_API_KEY')
    }

    stages {
        stage('Cleanup Old Docker Stuff') {
            steps {
                sh '''
                    echo "🧹 Stopping and removing existing containers..."
                    docker ps -aq | xargs -r docker stop || true
                    docker ps -aq | xargs -r docker rm || true

                    echo "🧼 Removing old images (doc2pdf-flask-app)..."
                    docker images -q doc2pdf-flask-app | xargs -r docker rmi -f || true

                    echo "✅ Cleanup complete"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t doc2pdf-flask-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
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
