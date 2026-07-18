pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Branch information') {
            steps {
                echo "Building branch: ${env.BRANCH_NAME}"
                echo "Commit: ${env.GIT_COMMIT}"
            }
        }

        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest discover -s tests -p "test_*.py" -v'
                    } else {
                        bat 'python -m unittest discover -s tests -p "test_*.py" -v'
                    }
                }
            }
        }

        stage('Package') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 package_app.py'
                    } else {
                        bat 'python package_app.py'
                    }
                }
                archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
            }
        }

        stage('Deploy simulation') {
            when {
                branch 'main'
            }
            steps {
                echo 'Main branch passed: simulating a production deployment.'
            }
        }
    }

    post {
        success {
            echo "${env.BRANCH_NAME} completed successfully."
        }
        failure {
            echo "${env.BRANCH_NAME} failed. Check the test output above."
        }
    }
}

