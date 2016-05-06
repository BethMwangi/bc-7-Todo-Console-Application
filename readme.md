# Todo Console Application


> This is a simply python application that runs inside the terminal
> enabling the users to create and keep track of their 
> to do list.

In Details the user can:


 - Create List with collection of to do items
 - Add an item to the list
 - Save items on sqlite and firebase

### Tech

The following resources were used to make this app

* [Click] - Pythonic package used to create command-line interfaces 
* [Firebase] - Cloud services platform that is used to store and sync your app's data
* [SQLAlchemy] - Python SQL toolkit 

### Installation

You need python and pip installed globally:

```sh
$ apt-get install python2.7
$ python get-pip.py
```

```sh
$ git clone https://github.com/Onikah/bc-7-Todo-Console-Application.git
$ cd bc-7-Todo-Console-Application
$ . venv/bin/activate
$ pip install -r requirements.txt
$ pip install --editable .
```

### Usage:Commands

Get Help:

```sh
$ todo --help
```

Create list:

```sh
$ todo create '<list name>'
```

Open list:

```sh
$ todo open '<list name>'
```
List specific list:

```sh
$ todo list '<list name>'
```
List all lists:

```sh
$ todo list_todos 
```

Add items to an existing list quickly:

```sh
$ todo add '<existing-list-name>' '<itemname>' 
```

Save list items to cloud:

```sh
$ todo save
```

Retrieve items from cloud storage:

```sh
$ todo sync
```
Exit listing shell that list all items:

```sh
$ q
```

Close app

```sh
$ done
```