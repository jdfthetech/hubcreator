import argparse
import os
import requests
import json

# pull api key from environment variables
# to set API key in environment variables add the following line to ~/.bashrc (or .zshrc etc):
# export GITKEY="<key value>"

secret = os.environ["GITKEY"]

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--reponame", help="Repo name",required=True)
    parser.add_argument("-u", "--username", help="User name",required=True)
    parser.add_argument("-d", "--description", help="Description")
    parser.add_argument("-i", "--init", help="Init: true/false, default: false",default="false")
    parser.add_argument("-l", "--licenseVer", help="License: ex. gpl-2.0, default: unlicense",default="unlicense")

    args = parser.parse_args()

    api_root = "https://api.github.com/"

    repo = args.reponame
    description = args.description
    user = args.username
    token = secret
    init = args.init
    licenseVer = args.licenseVer

    payload = {'name': repo, 'description': description, 'auto_init': init, 'license': licenseVer}
    
    
    requests.post(api_root + 'user/repos', auth=(user,token), data=json.dumps(payload))
    print("Repository:",repo, "created succesfully with the following options: ",
        "\nDescription: ",description,
        "\nCreated Basic Readme: ",init,
        "\nLicense: ", licenseVer
        )



if __name__=="__main__":
    main()        