import boto3
from pprint import pprint as pp

def get_regions():
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions()['Regions']
    region_list = []
    for region in regions:
        region_list.append(region['RegionName'])
    return region_list

def describe_s3_endpoints():
    region_list = get_regions()
    s3_endpoint_list = []
    for region in region_list:
        client = boto3.client('ec2', region_name=region)
        vpc_endpoints = client.describe_vpc_endpoints()
        for vpc_endpoint in vpc_endpoints['VpcEndpoints']:
            for tag in vpc_endpoint['Tags']:
                if tag['Key'] == 'Name':
                    if 's3' in tag['Value'] and 'endpoint' in tag['Value']:
                        s3_endpoint_list.append({region: tag['Value']})
    return s3_endpoint_list

def describe_vgw_info():
    region_list = get_regions()
    vgw_list = []
    for region in region_list:
        client = boto3.client('ec2', region_name=region)
        vgw_response = client.describe_vpn_gateways()
        for vgw in vgw_response['VpnGateways']:
            vgw_list.append({region: vgw})
    return vgw_list

def describe_nat_gateways():
    region_list = get_regions()
    nat_gateway_list = []
    for region in region_list:
        client = boto3.client('ec2', region_name=region)
        nat_gateway_response = client.describe_nat_gateways()
        for nat_gateway in nat_gateway_response['NatGateways']:
            nat_gateway_list.append({region: nat_gateway})
    return nat_gateway_list

def describe_main_route_table(vpc_id):
    ec2 = boto3.client('ec2')
    response = ec2.describe_route_tables(Filters=[{'Name': 'association.main', 'Values': ['true']}, {'Name': 'vpc-id', 'Values': [vpc_id]}])
    main_route_table = response['RouteTables']
    return main_route_table

def print_menu():
    print("Please select an option:")
    print("1. Describe S3 Endpoints")
    print("2. Describe Virtual Private Gateways")
    print("3. Describe NAT Gateways")
    print("4. Describe Main Route Table")
    print("5. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            s3_endpoints = describe_s3_endpoints()
            pp(s3_endpoints)
        elif choice == '2':
            vgws = describe_vgw_info()
            pp(vgws)
        elif choice == '3':
            nat_gateways = describe_nat_gateways()
            pp(nat_gateways)
        elif choice == '4':
            vpc_id = input("Enter VPC ID: ")
            main_route_table = describe_main_route_table(vpc_id)
            pp(main_route_table)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
