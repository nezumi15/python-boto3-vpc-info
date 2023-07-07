# Script to list S3 Endpoints
import boto3
from pprint import pprint as pp

def lambda_handler(event, context):

    region_list = get_regions()
    all_s3_endpoints = get_s3_endpoints(region_list)
    pp(all_s3_endpoints)

def get_regions():
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions()['Regions']
    region_list = []
    for region in regions:
        region_list.append(region['RegionName'])

    return region_list 

def get_s3_endpoints(region_list):
    s3_endpoint_list = []
    for region in region_list:
        print(region)
        client = boto3.client(;ec2, region_name=region)
        vpc_endpoints = client.describe_vpc_endpoints()
        for vpc_endpoint in vpc_endpoints['VpcEndpoints']:
            for tag in vpc_endpoint['Tags']:
                if tag['Key'] == 'Name':
                    if 's3' in tag['Value'] and 'endpoint' in tag['Value']:
                        s3_endpoint_list.append({region: tag['Value']})

    return s3_endpoint_list

lambda_handler('event', 'context')
