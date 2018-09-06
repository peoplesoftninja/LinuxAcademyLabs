import subprocess
import pwd

def add(user_info):

    print(f"Adding user '{user_info['name']}'")
    subprocess.call([
        'useradd',
        '-p',
        user_info['password'],
        '-G',
        _groups_str(user_info),
        user_info['name']
        ])

def remove(user_info):
    print(f"Removing user '{user_info['name']}'")
    subprocess.call([
        'userdel',
        '-r',
        user_info['name']
        ])


def update(user_info):
    print(f"Updating user '{user_info['name']}'")
    subprocess.call([
        'usermod',
        '-p',
        user_info['password'],
        '-G',
        _groups_str(user_info),
        user_info['name']
        ])


def sync(user_info,existing_users=None):
    existing_users = (existing_users or _user_names())
    user_names = [user['name'] for user in user_info]
    for user in user_info:
        if user['name'] not in existing_users:
            add(user)
        elif user['name'] in existing_users:
            update(user)
    for user_name in existing_users:
        if not user_name in user_names:
            remove({'name':user_name})

def list_all():
    print("Listing all users\n")
    userList = subprocess.call([
        'cut',
        '-d',
        ':',
        '-f1',
        '/etc/passwd'
        ])
    print(userList)

def _user_names():
    return [user.pw_name for user in pwd.getpwall()
            if user.pw_uid >= 1000 and 'home' in user.pw_dir]



def _groups_str(user_info):
    return ','.join(user_info['groups'] or [])


