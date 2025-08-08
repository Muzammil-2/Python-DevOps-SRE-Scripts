def rotate_access_key(user_name):
    keys = iam.list_access_keys(UserName=user_name)['AccessKeyMetadata']
    
    if len(keys) >= 2:
        print("User already has two keys. Please delete one before rotating.")
        return

    new_key = iam.create_access_key(UserName=user_name)['AccessKey']
    print(f"New access key created: {new_key['AccessKeyId']}")

    # Optional: deactivate and delete old key
    old_key_id = keys[0]['AccessKeyId']
    iam.update_access_key(UserName=user_name, AccessKeyId=old_key_id, Status='Inactive')
    iam.delete_access_key(UserName=user_name, AccessKeyId=old_key_id)
    print(f"Old key {old_key_id} deactivated and deleted.")

rotate_access_key('newuser')
