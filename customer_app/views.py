from django.shortcuts import redirect, render

from .forms import HelpRequestForm


def help_request_view(request):
    if request.method == "POST":
        form = HelpRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = HelpRequestForm()
    return render(request, "./help_form.html", {"form": form})


def success_view(request):
    return render(request, "./success.html")
