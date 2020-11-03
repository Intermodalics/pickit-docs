pipeline {
  triggers {
    issueCommentTrigger('.*test this please.*')
  }
  agent any
  stages {
    stage('Build') {
      steps {
        sh "docker build --iidfile image_id ."
      }
    }
    stage('Start instance') {
      when { changeRequest() }
      steps {
        script {
          def container_name = "docs-pr-${pullRequest.number}"
          sh "docker rm --force ${container_name} || true"
          def container_args = "--rm -d \
                                --name ${container_name} \
                                --network demo.pickit3d.com"
          sh "docker run ${container_args} `cat image_id` python -m http.server 8080"

          def post_instance_url_comment = true;
          for (comment in pullRequest.comments) {
            if (comment.body ==~ /.*Docker instance URL.*/) {
              post_instance_url_comment = false;
            }
          }
          if (post_instance_url_comment) {
            pullRequest.comment("Docker instance URL: http://${container_name}.demo.pickit3d.com:8080")
          }
        }
      }
    }
    stage('Update public repository') {
      when {
        expression { BRANCH_NAME ==~ /(2.4)/ }
      }
      steps {
        sh "echo Pushing branch ${BRANCH_NAME} to public repo..."
        sh "git remote add public git@github.com:Intermodalics/pickit-docs.git"
        sh "git push public HEAD:${BRANCH_NAME} -f"
      }
    }
  }
}
