from django.contrib.auth.views import LoginView

from users_app.models import Profile
from users_app.forms import CustomLoginForm, CustomUserCreationForm
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('blog:index_page')

class ProfileDetailView(DetailView):
   model = Profile
   template_name = 'users/profile_detail.html'
   context_object_name = 'profile'

   def get_object(self, queryset=None):
       profile, created = Profile.objects.get_or_create(
           user=self.request.user
       )
       return profile

class ProfileUpdateView(UpdateView):
    template_name = 'users/profile_edit.html'
    fields = ['bio', 'social_link', 'avatar']
    success_url = reverse_lazy('blog:index_page')

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(
            user=self.request.user
        )
        return profile

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
