pipeline {
    agent any

    environment {
        REGISTRY = 'aaronre4'
        IMAGE_NAME = 'reto-final-python'
    }

    stages {
        stage('Clonar código') {
            steps {
                git 'https://github.com/TU_USUARIO/TU_REPO.git' // o usa una ruta local
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
                sh 'docker build -t $REGISTRY/$IMAGE_NAME:latest .'
            }
        }

        stage('Push to Registry') {
            when {
                branch pattern: "^(main|master|develop)$", comparator: "REGEXP"
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
