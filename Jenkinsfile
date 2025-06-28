pipeline {
    agent any

    environment {
        IMAGE_NAME = "doc2pdf-app"
        CONTAINER_NAME = "doc2pdf-container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/hemananthDev/doc2pdf-flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container (if running)') {
            steps {
                sh 'docker rm -f $CONTAINER_NAME || true'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 \
                    --name $CONTAINER_NAME \
                    -v /usr/bin/soffice:/usr/bin/soffice \
                    -v /usr/lib/libreoffice:/usr/lib/libreoffice \
                    $IMAGE_NAME
                '''
            }
        }
    }

    post {
        failure {
            echo "❌ Build failed."
        }
        success {
            echo "✅ Build and deployment successful!"
        }
    }
}
