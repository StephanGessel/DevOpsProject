pipeline {
    agent any
    stages {
        stage('Pull Code') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
                git 'https://github.com/StephanGessel/DevOpsJenkins.git'
            }
        }
        stage('run rest app server ') {
            steps {
                script {
                    sh 'nohup python3 web_app.py &'

                }
            }
        }
        stage('run web app server') {
            steps {
                script {
                    sh 'nohup python3 rest_app.py &'

                }
            }
        }
        stage('run backend testing') {
            steps {
                script {
                    sh 'python3 backend_testing.py'

                }
            }
        }
        stage('run frontend testing') {
            steps {
                script {
                    sh 'python3 frontend_testing.py'

                }
            }
        }
        stage('run combined testing') {
            steps {
                script {
                    sh 'python3 combined_testing.py'

                }
            }
        }
        stage('run clean environment ') {
            steps {
                script {
                    sh ' python3 clean_environment.py'

                }
            }
        }
    }
}