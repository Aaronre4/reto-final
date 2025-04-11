pipeline {
    agent any

    environment {
        REGISTRY = 'aaronre4'
        IMAGE_NAME = 'reto-final-python'
    }

    stages {
        stage('Clonar código') {
            steps {
                git 'https://github.com/Aaronre4/reto-final.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 app || true'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aaronre4/reto-final-python:latest .'
            }
        }

        stage('Push to Registry') {
            when {
                branch 'main'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $REGISTRY/$IMAGE_NAME:latest
                    '''
                }
            }
        }
    }
}
