def delete_user(user_name):
    # Detach all policies
    for policy in iam.list_attached_user_policies(UserName=user_name)['AttachedPolicies']:
        iam.detach_user_policy(UserName=user_name, PolicyArn=policy['PolicyArn'])

    # Remove from groups
    for group in iam.list_groups_for_user(UserName=user_name)['Groups']:
        iam.remove_user_from_group(GroupName=group['GroupName'], UserName=user_name)

    # Delete access keys
    for key in iam.list_access_keys(UserName=user_name)['AccessKeyMetadata']:
        iam.delete_access_key(UserName=user_name, AccessKeyId=key['AccessKeyId'])

    # Delete user
    iam.delete_user(UserName=user_name)
    print(f"User {user_name} deleted successfully")

delete_user('newuser')
