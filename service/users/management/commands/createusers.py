from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string
from random import randint
from users.models import User
from datetime import datetime


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        if options['createnewusers']:
            MAIL_SERVER = '@gmail.com'
            total = options['createnewusers']
            for _ in range(total):
                _username = get_random_string(randint(5, 15))
                newuser = User(username=_username,
                               first_name=get_random_string(randint(5, 15)),
                               last_name=get_random_string(randint(5, 15)),
                               email=_username + MAIL_SERVER,
                               birthday_year=randint(1900, datetime.now().year-18))
                newuser.save()
                print(f'Создан пользователь с ником: {newuser.username}')
        else:
            print(options)
            print(args)
            import this

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '-cnu',
            '--createnewusers',
            nargs='?',
            type=int,
            const=1,
            help='Создать нового рандомного пользователя',
        )
