<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

def register(request):

    if request.method == 'POST': # This is a POST Request
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # Grab the username that is submitted for now
            messages.success(request, f'Account created for {username}!')
            return redirect('login')

    else:    # This is not a POST Request. We will just create a form

        form = UserRegisterForm()

    return render(request, 'users/UserRegister.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/Userprofile.html', context)
=======
# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

def signup(response):
    form = UserCreationForm()
    return render(response, 'signup.html', {'form':form})


class UserUpdateView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'update.html'

    # This keeps users from accessing the profile of other users.
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=user.id)

class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('home')
    template_name = 'change_password.html'

class UserPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'reset_password.html'
>>>>>>> dd8e683bf902422332c15d70d55d3d53b3553e2d
