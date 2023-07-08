# neurolab-mongo-python

![image](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### step 3 - Git Version

```bash
Git --Version
```

### step 4 - mongodb connection

```bash
Add connect- connect with connecting string and paste local url from main file

mongodb://localhost:27017
```


### step 5 -create/ download dataset

```bash
write in terminal- wget 'paste url/git hub link'
```

### step 6 - Insert this record or dataset in mongodb

```bash
create filename - data_dump.py
```


### step 7 - To Insert this record or dataset in mongodb
 
 ```bash
write source code
```


### step 8 - install pandas lib

```bash
write pandas in requirements and 

import pandas in main file om top

copy path by clicking on csv file pass location to create variable 
```


### step 9 - Convert dataframe to json so that we can dump these records in momgodb
  ```bash 
     #Convert dataframe to json so that we can dump these records in momgodb
    df.reset_index(drop=True, inplace= True)
```


### step 10 - to remove git repo

```bash
git remote -v ---> to check
git remote remove origin ---> to remove  
# hereorigin is just a variable u can name it with other name as well
to check again ---->  get remote-v
```

### step 11 -  add connection to git 

```bash
git log # to see what changes have made by whom

git remote add origin & paste url of git
# to add new git url to source code 
#  origin is variable here u can change its name


git remote -v 
# to check git is added or not
```


### step 12 - git commit connection
```bash
git push origin main
# when latest commit dose not visible in git
# and to merge all changes together copy cide paste and authorise it to abstain from errors
```


### step 13 - add commit in git
```bash
git add .  # to add commit in git
git status  # to check modified files 
git commit -m "this is my first version of commit"
git log # to check latest changes if any by anybody
```


### step 14 - add new file 
```bash
git add .
git commit -m "added a new file .gitignore"
git push origin main
```


file is edited by manisha in github file 
