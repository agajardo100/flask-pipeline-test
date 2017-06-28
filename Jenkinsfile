Jenkinsfile(Declarative Pipeline)
pipeline {

    agent {
        docker {image 'python:2.7-slim'}
    }

    environment {

    }

    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello Flask"'
                sh 'echo ls -alt'
                sh 'echo flask db init'
                sh 'echo flask db migrate'
                sh 'echo flask db upgrade'
            }
        }
        stage('Test'){
            steps {
                sh 'python --version'
            }
        }
    }
    post {
        failure {
            mail to: 'andresegajardo@gmail.com',
            subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
            body: "Something is wrong with ${env.BUILD_URL}"
        }
    }
}