from django.urls import path
from .views import chat_page,chat_with_gemini

urlpatterns = [
   
    path('', chat_page,name='chat_page'), #ui
    path('geminichat/', chat_with_gemini,name='chat_with_gemini') #api

]
