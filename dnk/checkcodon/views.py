from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages


from .forms import CodonFindForm, UserRegisterForm, LoginUserForm
from .models import Dnk, History


class IndexView(View):

    def get(self, request, *args, **kwargs):
        form = CodonFindForm()
        context = {'form': form}
        if request.user.is_authenticated:
            history = History.objects.filter(user__pk=request.user.pk)
            context.update({'history': history})
        return render(request, 'checkcodon/index.html', context)

    def post(self, request, *args, **kwargs):
        form = CodonFindForm(request.POST)
        context = {'form': form}
        history = History.objects.filter(user__pk=request.user.pk)
        context.update({'history': history})
        if form.is_valid():
            codon_find = form.cleaned_data['codon']
            dnk = Dnk.objects.first().dnk
            approved_codon_find = codon_find.lower() in dnk
            if approved_codon_find:
                messages.add_message(request, messages.SUCCESS, 'Последовательность найдена')
            else:
                messages.add_message(request, messages.ERROR, 'Последовательность не найдена')
            if request.user.is_authenticated:
                History.objects.create(user=request.user, codon=codon_find, approved=approved_codon_find)
                history = History.objects.filter(user__pk=request.user.pk)
                context.update({'history': history})
        return render(request, 'checkcodon/index.html', context)


def register(request):
    """ Регистрация пользователя """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.warning(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'checkcodon/index.html', {'form': form})


def login_user(request):
    """ Авторизация пользователя """
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Ошибка авторизации, проверьте свой логин и пароль')
            form = LoginUserForm()
    else:
        form = LoginUserForm()
    return render(request, 'checkcodon/index.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('index')