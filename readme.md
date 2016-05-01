# Todo Console Application


> This is simply python application that runs inside the terminal
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
$ virtualenv venv
$ . venv/bin/activate
$ pip install --editable .
```
Run the app by typing:

```sh
$ todo
```