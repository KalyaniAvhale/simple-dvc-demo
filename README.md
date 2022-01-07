1. Create virtual env
``` $ conda create -n wineq python=3.9 -y ```

2. Activate the vir env 
``` $ conda activate wineq ```

3. Create requirements.txt and add required packages list
4. install the required lib from requirements.txt file
``` $ pip install -r requirements.txt ```

4. Define Forlder structure 
create template.py d=to define folder structure,and run it 
``` $python template.py```

5. Download Wine Quality dataset 
![https://archive.ics.uci.edu/ml/datasets/wine+quality]

6. ``` git init ``` 
This command creates an empty Git repository - basically a .git directory with subdirectories for objects, refs/heads, refs/tags, and template files. An initial branch without any commits will be created


7. ``` dvc init ```
Initialize a DVC project in the current working directory.At DVC initialization, a new .dvc/ directory is created for configuration, default cache location, and other internal files and directories, that are hidden from the user. This directory is automatically staged with git add, so it can be easily committed with Git.

8. ``` dvc add data_given/winequality.csv ``
The dvc add command is analogous to git add, in that it makes DVC aware of the target data, in order to start versioning it. It creates a .dvc file to track the added data.

9. ``` git add . ```
Add file contents to the index.The "index" holds a snapshot of the content of the working tree, and it is this snapshot that is taken as the contents of the next commit. Thus after making any changes to the working tree, and before running the commit command, you must use the add command to add any new or modified files to the index.if you want subsequent changes included in the next commit, then you must run git add again to add the new content to the index.

10. ``` git commit -m "first commit" ```
git commit : Record changes to the repository
-m : specifies the next paramter as message 


