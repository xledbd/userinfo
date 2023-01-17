from argparse import ArgumentParser

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
    from userinfo import pwdparser

    args = create_parser().parse_args()
    if args.format == 'json':
        pwdparser.write_to_json(args.path)
    elif args.format == 'csv':
        pwdparser.write_to_csv(args.path)
