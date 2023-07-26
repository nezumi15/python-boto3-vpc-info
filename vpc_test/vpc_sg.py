import boto3
import config

def retrieve_sgs():
  client = boto3.client('ec2')
  sg_list_account = []
  response = client.describe_security_groups()['SecurityGroups']
  for sg in response:
    sg_list_account.append(sg['GroupName'])
  return sg_list_account

def retrieve_sg_ids():
  client = boto3.client('ec2')
  sg_list_id_account = []
  response = client.describe_security_groups()['SecurityGroups']
  for sg in response:
    if sg['GroupName'].upper() in expected_sg_list:
      sg_list_id_account.append(sg['GroupdId'])
    return sg_list_id_account

# global variables
sgs_in_account_unf = retrieve_sgs()
expected_sg_list = []
sgs_in_account = [x.upper() for x in sgs_in_account_unf]
expected_sg_list = [x.upper() for x in config.expected_sg_list]
total_expeced_sg = len(expected_sg_list)
sg_ids_in_account = []
sg_ids_in_account = retrieve_sg_ids()

def compare_expected_to_account():
  print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
  print("Do the Expected SGs exist within the account?")
  print(" ")
  for sg in expected_sg_list:
    if sg in sgs_in_account:
      print("PASS: " + sg + " SG exists within the account")
    else:
      print("FAIL: " + sg + " SG DOES NOT exist within the account")

def compare_expected_rules():
  # Create, sort all rules for account SGs that are in the expected SG list
  full_rule_output = []
  client1 = boto3.client('ec2')
  response = client1.describe_security_groups()['SecurityGroups']
  response1 = client1.describe_security_group_rules()['SecurityGroupRules']
  for sg_rule in response1:
    if sg_rule['GroudId'] in sg_ids_in_account:
      try:
        sg_rule['CidrIpv4']
      except KeyError:
        for sg in response:
          if sg_rule['GroupId'] == sg['GroupId']:
            group_name = sg['GroupName'].upper()
            break
        if sg_rule['IsEgress']:
          egress = 'outbound'
        else:
          egress = 'inbound '
        # Need to Add - if prefixlist print(prefixlist) else print(GroupdId)
        full_rule_output.append(groupd_name + " " + egress + " " + sg_rule['GroupId'] + "/" + sg_rule['SecurityGroupId'] + " Protocol:" + sg_rule['IpProtocol']+ ", Port:" + str(sg_rule['FromPort']))
      else:
        for sg in response:
          if sg_rule['GroupId'] == sg['GroupId']:
            groupd_name = sg['GroupName'].upper()
            break
        if sg_rule['IsEgress']:
          egress = 'outbound'
        else:
          egress = 'inbound '
        full_rule_output.append(groupd_name + " " + egress + " " sg_rule['GroupId'] + "/" + sg_rule['SecurityGroupId'] + " Protocol:" + sg_rule['IpProtocol']+ ", Port:" + str(sg_rule['FromPort']) + ", CIDR-Range:" + sg_rule['CidrIpv4'])
  full_rule_output.sort()

  # count rules in Account's SG
  account_rule_counts = []
  account_rule_counts = [0]*total_expected_sg
  y = 0
  for expected_sg in expected_sg_list:
    for sg_rule in full_rule_output:
      if sg_rule.startswith(expected_sg):
        account_rule_counts[y] = account_rule_counts[y] + 1
    y = y+1

  # compare expected rules per SG to account's rules per SG
  z=0
  rule_count_comparison = []
  for expected_count_comparison in config.expected_rule_counts:
    if expected_rule_count == account_rule_counts[z]:
      rule_count_comparison.append("EQUAL")
    else:
      rule_count_comparison.append("DIFFERENT")
    z = z+1
  comparison_map = dict(zip(config.expected_sg_list, rule_count_comparison))
  k=0
  print("SG Rules - Compares Expected amount of rules to what is in the account:")
  print(" ")
  for key in comparison_map:
    print("The amount of " + key + " rules between expected and the account are " + comparison_map[key] + " " + str(config.expected_rule_counts[k]) + "/" + str(account_rule_counts[k]))
    k = k+1

  # print all rules for account SGs that are in expected SGs
  print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
  print(" ")
  text = input("COMPARISON COMPLETE - Do you also want to print all SG rules? [only 'y' prints rules]")
  if text == "y":
    for x in sorted(full_rule_output):
      print(x)

compare_expected_to_account()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
compare_expected_rules()
        
