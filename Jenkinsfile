pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sainikhil115/pythonshopping.git'
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
                docker tag shopping-app:latest nikhilsimha112/shopping-app-app:latest
                docker push nikhilsimha112/shopping-app:tagname
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
