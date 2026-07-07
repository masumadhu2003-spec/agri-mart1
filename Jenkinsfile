pipeline {
    agent any

    stages {

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                '''
            }
        }
stage('Install Dependencies') {
    steps {
        sh '''
        . venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        '''
    }
}
 stage('Django Check') {
            steps {
                sh '''
                venv/bin/python manage.py check
                '''
            }
        }
    }
}
