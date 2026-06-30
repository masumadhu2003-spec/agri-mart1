node {

    stage('Checkout') {
        checkout scm
    }

    stage('Create Virtual Environment') {
        sh '''
        python3 -m venv venv
        '''
    }

    stage('Install Dependencies') {
        sh '''
        . venv/bin/activate
        pip install -r requirements.txt
        '''
    }

    stage('Django Check') {
        sh '''
        . venv/bin/activate
        python manage.py check
        '''
    }

    stage('Run Tests') {
        sh '''
        . venv/bin/activate
        python manage.py test
        '''
    }

    stage('Build Successful') {
        echo "Build completed successfully!"
    }
}
