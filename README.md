# aws_client_python
Python script to update services in AWS ECS.

Parameter Required in Jenkins Freestyle Job.

    1. CLUSTER_NAME
    2. SERVICES_LIST
    3. AWS_DEFAULT_REGION

**CLUSTER_NAME :** Name of ECS Cluster
    
    For e.g.
        CLUSTER_NAME=Test_Cluster


**SERVICES_LIST :** List of Services to be update using this script. Value should be in JSON format.

    Syntax
        SERVICES_LIST={ "service_name1" : #_of_count }
    for e.g.
        SERVICES_LIST={ "nginx" : 1, "ubuntu" : 3 }

**AWS_DEFAULT_REGION :** Provide region of ECS cluster installed.

    For e.g.
        AWS_DEFAULT_REGION=ap-south-1

**Configure AWS Credentials**
Add AWS Credentials in pipeline to create connectivity of Jenkins and AWS.
    > Build Environment > Use secret text(s) or file(s) > Select AWS Credentials

## Jenkins Freestyle Job shell Syntax

Go to Build > Execute shell

    python3 ./ecs_automation.py --cluster $CLUSTER_NAME --services "${SERVICES_LIST}"

[Reference for python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html)
