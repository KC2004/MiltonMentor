from django.shortcuts import render
from .models import User
from .forms import CreateUserForm

# Create your views here.
def create_user(request):
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user_num = request.user
			post.save()
	else:
		form = CreateUserForm()

	return render(request, 'MentorApp/create_user.html', {'form' : form})
