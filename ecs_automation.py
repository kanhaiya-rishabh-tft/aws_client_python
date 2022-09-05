#!/bin/python

import boto3
import argparse
import json

client = boto3.client('ecs')
ECS_CLUSTER_NAME = "Test_Clusters"
# ECS_SERVICE = "nginx-service"
ECS_TASK_DEFINITION = 'arn:aws:ecs:ap-south-1:891386428094:task-definition/CustomNginx:6'

# def create_ecs_cluster():
#     response = client.create_cluster(
#         clusterName= ECS_CLUSTER_NAME
#     )

# def list_ecs_cluster():
#     return client.list_clusters()

def list_ecs_services():
    services =  client.list_services(cluster= ECS_CLUSTER_NAME)
    if services.get('ResponseMetadata')['HTTPStatusCode'] == 200 :
        return services.get('serviceArns')
    else:
        return None

# def list_ecs_tasks():
#     tasks =  client.list_tasks(cluster = ECS_CLUSTER_NAME)
#     if tasks.get('ResponseMetadata')['HTTPStatusCode'] == 200 : 
#         return tasks.get('taskArns')
#     else :
#         return None

# def create_ecs_services():
#     create_service = client.create_service(
#         cluster= ECS_CLUSTER_NAME,
#         serviceName= ECS_SERVICE ,
#         taskDefinition=ECS_TASK_DEFINITION,
#         launchType='FARGATE',
#         # healthCheckGracePeriodSeconds=30,
#         enableExecuteCommand=True,
#         desiredCount=2,
#         networkConfiguration={
#             'awsvpcConfiguration': {
#                 'subnets': [
#                     'subnet-073db37a8c447e7f8',
#                     'subnet-017955bec7c63ae7c',
#                     'subnet-0bed54e9ac42a65fd'
#                 ],
#                 'securityGroups': [
#                     'sg-0d12a24204f86d226',
#                 ],
#                 'assignPublicIp': 'ENABLED'
#             }
#         },
#     )
#     pass

def update_ecs_service(service,d_count):
    try:
        if d_count >= 0:
            response = client.update_service(
                cluster= ECS_CLUSTER_NAME,
                service= service ,
                taskDefinition=ECS_TASK_DEFINITION,
                desiredCount=d_count
            )
            if response.get('ResponseMetadata')['HTTPStatusCode'] == 200:
                print('-'*88)
                print("{} desired value is updated to {}".format(service,d_count))
            else :
                print('-'*88)
                print(response.get('ResponseMetadata'))
        else:
            print('-'*88)
            print("Error : {} container value provided is less than 0".format(service))
    except Exception as e:
        print('-'*88)
        print(e)


def arg_parse():
    try:
        parser = argparse.ArgumentParser(
            'AWS ECS Deployment Script'
        )
        parser.add_argument(
            '-c',
            '--cluster',
            help='Name of the cluster',
            required=True

        )
        parser.add_argument(
            '-s',
            '--services',
            help='List of Services in JSON',
            required=True,
            type= str
        )
        args = parser.parse_args()
        global ECS_CLUSTER_NAME
        ECS_CLUSTER_NAME = args.cluster
        services = json.loads(args.services)
        print("{} {}".format(ECS_CLUSTER_NAME,services))
        print('-'*88)
        print("Welcome to the AWS ecs client!")
        for service in services:
            update_ecs_service( service=service,d_count=services[service])
        
    except json.JSONDecodeError:
        print('-'*88)
        print("Error : Json value passed ")
    except Exception as e :
        print('-'*88)
        print("Error : {}".format(e))
    finally:
        print('-'*88)
        
   

if __name__ == '__main__':
    # usage_demo()
    arg_parse()
