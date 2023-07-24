from django.views.generic import CreateView
from .forms import UserAccountCreationForm
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(CreateView):
    form_class = UserAccountCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


