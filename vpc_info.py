import sys

def display_menu():
    print("Select an option:")
    print("1. List NAT Gateways")
    print("2. List S3 Endpoints")
    print("3. Describe Main Route Table")
    print("4. List Transit Gateways")
    print("5. List VPN Gateways")
    print("0. Exit")

def run_script(script_index):
    if script_index == 1:
        import vpc_natgw
        vpc_natgw.lambda_handler('event', 'context')
    elif script_index == 2:
        import vpc_s3_enpoints
        vpc_s3_enpoints.lambda_handler('event', 'context')
    elif script_index == 3:
        import vpc_rt
        vpc_rt.lambda_handler('event', 'context')
    elif script_index == 4:
        import vpc_tgw
        vpc_tgw.lambda_handler('event', 'context')
    elif script_index == 5:
        import vpc_vgw
        vpc_vgw.lambda_handler('event', 'context')
    else:
        print("Invalid option. Please try again.")

def main():
    while True:
        display_menu()
        option = input("Enter your choice (0-5): ")
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
