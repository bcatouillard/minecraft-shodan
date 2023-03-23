from argparse import ArgumentParser

from src.models.shodan_client import ShodanClient

parser = ArgumentParser()
parser.add_argument(
    "--key", metavar="API KEY", type=str, help="API KEY", action="store"
)
args = parser.parse_args()

if not args.key:
    raise ("Missing key")

ShodanClient(args.key).minecraft_servers()
