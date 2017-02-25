from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.conf import settings

import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for user in settings.ADMINS:
                username = user[0].replace(' ', '')
                email = user[1]
                password = os.getenv('SLMWEBSITE_ADMIN_PASSWORD', 'admin')
                print('Creating account for %s (%s)' % (username, email))
                admin = User.objects.create_superuser(email=email,
                                                      username=username,
                                                      password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
