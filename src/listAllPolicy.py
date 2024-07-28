import boto3

def list_policies():
    iam = boto3.client('iam')
    
    paginator = iam.get_paginator('list_policies')
    
    policy_count = 0
    
    for response in paginator.paginate(Scope="Local"):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            Arn = policy['Arn']
            policy_count += 1
            print('({}) Policy Name : {} Arn : {}'.format(policy_count,policy_name,Arn))
            
            
list_policies()