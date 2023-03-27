from requests import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet

from users.models import CustomUser, RegistrationCode
from users.serializers import UserSerializer
from django.http import JsonResponse
from django.utils import timezone
import smtplib
from email.mime.text import MIMEText

def send_email_with_code(email, code):
    # Настройки SMTP-сервера и учетных данных
    smtp_server = 'smtp.ethereal.email'
    smtp_port = 587
    smtp_user = 'myra76@ethereal.email'
    smtp_password = 'yb7dngrpmVC1s753bc'

    # Формируем сообщение
    message = MIMEText(f'Your registration code is {code}')
    message['Subject'] = 'Registration Code'
    message['From'] = smtp_user
    message['To'] = email

    # Отправляем сообщение
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, email, message.as_string())


@api_view(['POST'])
def send_registration_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            reg_code = RegistrationCode(email=email)
            reg_code.save()
            send_email_with_code(email, reg_code)
            # Отправить регистрационный код на указанный email
            print(reg_code)
            return JsonResponse({'key': 'value'}, status=200)
        else:
            return JsonResponse({'key': 'value'}, status=400)


@api_view(['POST'])
def register_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    code = request.data.get('code')
    username = request.data.get('username')

    # Проверяем, существует ли код регистрации
    try:
        registration_code = RegistrationCode.objects.get(code=code)
    except RegistrationCode.DoesNotExist:
        return JsonResponse({'key': 'value'}, status=400)

    # Проверяем, не истек ли срок действия кода регистрации
    if registration_code.expires_at < timezone.now():
        return JsonResponse({'key': 'value'}, status=400)

    if CustomUser.objects.filter(email=email).exists() or CustomUser.objects.filter(username=username).exists():
        return JsonResponse({'key': 'value'}, status=400)

    # Создаем нового пользователя с указанным email и паролем, связанным с кодом регистрации
    registration_code.create_new_user_with_code(email=email, password=password, username=username)

    return JsonResponse({'key': 'value'}, status=200)


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
