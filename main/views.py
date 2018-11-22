from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import *
from .forms import *


def login_view(request):
    if request.user.is_authenticated:
        return redirect(main)
    context = {}
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(main)

    context["form"] = form

    return render(request, 'main/login.html', context)


@login_required(login_url='/login/')
def logout_view(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def main(request):
    context = {}
    context["goods"] = Good.objects.all()
    return render(request, 'main/all_goods.html', context)


@login_required(login_url='/login/')
@permission_required('main.add_good', raise_exception=True)
def add_good(request):
    context = {}

    form = GoodForm()

    if request.method == "POST":
        form = GoodForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(main)

    context["form"] = form

    return render(request, 'main/add_good.html', context)


@login_required(login_url='/login/')
@permission_required('main.view_good', raise_exception=True)
def sold(request, good_id):
    context = {}
    good = get_object_or_404(Good, id=good_id)
    context["good"] = good
    form = GoodSoldForm()

    if request.method == "POST":
        form = GoodSoldForm(request.POST)
        if form.is_valid():
            qty = form.cleaned_data["qty"]
            if qty > good.qty or qty < 0:
                context["message"] = f"Введите число больше 0 и меньше текущего количества ({good.qty})"
            else:
                good.qty = good.qty - qty
                good.save()
                return redirect(main)
    context["form"] = form

    return render(request, 'main/sold.html', context)


@login_required(login_url='/login/')
@permission_required('main.change_good', raise_exception=True)
def edit_good(request, good_id):
    context = {}
    good = get_object_or_404(Good, id=good_id)
    context["good"] = good

    form = GoodForm(instance=good)

    if request.method == "POST":
        form = GoodForm(request.POST, instance=good)
        if form.is_valid():
            form.save()
            return redirect(main)

    context["form"] = form

    return render(request, 'main/edit_good.html', context)


@login_required(login_url='/login/')
@permission_required('main.delete_good', raise_exception=True)
def delete_good(request, good_id):
    context = {}
    good = get_object_or_404(Good, id=good_id)
    context["good"] = good

    if request.method == "POST":
        if "yes" in request.POST:
            good.delete()
        return redirect(main)

    return render(request, 'main/delete_good.html', context)


@login_required(login_url='/login/')
@permission_required('main.add_good', raise_exception=True)
def good_is_coming(request, good_id):
    context = {}
    good = get_object_or_404(Good, id=good_id)
    if not good.status.name == 'Нет в наличии':
        return redirect(main)
    good.status = Status.objects.get(name='Ожидает поступления')
    good.save()
    context["good"] = good
    return redirect(main)
