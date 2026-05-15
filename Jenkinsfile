pipeline {
    agent any

    environment {
        IMAGE          = 'zxckartoplya52/car-factory-api'
        CONTAINER_NAME = 'car-factory'
        SERVER         = 'root@45.90.216.186'
    }

    stages {

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest tests/ -v
                '''
            }
        }

        stage('Build & Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker buildx build --platform linux/amd64 -t $IMAGE --push .'
                }
            }
        }

        stage('Deploy') {
            steps {
                sshagent(credentials: ['server-ssh']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${SERVER} '
                            docker stop ${CONTAINER_NAME} || true
                            docker rm ${CONTAINER_NAME} || true
                            docker pull ${IMAGE}
                            docker run -d -p 8000:8000 --name ${CONTAINER_NAME} ${IMAGE}
                        '
                    """
                }
            }
        }
    }

    post {
        success { echo 'Pipeline выполнен успешно' }
        failure { echo 'Pipeline завершился с ошибкой' }
    }
}
