import argparse
from api import create_api_app
from website import create_web_app

actions = ("runapi", "runweb", "runall")

parser = argparse.ArgumentParser(description="Manage the application")
parser.add_argument("action", type=str, help="Action to perform")
parser.add_argument(
    "--apiport", "-ap", type=int, default="8000", help="Port for the API server"
)
parser.add_argument(
    "--webport", "-wp", type=int, default="5000", help="Port for the web server"
)
parser.add_argument(
    "--debug",
    "-d",
    action="store_true",
    help="Debug mode",
)
args = parser.parse_args()

if args.action.lower() not in actions:
    raise Exception("Invalid action")

if __name__ == "__main__":
    if (action := args.action) == "runapi":
        create_api_app().run(debug=args.debug, port=args.apiport)
    elif action == "runweb":
        create_web_app().run(debug=args.debug, port=args.webport)
    elif action == "runall":
        create_api_app().run(debug=args.debug, port=args.apiport)
        create_web_app().run(debug=args.debug, port=args.webport)
