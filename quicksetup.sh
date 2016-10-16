virtualenv testenv
cd testenv
. bin/activate
git clone https://github.com/yuryypogoreliuk/steelkiwi_fullstack_django
cd steelkiwi_fullstack_django
pip install -r steelkiwi_fullstack_django/requirements.txt
python steelkiwi_fullstack_django/manage.py collectstatic
python steelkiwi_fullstack_django/manage.py migrate
python steelkiwi_fullstack_django/manage.py runserver