# aws_client_python
Python script to update services in AWS ECS.

Commands available to run python script

    List All Services
    python ./ecs_service_automation.py -c <cluster_name> list-services

    for e.g.
    python ./ecs_service_automation.py -c test_cluster list-services

    Upgrade Services
    python ./ecs_service_automation.py -c <cluster_name> upgrade 

    for e.g.
    python ./ecs_service_automation.py -c test_cluster upgrade 

    Downgrade Service
    python ./ecs_service_automation.py -c <cluster_name> downgrade

    python ./ecs_service_automation.py -c test_cluster downgrade

Parameter Required in Jenkins pipeline to build.

    1. CLUSTER_NAME
    2. UPGRADE
    3. DOWNGRADE
    4. AWS_DEFAULT_REGION

**CLUSTER_NAME :** Name of ECS Cluster
    
    For e.g.
        CLUSTER_NAME=Test_Cluster


**UPGRADE :** Enable to upgrade (Boolean).

**DOWNGRADE :** Enable to downgrade (Boolean).

**AWS_DEFAULT_REGION :** Provide region of ECS cluster installed.

    For e.g.
        AWS_DEFAULT_REGION=ap-south-1


[Reference for python script](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html)
