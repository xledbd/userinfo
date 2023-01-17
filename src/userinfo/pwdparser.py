import pwd
import sys
import json
import csv

def _get_user_data() -> dict:
    entries = pwd.getpwall()
    users = []
    for entry in entries:
        if entry.pw_uid >= 1000:
            users.append({'name': entry.pw_name, 
                'id': entry.pw_uid, 
                'home': entry.pw_dir, 
                'shell': entry.pw_shell})

    return users

def write_to_json(path):
    fp = sys.stdout
    if path != None:
        fp = open(path, 'w')
    json.dump(_get_user_data(), fp)
    fp.close()

def write_to_csv(path):
    fp = sys.stdout
    if path != None:
        fp = open(path, 'w', newline='')
    users = _get_user_data()
    fieldnames = users.keys()
    writer = csv.DictWriter(fp, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(users)

    fp.close()
