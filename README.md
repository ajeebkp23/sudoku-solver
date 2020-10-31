# How to run sudoku-solver

## clone
`git clone https://github.com/ajeebkp23/sudoku-solver`

## install django

`cd </path/to/>sudoku-solver/`

`cd solver0/`

`pip install -r requirements.txt`

## Run server
`DJANGO_SETTINGS_MODULE=djangoserver python djangoserver.py runserver  --noreload`
### OR
`PYTHONPATH=. DJANGO_SETTINGS_MODULE=djangoserver django-admin.py runserver  --noreload`

Visit

http://localhost:8000/

And click solve button

## where to get some sudoku puzzles

Get from 

sudoku.com or websudoku.com

You can enter output of programs in above sites to verify. Or there are other good sudoku solvers online to verify.

## Know issues

* Only solves simple/easy sudoku
* Django single file server doesn't reload properly
