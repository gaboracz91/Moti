import os

from django import setup

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings.prod'
setup()

from service.models import Member
from django.contrib.auth.models import User

u1 = User.objects.create_superuser(username='Anita', email='email@email.com', password='123')
u1.save()
print('created Anita')

u2 = User.objects.create_user(username='Gabor', password='123')
u2.save()
print('created Gabor')

m = Member(user=u2, name='Gabor Racz', phone='123123', button_id=4701, should_be_contacted=True,
           email='blackspike182@gmail.com')
m.save()

print(f'User.objects.all() = {User.objects.all()!r}')
