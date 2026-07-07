pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                sh 'git clone https://github.com/masumadhu2003-spec/agri-mart1.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                cd agri-mart1
                python3 -m venv venv
                '''
            }
        }

    }
}
