Git user guide for collaboration


Solo
1. git clone [repo]
2. Open folder and work 

change repo
1. git status 
2. git add .
3. git commit -m “commit messgae”
4. git push
5. [next time, if any change] git pull

merge changes from main
1. git checkout main
2. git pull
3. git checkout [your_branch]
4. git merge main 
5. git push

Preparation for git 
1. Download git 
2. Prepare personal token to access Github from command line 

Access your Github locally using a token
1. Set email and user neam
	git config —global user.name “”
	git config —global user.email “”
	git config -1
2. Use token to login 
    1. Clone a repo
    2. Enter user name and token


Preparation for collaboration 
1. Create a main repo under a user 
2. For every contributor, fork the repo into their own account 
3. In their local computer, use “git clone http …” to copy the repo from the cloud. 
4. Set origin, “git remote add origin <forked url>”
5. Set upstream, “git remote add upstream <main repo url>”

Before work
1. Run “git status” to check all work are committed
2. If not, run “git add .” & “git commit -m “<message>” “ to clear workspace 
3. Run “git fetch upstream/main” to download the newest version (sometimes main should be changed into master)
4. Run “git merge upstream/main” to update local file. 
5. You can use “git pull” to update from your own repo
6. Ready to work 

After work
1. Run “git add .” To add all changes to workspace 
2. Run “git commit -m “<message>” “ to commit the changes with a reference message
3. Run “git push origin main” to upload your local change to your repo in your account 
4. If the main repo has another update, you should run “fetch & merge” before you “push”
5. Login to Github and start a pull request. 
