def create_user_and_add_to_group(user_name, group_name):
    iam.create_user(UserName=user_name)
    iam.add_user_to_group(GroupName=group_name, UserName=user_name)
    print(f"User {user_name} created and added to group {group_name}")

create_user_and_add_to_group('newuser', 'DevOpsTeam')
