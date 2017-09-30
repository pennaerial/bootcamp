# bootcamp
The purpose of this project is to introduce new members to ROS and Git. You will learn how to use ROS to send text between terminal windows and how to use git to share and version your code.
## Instructions
### Setup
#### Getting the example code
First you will have to get the clone the repository. The process is quite simple. If you don't already have git on your Ubuntu install get it by running `sudo apt update` followed by `sudo apt install git`. Follow these steps to get the code:
1. Navigate into ~/catkin_ws/src : `cd ~/catkin_ws/src`. `~/` is a shorthand for your user's home directory.
2. Clone the repository : `git clone https://github.com/pennaerial/bootcamp.git`. This will make a local copy of the repository on your computer.
3. Now build catkin : `catkin build` or `catkin build bootcamp`. The latter will install only bootcamp. Even though we are using python, catkin will run a script which adds your project to ROS, so that you can run roscommands such as `roscd` or `rosrun`.
4. Restart terminal or `source `~/.bashrc`.
#### Learning git
At this point you should take a minute to learn about git. This [guide](http://rogerdudler.github.io/git-guide/) is a nice place to start. I recomend that you are familiar with command line git, however it is up to you. My favorite graphical git client is [GitKraken](https://www.gitkraken.com/github-student-developer-pack#get-started), which you can get through the (student developer pack)[https://education.github.com/pack]. You can also use version control plugins that are avaiable for most IDEs.
#### Learning GitHub
Hah, so git is not the same things as GitHub. Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency, while GitHub is a really handy service that allows us to store code online and collaborate. Please get familiar with these [guides](https://guides.github.com/).
#### Making your first branch
1. Make a new issue in the bootcamp repository. Call it something descriptive like "[YOURNAME]'s Tutorial". Note the issue number.
2. Go back to git (on your computer) and make sure you are in `~/catkin_ws/src/bootcamp`.
3. Make a new branch by typing `git branch [ISSUE#]-[DESCRIPTIVE NAME]`. For example, `git branch 47-DamianTutorial`. This creates a local branch on your computer.
4. Checkout the new branch `git checkout [BRANCH NAME]`
5. Push (upload) you branch to GitHub : `git push origin [BRANCH NAME]`. Git will complain a bit at this point. It will ask you to run a couple commands to set your email adress etc. Just follow what it says.

### Task
If you navigate to `bootcamp/src` you will find two folders listener and publisher. Each one is a standalone python (package)[https://docs.python.org/3.6/tutorial/modules.html#packages]. Your goal is to use ROS to send text messages from publisher to listener. When both "nodes" are open then by typing into publisher and pressing return I should see the message display in listener. A good place to get started is this (tutorial)[http://wiki.ros.org/rospy/Overview/Publishers%20and%20Subscribers] on (ros wiki)[http://wiki.ros.org/].

### Running your code
1. Start ros master node `roscore`.
2. To run publisher: `rosrun bootcamp publisher`
3. To run listener: `rosrun bootcamp listener`

### Uploading to GitHub
Once you finish working on your code and you test it's awesomeness it's time to share this with other people.
1. Make sure you have checked out your branch: `git checkout [BRANCH NAME]`.
2. View status `git status`.
3. Stage your changes for commit. For every file that you want to upload do `git add [path]`. For example `git add src/publisher/publisher.py`.
4. Commit your changes: `git commit -m "[DESCRIPTIVE MESSAGE]"`
4. Push your code `git push`.
5. Make a pull request on GitHub. Open the repository on GitHub and switch to your branch. Click new pull request. Good job! If I don't have any comments you're done. 


