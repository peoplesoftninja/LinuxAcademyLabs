import pytest
import tempfile
from hr import inventory

def test_inventory_load():
    """
    inventory.load(..) will read a given file in json and
    store it as a list
    """
    inv_file = tempfile.NamedTemporaryFile(delete=False)
    inv_file.write(b"""
    [
    {
    "name":"kevin",
    "groups":["wheel","dev"],
    "password":"password_one"
    },
    {
    "name": "lisa",
    "groups": ["wheel"],
    "password": "password_two"
    },
    {
    "name": "jim",
    "groups": [],
    "password": "password_three"
     }
     ]
     """)
    inv_file.close()
    users_list = inventory.load(inv_file.name)
    assert users_list[0] == {
            'name': 'kevin',
                    'groups': ['wheel', 'dev'],
                            'password': 'password_one'
                                }
    assert users_list[1] == {
                        'name': 'lisa',
                                'groups': ['wheel'],
                                        'password': 'password_two'
                                            }
    assert users_list[2] == {
                            'name': 'jim',
                                    'groups': [],
                                            'password': 'password_three'
                                                }

