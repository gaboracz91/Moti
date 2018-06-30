from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=30)
    button_id = models.CharField(max_length=100, blank=True)
    should_be_contacted = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            send_mail('Subject: Welcome to Moti!',
                      message,
                      'messagemoti@gmail.com', [self.email], fail_silently=False)

        super(Member, self).save(*args, **kwargs)


message = """
Yay! You made the first, important step towards a conscious lifestyle change! Congratulations!
I am so happy to welcome you as a participant of the Moti Training Course!
As we have talked about it in the first session, the program consists of two important parts, one are the sessions themselves, the other one is the constant care system built around it, which is represented by the button.
You can reach your button here:
https://www.moti.herokuapp.com 
Your Username: your first name.your last name (for example: emma.kiss)
Your Password: first name.lastname+last 4 digits of the mobile number you’ve given me (for example: emma.kiss1234)
If you have any problem signing in, please contact me via e-mail: messagemoti@gmail.com Or phone: +36305137592
You’ll find all the information needed about the button once you log in, but it is actually quite simple: you push it once a day, as part of the changes you are making. If you don’t push it one day, I’m going to call you the next day to make sure everything is okay and give you a little extra support if needed.
So do your weekly challenges, push the button every day and change consciously!
I am very happy we are taking this journey together.
Trust yourself, trust the process, be patient and experience the moment.
Let’s rock this!
You will soon be getting the e-mail reminder of your first weekly challenge, have fun with it :)

Welcome to Moti!

Cheers,

Anita
"""