import boto3

def add_user( username , group_name):
    iam = boto3.client('iam')
    
    response = iam.add_user_to_group(
        UserName = username,
        GroupName = group_name
    )
    
    print(response)
    
#Replace 'username' with an existing User
#Replace 'group_name' with an existing User group
add_user('username', 'group_name')