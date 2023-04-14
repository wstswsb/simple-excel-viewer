import argparse
import os

from main import main


class KwargsAppendAction(argparse.Action):
    def __call__(self, parser, args, values, option_string=None):
        try:
            d = dict(map(lambda x: x.split("="), values))
        except ValueError:
            raise argparse.ArgumentError(
                self, f'Could not parse argument "{values}" as k1=v1 k2=v2 ... format'
            ) from None
        setattr(args, self.dest, d)


def get_valid_filename(parser, path_to_file):
    if os.path.exists(path_to_file):
        return path_to_file
    parser.error(f"The file {path_to_file} does not exist")


parser = argparse.ArgumentParser(description="...")
parser.add_argument(
    "-i",
    dest="filename",
    required=True,
    help="input file with two matrices",
    metavar="FILE",
    type=lambda x: get_valid_filename(parser, x),
)
parser.add_argument(
    "-f",
    "--filters",
    dest="filters",
    nargs="*",
    default={},
    required=False,
    action=KwargsAppendAction,
    metavar="KEY=VALUE",
    help="Add key/value params. May appear multiple times. Aggregate in dict",
)
args = parser.parse_args()

if __name__ == "__main__":
    main(path=args.filename, filters=args.filters)
