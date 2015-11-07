

# Configure Git

https://github.com/join

		git config --global user.name "Beyonce Knowles"
		git config --global user.email beyonce@thinkful.com


# List of files you want Git to ignore

Make a new file in your home directory (~) called `.gitignore_global` 

Copy the contents of this file into .gitignore_global.
https://github.com/github/gitignore/blob/master/Python.gitignore

Then tell Git to use the file as a guide to which files to ignore

		git config --global core.excludesfile ~/.gitignore_global


# Initializing a Git Repository

		git init



# "Saving" files

		git status

		git add .

		git commit -m "Initial commit"

		git status


# Saving to GitHub

Create new repository: https://github.com/new

Add the GitHub repository as a remote to your local Git repository:

		git remote add origin https://github.com/ddbs/tpy.git

Push changes to the remote repository: 

		git push -u origin master


# Pulling code from GitHub

(So that your version matches the version on a remote server)

		git pull origin master




