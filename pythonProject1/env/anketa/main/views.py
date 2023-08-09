from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import AdvUser
from .forms import ProfileEditForm, RegisterForm


def index(request):
    template = loader.get_template('public/main.html')
    content = {}
    return HttpResponse(template.render(content, request))


class MyLoginView(LoginView):
    template_name = 'registration/login.html'


class MyLogoutView(LogoutView):
    pass


@login_required
def profile(request):
    return render(request, 'registration/profile.html')


class ProfileEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    # fields = '__all__'
    from_class = ProfileEditForm
    fields = ProfileEditForm.Meta.fields
    model = AdvUser
    template_name = 'registration/profile_edit.html'

    success_url = reverse_lazy('profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class PasswordEditView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_edit.html'
    success_url = reverse_lazy('profile')
    success_message = 'Пароль изменен'


class RegisterView(CreateView):
    model = AdvUser
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('register_done')


class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'
