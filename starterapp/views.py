from django.shortcuts import render, redirect

# Create your views here.

def frontpage(request):
    return render(request, "frontpage.html")


def diary(request):
    diary_content = request.POST.get('diary', '') if request.method == 'POST' else ''
    return render(request, 'diary.html', {'diary': diary_content})