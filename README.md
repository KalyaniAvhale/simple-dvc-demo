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

8. ``` dvc add data_given/winequality.csv ```
The dvc add command is analogous to git add, in that it makes DVC aware of the target data, in order to start versioning it. It creates a .dvc file to track the added data.

9. ``` git add . ```
Add file contents to the index.The "index" holds a snapshot of the content of the working tree, and it is this snapshot that is taken as the contents of the next commit. Thus after making any changes to the working tree, and before running the commit command, you must use the add command to add any new or modified files to the index.if you want subsequent changes included in the next commit, then you must run git add again to add the new content to the index.

10. ``` git commit -m "first commit" ```
git commit : Record changes to the repository
-m : specifies the next paramter as message 


11. ``` git add . && git commit -m "updated README.md" ``` : this is chain command that  can be used after we make any changes in files and commit same to reprository.

12. Create git reprository in github

13. ``` git remote add origin https://github.com/KalyaniAvhale/simple-dvc-demo.git ```
: push the commits in the local branch named master to the remote named origin". Once this is executed, all the stuff that you last synchronised with origin will be sent to the remote repository and other people will be able to see them there.

14. ``` git branch -M main ``` : 
git branch command lets you create, list, rename, and delete branches. Here we will rename Master branch to main 

15. ``` git push -u origin main ``` : 
git push -u origin master is used for pushing local content to GitHub. In the code, the origin is your default remote repository name and '-u' flag is upstream, which is equivalent to '-set-upstream. ' and the master is the branch.

16. params.yaml : 
In order to track parameters and hyperparameters associated to machine learning experiments in DVC projects, DVC provides a different type of dependencies: parameters. They usually have simple names like epochs, learning-rate, batch_size, etc.
To start tracking parameters, list them under the params field of dvc.yaml .OR python files can be used additionally (listed under params: with a sub-list of param values). These files are typically written manually (or they can be generated) and they can be versioned directly with Git.The default parameters file name is params.yaml, but any other YAML 1.2, JSON, TOML , python file can be used .

Stage 1 : Load Data 
17. get_data.py :
File will be used to get data from given source , this will include reading params from params.yaml , process it and return the dataframe.

