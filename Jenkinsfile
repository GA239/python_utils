pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'build'
        sh '''echo ${WORKSPACE}
echo ${BUILD_TAG}
python -m venv ${BUILD_TAG}
source ${BUILD_TAG}/Scripts/activate
pip install -r requirements-dev.txt'''
      }
    }
    stage('Test') {
      steps {
        echo 'test'
        sh '''echo ${WORKSPACE}
echo ${BUILD_TAG}
source ${BUILD_TAG}/Scripts/activate
python -m pytest tests/ -svv --junit-xml test-reports/results.xml'''
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
  options {
    disableConcurrentBuilds()
  }
}