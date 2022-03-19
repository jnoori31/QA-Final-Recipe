pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDS = credentials("DOCKER_HUB_CREDS")
        DATABASE_URI = credentials("DATABASE_URI")
    }
    stages {
        stage('Setup') {
            steps {
                sh "echo setup"
            }
        }
        stage('Test') {
            steps {
                sh "echo test"
            }
        }
        stage('Build') {
            steps {
                sh "echo test"
            }
        }
        stage('Push') {
            steps {
                sh "echo test"
            }
        }
        stage('Deploy') {
            steps {
                sh "echo test"
            }
        }
    }
}
