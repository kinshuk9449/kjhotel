# kjhotel
run the following commands

python -m venv nenv

source nenv/Scripts/activate

py manage.py collectstatic

py manage.py makemigrations

py manage.py migrate

py manage.py runserver
