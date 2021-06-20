pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh '''
            python3 -m venv .venv
            . .venv/bin/activate
            '''
	            sh 'make deps'
	            sh 'make test'
        	}
        }
    }
}