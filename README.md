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
