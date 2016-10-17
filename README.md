#This is test task for Steelkiwi


##Quicksetup

```bash
$ curl -sSL https://git.io/vPXmE | bash -s stable
```

##Setup

At first create virtual environmwnt for app:

```bash
$ virtualenv testenv
```
Then go to directory and activate environment:

```bash
$ cd testenv
$ . bin/activate
```
Clone this repo:

```bash
$ git clone https://github.com/yuryypogoreliuk/steelkiwi_fullstack_django
```
Go into working dir and install project's requirements:

```bash
$ cd steelkiwi_fullstack_django
$ pip install -r requirements.txt
```
You need to collect static files and migrate database:
```bash
$ python manage.py collectstatic
$ python manage.py migrate
```

I provide fixtures but you don't need them cause I forgot to include db.sqlite3 to .gitignore. So you can just type
```bash
$ python manage.py runserver
```
and open http://localhost:8000 in your browser.

If you want to see the live demo visit http://cl0jur3.pythonanywhere.com/

