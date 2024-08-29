import boto3

def attach_policy(policy_arn,group_name):
    iam = boto3.client('iam')
    
    response = iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )
    
    print(response)
    
#policy_arn needs to be replaced with the ARN of a policy
#group-name needs to be replaced with the name of a User Group
attach_policy('policy_arn','group_name')