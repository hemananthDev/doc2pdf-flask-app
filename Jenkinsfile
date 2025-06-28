pipeline {
    agent any

    environment {
        APP_DIR = "/home/ec2-user/doc2pdf-flask-app"
        FLASK_PORT = "5000"
    }

    stages {
        stage('Clone Latest Code') {
            steps {
                sh '''
                    if [ -d "$APP_DIR" ]; then
                        rm -rf $APP_DIR
                    fi
                    git clone https://github.com/hemananthDev/doc2pdf-flask-app.git $APP_DIR
                '''
            }
        }

        stage('Clean Old Files') {
            steps {
                sh '''
                    find $APP_DIR/uploads/ -type f \\( -name "*.doc" -o -name "*.docx" -o -name "*.pdf" \\) -delete || true
                '''
            }
        }

        stage('Kill Running App') {
            steps {
                sh '''
                    pkill -f "python app.py" || true
                '''
            }
        }

        stage('Install Requirements') {
            steps {
                sh '''
                    pip install -r $APP_DIR/requirements.txt
                '''
            }
        }

        stage('Start Flask App') {
            steps {
                sh '''
                    nohup python $APP_DIR/app.py > $APP_DIR/flask.log 2>&1 &
                '''
            }
        }
    }

    post {
        failure {
            echo "❌ Build failed."
        }
        success {
            echo "✅ App deployed successfully without Docker."
        }
    }
}
