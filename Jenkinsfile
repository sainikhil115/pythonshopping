pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/shopping-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t shopping-app:latest .'
            }
        }

        stage('Push Image') {
            steps {
                sh '''
                docker tag shopping-app:latest yourdockerhub/shopping-app:latest
                docker push yourdockerhub/shopping-app:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
