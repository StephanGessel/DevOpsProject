pipeline {
    agent any
    environment {
        registry = "my-user/my-repo"
        registryCredential = 'docker_hub'
        dockerImage = ''
    }
    stages {
        stage('Pull Code') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
                git 'https://github.com/StephanGessel/DevOpsProject.git'
            }
        }
        stage('run rest app server ') {
            steps {
                script {
                    sh 'nohup python3.9 web_app.py &'

                }
            }
        }
        stage('run web app server') {
            steps {
                script {
                    sh 'nohup python3.9 rest_app.py &'

                }
            }
        }
        stage('run backend testing') {
            steps {
                script {
                    sh 'python3.9 backend_testing.py'

                }
            }
        }
        stage('run frontend testing') {
            steps {
                script {
                    sh 'python3.9 frontend_testing.py'

                }
            }
        }
        stage('run combined testing') {
            steps {
                script {
                    sh 'python3.9 combined_testing.py'

                }
            }
        }
        stage('run clean environment ') {
            steps {
                script {
                    sh 'python3.9 clean_environment.py'

                }
            }
        }
    }
}
