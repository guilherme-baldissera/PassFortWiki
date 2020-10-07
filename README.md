# PassFortWiki

## Requirements to execute the project
- python 3.7 (or higher version)
- Django 3.1.1 and djangorestframework 3.11.1 (Both are inside requirements.txt)


## To run the project locally Execute the following commands
- `./manage.py makemigrations`
- `./manage.py migrate`
- `./manage.py runserver` (run by default into the port 8000) 

## To run tests
- `./manage.py test`

## Observations
- The database used is sqlite3, but this can be easily change in the setting.py file
- database will be empty but it's easy to add data through admin ui.
- to access the admin it's necessary create a user with the following command : `./manage.py createsuperuser`
- Access with the [link](http://127.0.0.1:8000/admin/)

## Requirements to run the project inside the Docker
- docker [To install docker](https://docs.docker.com/engine/install/ubuntu/)

## To run the project using docker
- `docker build -t passfort .`
- `docker run -p 8080:8080 passfort`
