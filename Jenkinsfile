node {

    stage('Git Checkout') {
        checkout scm
    }

    stage('Python Version') {
        sh 'python3 --version'
    }

    stage('Pip Version') {
        sh 'pip3 --version'
    }

    stage('Install Dependencies') {
        sh 'pip3 install -r requirements.txt'
    }

    stage('Django Check') {
        sh 'python3 manage.py check'
    }

    stage('Run Tests') {
        sh 'python3 manage.py test'
    }

    stage('Collect Static Files') {
        sh 'python3 manage.py collectstatic --noinput'
    }

    stage('Build Successful') {
        echo 'Build Completed Successfully'
    }

}
