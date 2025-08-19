from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import DocumentForm, SignupForm
from .models import Document


@login_required
def document_list(request):
    documents = Document.objects.all()
    return render(request, "files/document_list.html", {"documents": documents})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("files:login")
    else:
        form = SignupForm()
    return render(request, "files/signup.html", {"form": form})


@login_required
def upload_document(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("files:document_list")
    else:
        form = DocumentForm()
    return render(request, "files/upload.html", {"form": form})


@login_required
def user_list(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    users = User.objects.all()
    return render(request, "files/user_list.html", {"users": users})
