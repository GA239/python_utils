pipeline {
  agent any
  stages {
    stage('Build') {
      agent any
      steps {
        echo 'Building'
        sh '''python -m venv ${BUILD_TAG}
source activate ${BUILD_TAG}
pip install -r requirements-dev.txt
python -m pytest tests/ -svv'''
      }
    }
    stage('Test') {
      steps {
        echo 'Testing'
        sh '''source activate ${BUILD_TAG}
python -m pytest tests/ -svv'''
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying'
      }
    }
  }
  post {
    always {
      echo 'This will always run'

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