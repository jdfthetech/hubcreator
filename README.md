# hubcreator
A simply python script to create a basic github repo on the command line.

# IMPORTANT
Your github API key is required in your environment variables.
To set the API key in environment variables add the following line to ~/.bashrc (or .zshrc etc):

export GITKEY="<key value>"


usage: main.py [-h] -r REPONAME -u USERNAME [-d DESCRIPTION] [-i INIT] [-l LICENSEVER]

arguments:
  -h, --help            show this help message and exit

  -r REPONAME, --reponame REPONAME
                        Repo name
  -u USERNAME, --username USERNAME
                        User name
  -d DESCRIPTION, --description DESCRIPTION
                        Description
  -i INIT, --init INIT  
                        Init: true/false, default: false
  -l LICENSEVER, --licenseVer LICENSEVER
                        License: ex. gpl-2.0, default: unlicense

github repo api reference:

https://docs.github.com/en/rest/reference/repos#create

github license reference:

https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository#searching-github-by-license-type

Binary is in the binary folder in case you want to use that in bin, or you can make your own using pyinstaller