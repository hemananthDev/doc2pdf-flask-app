pipeline {
    agent any

    environment {
        // Securely pull the PDF.co API key from Jenkins credentials
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
                    # Ensure system is ready
                    sudo apt update
                    
                    # Install pip if not already present
                    sudo apt install -y python3-pip

                    # Upgrade pip and install dependencies
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    # Kill any previously running app
                    pkill -f "python3 app.py" || true

                    # Run the app in background
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
