def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("cannot divide by zero")
    return x / y


"""
steps to follow in git :
------------------------
git branch subtract
git checkout subtract
git status
git add -A
git commit -m "kkkk"
git push -u origin subtract
git checkout master
git pull origin master
git merge subtract
git push origin master
git branch -d subtract
git push origin --delete subtract
git branch -a
"""
