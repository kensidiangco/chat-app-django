from django.urls import path
from . import views

app_name = 'teleusap'

urlpatterns = [
	path('', views.MessageListView, name='messages'),
	path('<int:year>/<int:id>/', views.ChatBoxView, name='chat_box'),
]