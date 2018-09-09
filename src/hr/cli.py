from argparse import ArgumentParser
from hr import inventory, users

def create_parser():
    parser = ArgumentParser("Argument Parser for HR Project")
    parser.add_argument('path',help="the path to the inventory file")
    parser.add_argument(
                '--export',
                help="add json file",
                action='store_true')
    return parser

def main():
    args = create_parser().parse_args()

    if args.export:
        inventory.dump(args.path)
    else:
        users_info = inventory.load(args.path)
        users.sync(users_info)
