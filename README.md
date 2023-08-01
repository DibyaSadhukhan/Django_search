# Django Search Application.
Uses a CSV File to create a database and search that database on the basis of the search term

## How to run
Create a Virtual environment on the parent directory of the folder using
```
python -m venv appenv
```
travel into the folder and install requirement.txt
```
pip install -r requirements.txt
```
migrate the databases.
```
>>> python manage.py makemigrations
>>> python manage.py makemigrations search_menu
>>> python manage.py migrate 
```
use the loader file to load the data into the models
```
python loader.py
```
run the server 
```
python manage.py runserver
```
click here to see demo 
https://github.com/DibyaSadhukhan/Django_search/blob/bd87886c3e25475edfeb7633fa23da5fbea09bef/Small%20Resturants%20-%20Google%20Chrome%202023-08-01%2011-54-52.gif
![demo](https://github.com/DibyaSadhukhan/Django_search/blob/d9752138b1fc93aced787e82aa2dbf7863842017/Small%20Resturants%20-%20Google%20Chrome%202023-07-19%2013-41-36.gif)
Updated:
![demo](https://github.com/DibyaSadhukhan/Django_search/blob/bd87886c3e25475edfeb7633fa23da5fbea09bef/Small%20Resturants%20-%20Google%20Chrome%202023-08-01%2011-54-52.gif)
