from django.core.mail import send_mail


send_mail('Django mail',
          'This e-mail was sent with Django.',
          'atsou12@gmail.com',
          ['aatsou12@gmail.com'],
          fail_silently=False)