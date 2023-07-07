import sys

def display_menu():
    print("Select an option:")
    print("1. List VPC CIDRs")
    print("2. List NAT Gateways")
    print("3. List Main Routing Table")
    print("4. List S3 Endpoints")
    print("5. List Transit Gateways")
    print("6. List VPN Gateways")
    print("0. Exit")

def run_script(script_index):
    if script_index == 1:
        import vpc_vpc_cidrs
        vpc_cidrs.lambda_handler('event', 'context')
    elif script_index == 2:
        import vpc_ngw
        vpc_ngw.lambda_handler('event', 'context')
    elif script_index == 3:
        import vpc_rt
        vpc_rt.lambda_handler('event', 'context')
    elif script_index == 4:
        import vpc_s3_endpoints
        vpc_s3_endpoints.lambda_handler('event', 'context')
    elif script_index == 5:
        import vpc_tgw
        vpc_tgw.lambda_handler('event', 'context')
    elif script_index == 6:
        import vpc_vpg
        vpc_vpg.lambda_handler('event', 'context')
    else:
        print("Invalid option. Please try again.")

def main():
    while True:
        display_menu()
        option = input("Enter your choice (0-6): ")
        try:
            option = int(option)
            if option == 0:
                print("Exiting...")
                break
            else:
                run_script(option)
        except ValueError:
            print("Invalid option. Please enter a number.")

if __name__ == "__main__":
    main()
