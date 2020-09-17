#### Setup instructions
- For this application I used python 3.6 ( if you don't have python you can download it from [Download from here](https://www.python.org/downloads/))

- I am using pipenv for the virtual enviorment, in case you don't have that. You can use virtualenv or download pipenv from [dowload pipenv](https://pypi.org/project/pipenv/)

- Once you have all the required depedency just clone the repo

- after cloning the repo navigate to server folder and run `pipenv shell` to run the virtual enviorment.

- Once you active the virtual enviorment now you need to install the project dependencies.

- To install project dependencies run `pipenv install` command from your terminal. It will install all of the required depency.

- Now to run the server you just need to run this command `python manage.py runserver` in case if you're using mac then the command should be something like this `python3 manage.py runserver`. cause by default mac comes with python version 2 and we need to work with version 3.

- incase if the server doesn't work please specify the values in `.env` file. You could find the example in demo.env file


## All the API endpoints

* /api/v1/all-vistiors/  [ for getting all the visitors]

* /api/v1/create-visitor/ [ for creating a new visitor ]

* /api/v1/all-entry/ [ for getting all the entry ]

* /api/v1/update-entry/ [ for updating the entry ]