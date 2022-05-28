from uuid import uuid4

import dramatiq
from dramatiq import Message
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView

from django_settings.dramatiqconfig import backend
from .forms import UserAuthenticationForm, UserRegistrationForm
from .serializers import ImageDataSerializer


def index(request):
    return render(request, template_name="phyto_backend/home.html")


class SegmentationView(APIView):

    def post(self, request, format=None):
        serializer = ImageDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        img = serializer.validated_data.get("image")
        m = Message(
            message_id=uuid4().hex,
            queue_name=settings.SEGMENTATION_QUEUE,
            actor_name=settings.SEGMENTATION_TASK,
            args=(img, ), kwargs={}, options={}
        )
        dramatiq.get_broker().enqueue(m)
        broker_res = m.get_result(backend=backend, block=True)
        return Response(broker_res)


# класс-контроллер отвечает за логику веб-приложения при взаимодействии
# с формой регистрации
class RegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = "registration/register.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # заходим под пользователем после регистрации,
        # чтобы он не проходил аутентификацию снова
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class AuthenticateView(LoginView):
    form_class = UserAuthenticationForm
