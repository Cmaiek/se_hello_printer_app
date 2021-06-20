pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh '''
            python -m venv .venv
            . .venv/bin/activate
            pip intall -r requirements.txt
            pytest -v
        '''
	            sh 'make deps'
	            sh 'make test'
        	}
        }
    }
}