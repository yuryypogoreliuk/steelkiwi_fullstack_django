virtualenv testenv
cd testenv
. bin/activate
git clone https://github.com/yuryypogoreliuk/steelkiwi_fullstack_django
cd steelkiwi_fullstack_django
pip install -r requirements.txt
python manage.py collectstatic
python manage.py migrate
python manage.py runserver