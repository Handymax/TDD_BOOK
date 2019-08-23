import random
import os
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, warn_only
from superlists import settings


REPO_URL = 'https://github.com/Handymax/TDD_BOOK.git'


CREATE_USER_SCRIPT = """
db = db.getSiblingDB('%s');
if (db.auth('qicai21', '5233') == 0) {
    db.createUser(
        {
            user: 'qicai21',
            pwd: '5233',
            roles: [
                { role: 'readWrite', db: '%s' },
            ]
        }
    )
}
""" % (env.host, env.host)


def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latset_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()


def _get_latset_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run(f'git reset --hard {current_commit}')


def _update_virtualenv():
    if not exists('virturalenv/pip3'):
        run('python3.7 -m venv virtualenv')
    run('./virtualenv/bin/pip3 install -r requirements.txt')


def _create_or_update_dotenv(EMAIL_PASSWORD):
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host}')
    append('.env', f'EMAIL_PASSWORD={os.environ.get("EMAIL_PASSWORD")}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz1234567890', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')


def _update_static_files():
    run('./virtualenv/bin/python3.7 manage.py collectstatic --noinput')


def _update_database():
    try:
        _check_mongo_server_or_restart()
    except ValueError as e:
        print(e)
        return

    _check_user_exist_or_create()
    _migrate_database()


def _check_mongo_server_or_restart():
    with warn_only():
        mongod_pid = None
        for i in range(5):
            mongod_pid = run('pgrep mongod', capture=True)
            if mongod_pid:
                print('mongodb server running checked.')
                break
            else:
                if i == 5:
                    raise ValueError('mongo server can not start up!')
                run('mongod --fork')


def _check_user_exist_or_create():
    admin_name = os.environ.get('ADMIN_NAME')
    admin_pwd = os.environ.get('ADMIN_PWD')
    run(f'mongo 127.0.0.10:27010/admin --username {admin_name} --password {admin_pwd} \
--eval \"{CREATE_USER_SCRIPT}\"')


def _migrate_database():
    # check mongodb contains related db_names makemigrations
    for app in settings.INSTALLED_APPS:
        if not app.startswith('django.contrib'):
            run(f'./virtualenv/bin/python3.7 manage.py \
makemigrations {app} --noinput')

    run('./virtualenv/bin/python3.7 manage.py migrate --noinput')

