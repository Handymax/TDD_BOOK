# 使用markdown写一个轻blog

# 学习使用git Part1

### ubuntu下载git

​	apt install git即可



### 创建git repository

#### 	1.	设置git管理员

```shell
  git config --global user.name "qicai21"
  git config --global user.email "qicai21@hotmail.com"
  git config user.name
qicai21
  git config user.email
qicai21@hotmail.com
```

#### 	2.	创建repository (init)

​	cd到要创建库的文件夹下,`git init`	.

#### 	3.	添加管理(add)

​	`git add file`

​	      	![2017-10-30 01-04-35屏幕截图](/home/qicai21/图片/TyporaImage/2017-10-30 01-04-35屏幕截图.png)

#### 	4.	提交变更(commit)

先要add 变更后的文件,然后才能commit更改, 简化为`commit -a`.

#### 	5.	流程图

`git上的文件`	---更改--->	 `待上传状态文件(red)`	---add--->	`待确认变更状态文件(green)`	
---commit--->  `合并到git上的文件`	---更改--->	 `待上传状态文件(red)`	---add--->....

下边的流程图还是比较乱的.其实git主要涉及的是2方: 编辑客户端与git管理端.客户端变更后大概可以通过客户端查看到自己改了哪个文件,然后决定是否提交add(到staged), 这个状态应该就是Modified. add后管理端可以查看到新的文件,然后根据情况确认是否commit(合并)到git库中,这种状态就是staged(在台上待处理).commit了就变成了unmidified状态.  

![2017-10-30 02-08-09屏幕截图](/home/qicai21/图片/TyporaImage/2017-10-30 02-08-09屏幕截图.png)



#### 6.	git忽略文件

 [**Git忽略文件**](http://www.cnblogs.com/shangdawei/archive/2012/09/08/2676669.html)

因为有很多文件比如vim编辑的.swp,或者中途添加的某些zip,总会有些文件是我们不想git去管理的.

那么git对文件的处理通常是2个阶段,A:要不要trace,B:要不要commit.

通过.gitignore文件来生命这些不要管理的格式文件,git就得到了优化.

文章中提出了2中层级上解决的办法:

​	**设置全局gitignore_global**

​	全局的.gitignore可以通过创建~/.gitignore_global并添加到git全局配置以减少每层目录的规则重复定义。
​	使用命令`git config --global core.excludesfile ~/.gitignore_global` 即可.

- [ ] **如何创建`~/.gitignore_global`?**

      

      **当前project下的.gitignore**

       

```shell
	
    #git ignore swp file#                                                                                                                                      
  	#####################
 	*.swp      
```

```
    >>> ls -a
.  ..  .git  git1.py  .gitignore
```



7. #### 查看不同状态的文件的不同处

   git diff 命令

   -s: 查看modified状态的文件与git上的文件的不同.

   --cached: 查看staged状态文件与git上的文件的不同.

   HEAD: 	查看modified和staged与git上的文件的不同(主要用于同时有未提交变更,stage上还有提交了的变更	
   ​		文件的对比)

   

8.   #### git 分支


   git branch 命令

```bash
$git branch branchname  # create new branch with name of branchname
$git branch  # list all availible branch
$git checkout branchname # move to branchname
```

9. #### git 退回

   `$git reset --hard hd3j2 `​

#  学习使用git Part2

#### commit -amend命令

​	这个我说不太好,只知道这是用来合并同一个文件具有2个(或多个)staged状态时使用的.

#### commit reset filename

​	从stage上撤销提交,取回文件后其状态变为modified,然后继续编辑,重新提交.

reset --hard命令

​	HEAD: HEAD^^^ 接几个^,就是退回几个版本之前. 当然也可以用~n来指定退回数量.

​	id: 通过这种方式方便的将HEAD设置到指定的版本上.

log & reflog

​	log: 是当前的状况log

​	reflog: 这个库的所有的操作步骤全在这里,因为有时退回之后通过log无法再知道退回前的id,通过reflog就可以
​		查找到想要回去的版本了.





# Re-recongnization about git

**git! It just likes the save and read operation in game.** 

## usage commands:

```shell
$ git status 
$ git add .  
$ git diff --staged # review the changes we're about to commit
$ git reset HEAD .  # undo the add . operation
$ git commit -m "commit remark"
$ git log --oneline  # show the logs of commits on staged 
$ git tag #  i.e: $git tag end-of-chapter-05 then input git tag, can get a output as end-of-chapter-05

```



# Split big | mixed up repository into small one

## 拆分一个子目录为独立仓库

有人说用 filter-branch 来实现，but **now we have`subtree` integrated in git**。

```shell
# 这就是那个大仓库
.
├── GitRepository
│   ├── ContainerNoManager
│   ├── CrudeSurvey
│   ├── FirstSite
│   ├── MyFirstWeb
│   ├── MyToDoListProject
│   ├── PandasTechniques
│   ├── PythonDesignPattern
│   └── SimpleSurvey
└── superlists # 这个是一会新建的
   

$ cd GitRepository

# 把所有 `MyToDoListProject` 目录下的相关提交整理为一个新的分支 superlists
$ git subtree split -P MyToDoListProject -b superlists

# 另建一个新目录并初始化为 git 仓库
$ mkdir ../superlists
$ cd ../superlists
$ git init

# 拉取旧仓库的 superlists 分支到当前的 master 分支
$ git pull ../GitRepository superlists
```

**大功告成!**



# Push local git to github

```shell
$ git remote add origin https://github.com/Handymax/SuperListsSite.git
$ git push -u origin master
```



# Stop tracking files by regex

```shell
# supposing there are amount of files suffixed with .pyc (ie: test.ssdfa.pyc ), and the # files were alread tracking.

$ git rm --cached *.pyc # ok!

# then set the .gitignore with *pyc
```


