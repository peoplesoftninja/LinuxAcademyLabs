import pytest
import subprocess

from hr import users


# encrypted version of password
password = '$6$sieuGnUH3d4UqXYo$fu8/MJoj7yN3CjpAHlKXM/rRfkbQPCLbWkHYGJWHMRsiLdEqoxBLBhvir6RRwQRBlFIv229lo0qL77VtytGSZ/'

user_dict = {
        'name':'kevin',
        'groups':['wheel','dev'],
        'password':password
        }

def test_users_add(mocker):
    """
    Given a user dictionary user.add(..) should
    utilize `useradd` to create a user with the password
    """
    mocker.patch('subprocess.call')
    users.add(user_dict)
    subprocess.call.assert_called_with([
        'useradd',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'kevin'
        ])

def test_users_remove(mocker):
    """
    Delete the user based on the user dictionary
    """
    mocker.patch('subprocess.call')
    users.remove(user_dict)
    subprocess.call.assert_called_with([
        'userdel',
        '-r',
        'kevin',
        ])


def test_users_update(mocker):
    """
    Update user based on the user dictionary
    utilize `usermod` to set the groups and password for the user
    """
    mocker.patch('subprocess.call')
    users.update(user_dict)
    subprocess.call.assert_called_with([
        'usermod',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'kevin'
        ])

def test_users_sync(mocker):
    """
    Given a list of user dictionaries users.synch(..)should
    create the missing users
    remove extra non-system users
    update existing users
    """
    existing_user_names = ['kevin','bob']
    users_info = [
            user_dict,
            {
                'name':'jose',
                'groups':['wheel'],
                'password':password
            }
        ]
    mocker.patch('subprocess.call')
    users.sync(users_info, existing_user_names)
    subprocess.call.assert_has_calls([
        mocker.call([
            'usermod',
            '-p',
            password,
            '-G',
            'wheel,dev',
            'kevin',
            ]),
        mocker.call([
            'useradd',
            '-p',
            password,
            '-G',
            'wheel',
            'jose'
            ]),
        mocker.call([
            'userdel',
            '-r',
            'bob',
            ]),
        ])

def test_users_list_all(mocker):
    """
    Give a list of users
    """
    mocker.patch('subprocess.call')
    users.list_all()
    subprocess.call.assert_called_with([
        'cut',
        '-d',
        ':',
        '-f1',
        '/etc/passwd'
        ])

















