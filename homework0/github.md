# 标签 <br>
### 列出标签
git tag
### 打标签V1.1
git tag -a v1.1 -m "v1.1版本上线"  
### 显示v1.1的信息
git show v1.1     
### 上传到远程     
git push origin v1.1  
### 上传多个标签
git push origin --tags  

# 版本回退
### 回退到上一个版本
git reset --hard HEAD^
### 回退到上两个版本
git reset --hard HEAD^^
### 回退到指定ID的版本
git reset --hard <ID>

# 分支
### 查看分支
git branch -a
### 创建分支b1
git branch b1
### 切换到分支b1
git checkout b1
### 上传分支b1
git push --set-upstream origin b1
### 合并分支b1到master
git checkout master
git merge b1
### 删除分支b1
git branch -d b1
### 删除分支后更新到远程
git push origin :b1
