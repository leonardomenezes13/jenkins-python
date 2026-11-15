pipeline {
    agent any // Executar em agente Windows com python e git no PATH.
    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
        timestamps()
    }
    // Demonstração: a cada cinco minutos. Desativar após a gravação.
    triggers { cron('H/5 * * * *') }
    environment { PYTHONIOENCODING = 'utf-8' }
    stages {
        stage('Checkout GitHub') {
            steps {
                deleteDir()
                checkout scm
            }
        }
        stage('Preparar Python') {
            steps {
                bat 'python -m venv .venv-jenkins'
                bat '.venv-jenkins\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }
        stage('Build - verificar sintaxe') {
            steps { bat '.venv-jenkins\\Scripts\\python.exe -m compileall -q src' }
        }
        stage('Testes e gerar cobertura') {
            steps {
                script {
                    int status = bat(returnStatus: true, script: '.venv-jenkins\\Scripts\\python.exe -m pytest --junitxml=reports/junit.xml --cov=conversor --cov-report=term-missing --cov-report=xml:reports/coverage.xml --cov-report=html:reports/htmlcov')
                    if (status == 1) {
                        unstable('Pytest detectou testes reprovados; publicar JUnit na próxima etapa.')
                    } else if (status != 0) {
                        error("Erro de execução do Pytest (código ${status}).")
                    }
                }
            }
        }
        stage('Publicar resultados JUnit') {
            steps { junit testResults: 'reports/junit.xml', allowEmptyResults: false }
        }
        stage('Apresentar cobertura') {
            steps {
                echo 'A porcentagem calculada aparece na tabela TOTAL do console da etapa de testes.'
                archiveArtifacts artifacts: 'reports/coverage.xml,reports/htmlcov/**', allowEmptyArchive: false
            }
        }
    }
}
