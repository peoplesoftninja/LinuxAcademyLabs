import json
import grp
import spwd
from hr import helpers

def load(path):
    """
    Function to read a given inventory file, parse the JSON, and return
    a list of user dictionaries
    """
    with open(path) as f:
        return json.load(f)

def dump(path, user_names=helpers.user_names()):
    users = []
    for user_name in user_names:
        password = spwd.getspnam(user_name).sp_pwd
        groups = _groups_for_users(user_name)
        users.append({
            'name':user_name,
            'groups':groups,
            'password':password
            })
    with open(path, 'w') as f:
        json.dump(users,f)

def _groups_for_users(user_name):
    return [g.gr_name for g in grp.getgrall() if user_name in g.gr_mem]
