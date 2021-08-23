from django.shortcuts import render, get_object_or_404
from .models import Message, ChatBox
from django.contrib.auth.models import User
from .forms import MessageForm

def MessageListView(request):
	messages = ChatBox.active.all()
	return render(request, './message/list.html', {'messages': messages,})

def ChatBoxView(request, year, id):
	messages = get_object_or_404(ChatBox, updated__year=year, id=id)

	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			message = form.save(commit=False)
			message.chatbox = ChatBox.objects.get(id=id)
			message.messager = request.user
			message.receiver = User.objects.get(id=request.POST['receiver'])
			message.save()
	else: 
		form = MessageForm()

	return render(request, './message/chatbox.html', {
		'messages': messages,
		'form': form})