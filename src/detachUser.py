import boto3

def detach_user(username,policy_arn):
    iam = boto3.client('iam')
    
    response = iam.detach_policy(
        UserName = username,
        PolicyArn = policy_arn
        
    )
    
    print(response)

    
detach_user('testusername','arn from aws policy')