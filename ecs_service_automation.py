import argparse
import boto3

client = boto3.client('ecs')
ECS_CLUSTER_NAME="test"

def list_services():
    """List All the services in AWS ECS with in a region"""
    services =  client.list_services(cluster= ECS_CLUSTER_NAME)
    if services.get('ResponseMetadata')['HTTPStatusCode'] == 200 :
        for service in  services.get('serviceArns'):
            print(service)
        return services.get('serviceArns')
    else:
        print("Something went Wrong")
        return None

def upgrade_services():
    """Upgrade the AWS ECS services by 1"""
    services = list_services()
    if services != None:
        for service in services:
            update_service(service,1)
    pass

def downgrade_services():
    """Downgrade the AWS ECS services to 0"""
    services = list_services()
    if services != None:
        for service in services:
            update_service(service,0)
    pass

def update_service(service,d_count):
    try:
        if d_count >= 0:
            response = client.update_service(
                cluster= ECS_CLUSTER_NAME,
                service= service ,
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

def main():
    """Main function to AWS ECS service upgrade automation"""
    try:
        print('-'*88)
        parser = argparse.ArgumentParser(
            "AWS ECS Service upgrade"
        )
        subparser = parser.add_subparsers(help='List of commands for ECS')
        list_parser = subparser.add_parser("list-services",help="List all AWS ECS services")
        list_parser.set_defaults(func=list_services)

        upgrade_service = subparser.add_parser("upgrade",help="Upgrade services desired count to 1")
        upgrade_service.set_defaults(func=upgrade_services)

        downgrade_service = subparser.add_parser("downgrade",help="Downgrade services desired count to 0")
        downgrade_service.set_defaults(func=downgrade_services)

        parser.add_argument(
            "-c",
            "--cluster",
            help="AWS ECS cluster name",
            required=True
        )

        args = parser.parse_args()
        global ECS_CLUSTER_NAME
        ECS_CLUSTER_NAME = args.cluster

        args.func()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()