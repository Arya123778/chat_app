from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create a superuser with email authentication'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, help='Email address')
        parser.add_argument('--password', type=str, help='Password')

    def handle(self, *args, **options):
        User = get_user_model()
        
        email = options.get('email')
        password = options.get('password')
        
        if not email:
            email = input('Email: ')
        if not password:
            password = input('Password: ')
        
        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR(f'User with email {email} already exists'))
            return
        
        User.objects.create_superuser(email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Superuser {email} created successfully'))
