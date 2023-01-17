from argparse import ArgumentParser, Action

def create_parser():
    parser = ArgumentParser(description='Export user info in JSON or CSV format.')

    parser.add_argument('--format', '-f', 
        help='Output format (default: %(default)s)', 
        default='json',
        choices=['json', 'csv'],
        type=str.lower,
        metavar='FORMAT')
    parser.add_argument('--path', '-o',
        help='Destination file',
        metavar='FILE')

    return parser

def main():

    args = create_parser().parse_args()
    print(args)
