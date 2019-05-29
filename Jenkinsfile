pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building'
      }
    }
    stage('Test') {
      steps {
        echo 'Testing'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying'
      }
    }
    stage('end') {
      steps {
        echo 'end'
      }
    }
  }
  post {
    always {
      echo 'This will always run'

    stages {
        stage('Build') {
            steps {
                echo 'Building'
            }
        }
        stage('Test') {
            steps {
                sh '''
                python -m venv env_${BUILD_TAG}
                source activate env_${BUILD_TAG}.bat
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }

    success {
      echo 'This will run only if successful'

    }

    failure {
      echo 'This will run only if failed'

    }

    unstable {
      echo 'This will run only if the run was marked as unstable'

    }

    changed {
      echo 'This will run only if the state of the Pipeline has changed'
      echo 'For example, if the Pipeline was previously failing but is now successful'

    }

  }
}