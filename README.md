Django simple project 
==============
---
### python version  3.11.4 <br>
*run this command in terminal or CMD*
```commandline
python3 -V
```
**if you have version older than 3.11.4 you can go to *[python.org](www.python.org)* and get suitable version.**

---

## steps to run this project (*windows*):
 - open CMD in path you want to download repo on it 
 - git this repo in your device
 - create python virtual environment
 - active the virtual environment
 - install the modules and requires pakages
 - apply migrations files to create database 
 - run django server
```commandline
    $: git clone repo-link
    $: cd repo-folder-name
    $: python -m venv venv
    $: venv\Scripts\activate
    $: pip intall requirements.txt
    $: python manage.py migrate
    $: python manage.py runserver
```

## steps to run this project (*linux*):
 - open terminal in directory you want to git repo on it 
 - git this repo in your device
 - create python virtual environment
 - active the virtual environment
 - and run django server
```commandline
    $: git clone repo-link
    $: cd repo-folder-name
    $: python3 -m venv venv
    $: source venv\bin\activate
    $: pip intall requirements.txt
    $: python manage.py migrate
    $: python manage.py runserver
```
|     Folder |                           Description                            |
|-----------:|:----------------------------------------------------------------:|
|       core |            contains settings files and main root url             |
|      posts | contains every thing about posts (db models, tables, views, urls |
|      media |            contain media files (images, pdf, ...erc)             |
| migrations |  contains db tables files that allow django to create database   |
|  templates |                      contains (html) files                       |
|     static |                  contains ( css, Js, img) files                  |

