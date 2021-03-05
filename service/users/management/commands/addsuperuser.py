from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError
from django.contrib.auth.models import User


class Command(createsuperuser.Command):
    help = 'Crate a superuser, and allow password to be provided'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--password', dest='password', default=None,
            help='Specifies the password for the superuser.',
        )

    def handle(self, *args, **options):
        password = options.get('password')
        username = options.get('username')

        if password and not username:
            raise CommandError("--username is required if specifying --password")

        super(Command, self).handle(*args, **options)

        if password:
            user = User.objects.create_superuser(username=username)
            user.set_password(password)
            user.save()