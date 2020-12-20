from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def secret_page(request):
    return render(request, 'blog/secret_page.html', {})
