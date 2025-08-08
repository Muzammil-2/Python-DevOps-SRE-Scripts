def list_console_users():
    users = iam.list_users()
    for user in users['Users']:
        login_profile = None
        try:
            login_profile = iam.get_login_profile(UserName=user['UserName'])
        except iam.exceptions.NoSuchEntityException:
            continue
        if login_profile:
            print(f"User {user['UserName']} has console access")

list_console_users()
