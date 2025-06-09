### Intro Version control and Git (local repository)

#                   git add                git commit                              git push
# working directory --------> staging area ---------> git local repository (.git) ---------> remote repository

# create an empty git repository -> git init
# files in the git staging area -> git status, untracked files in red
# adding files in the staging area -> git add filename
# adding everything in the current directory -> git add .
# commiting files to a new save point in the repository -> git commit -m "Commit message, in present tense!"
# see what's to be commited -> git status
# seeing last commits -> git log
# compare file to last commited version -> git diff filename
# roll back to previous file version -> git checkout filename
# clear staging area -> git rm --cached -r .

### Github and remote repositories

# create remote repository git remote add origin https://github.com/ngerov/Story.git
# push local repository to remote repository -> git branch -M main, and then git push -u origin main

### .gitignore -> set rules to prevent commiting certain things (passwords, apikeys)

# create a gitignore file -> touch .gitignore
# then we need to add the names of the files to be ignored in .gitignore

### git clone -> cloning a remote repository to the local machine

# git clone https://github.com/ngerov/Story.git

### Branching and merging

# creating a new branch to develop in -> git branch name-of-branch
# list the branches -> git branch
# switch to the side branch -> git checkout name-of-branch
# mergin the experimental branch to the og one -> git merge name-of-branch