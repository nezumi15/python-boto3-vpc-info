import boto3
from pprint import pprint as pp

def lambda_handler(event, context):
    region_list = get_regions()
    all_vgws = get_vgws(region_list)
    pp(all_vgws)

def get_regions():
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions()['Regions']
    region_list = []
    for region in regions:
        region_list.append(region['RegionName'])
    return region_list

def get_vgws(region_list):
    vgw_list = []
    for region in region_list:
        print(region)
        client = boto3.client('ec2', region_name=region)
        vgw_response = client.describe_vpn_gateways()
        for vgw in vgw_response['VpnGateways']:
            vgw_list.append({region: vgw})
    return vgw_list

lambda_handler('event', 'context')
