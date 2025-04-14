pipeline {
    agent any

    environment {
        REGISTRY = 'aaronre4'
        IMAGE_NAME = 'reto-final-python'
    }
    
    stages {
        stage('Clonar código') {
            steps {
                checkout scm
            }
        }

        stage('Mostrar rama') {
            steps {
                sh 'git branch -a'
                sh 'echo "Rama actual: $(git rev-parse --abbrev-ref HEAD)"'
            }
        }
        
        stage('Instalar flake8') {
            steps {
                sh 'pip install flake8'
            }
        }

        stage('Instalar pytest') {
            steps {
                sh 'pip install pytest'
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
                        docker push aaronre4/reto-final-python:latest
                    '''
                }
            }
        }
    }
}
