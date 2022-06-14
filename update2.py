import urllib.parse
import argparse

from utils import update_repo, get_repos


parser = argparse.ArgumentParser(description='Databricks repo updater.')
parser.add_argument('--apikey',  help='Databricks API key')
parser.add_argument('--workspace',  help='Databricks workspace name')
parser.add_argument('--repo',  help='Databricks repo path')

args = parser.parse_args()
print(args)

print("Started update...")
print(args.apikey)

my_token = args.apikey
my_workspace = args.workspace
my_repo = args.repo

res = get_repos(workspace=my_workspace, path=urllib.parse.quote(my_repo), auth_token=my_token)
print(res)
if (len(res)== 0): 
    print("no repository found")
    quit()

if (len(res['repos'])!=1):
    print("multiple repos found")
    quit()

if (len(res['repos'])==1):
    print("got one repo. all good!")

repo_id = res['repos'][0]['id']
print(repo_id)
# 
res = update_repo(workspace=my_workspace, auth_token=my_token, id=repo_id, data={"branch": "master"})
print(res)

print("Finished update!")
