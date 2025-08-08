def attach_policy_to_user(user_name, policy_arn):
    iam.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)
    print(f"Policy {policy_arn} attached to {user_name}")

# Example ARN: arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess
attach_policy_to_user('newuser', 'arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess')
