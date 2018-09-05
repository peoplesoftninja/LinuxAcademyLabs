from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser("Argument Parser for HR Project")
    parser.add_argument('path',help="the path to the inventory file")
    parser.add_argument(
                '--export',
                help="add json file",
                action='store_true')
    return parser
