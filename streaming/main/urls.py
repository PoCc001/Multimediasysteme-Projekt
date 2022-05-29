from django.urls import URLPattern, path
from main.views import index, login, register, streaming, settings, chat

urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('streaming', streaming, name="streaming"),
    path('settings', settings, name="settings"),
    path('chat', chat, name="chat")
]