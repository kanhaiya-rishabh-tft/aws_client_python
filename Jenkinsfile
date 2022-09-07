 pipeline {
  agent { label 'default' }
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    AWS_CREDS = credentials('rishabh-admin')
  }
  stages {
    stage('List Services') {
      steps {
        withCredentials([[
          $class: 'AmazonWebServicesCredentialsBinding',
          credentialsId: 'rishabh-admin',
          accessKeyVariable: 'AWS_ACCESS_KEY_ID',
          secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
          ]]) {
            sh 'python3 ./ecs_service_automation.py -c "${CLUSTER_NAME}" list-services'
          }
      }
    }
//     stage('Upgrade Services') {
//         when {
//           expression { return params.UPGRADE }
//         }
//         steps {
//             withCredentials([[
//             $class: 'AmazonWebServicesCredentialsBinding',
//             credentialsId: 'rishabh-admin',
//             accessKeyVariable: 'AWS_ACCESS_KEY_ID',
//             secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
//             ]]) {
//                 sh 'python3 ./ecs_service_automation.py -c "${CLUSTER_NAME}" upgrade'
//             }
//         }
//     }
//     stage('Downgrade Services') {
//         when {
//          expression { return params.DOWNGRADE }
//         }
//         steps {
//             withCredentials([[
//             $class: 'AmazonWebServicesCredentialsBinding',
//             credentialsId: 'rishabh-admin',
//             accessKeyVariable: 'AWS_ACCESS_KEY_ID',
//             secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
//             ]]) {
//                 sh 'python3 ./ecs_service_automation.py -c "${CLUSTER_NAME}" downgrade'
//             }
//         }
//     }
       stage("Run Script") {
            steps {
				sh 'python3 ./ecs_service_automation.py -c "${CLUSTER_NAME}" "${CHOICE}" '
			}
       }
  }
}
