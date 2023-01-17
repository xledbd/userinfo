import pwd

def get_user_data():
    entries = pwd.getpwall()
    users = []
    for entry in entries:
        if entry.pw_uid >= 1000:
            users.append({'name': entry.pw_name, 
                'id': entry.pw_uid, 
                'home': entry.pw_dir, 
                'shell': entry.pw_shell})

    return users
