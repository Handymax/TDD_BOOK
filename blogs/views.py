from django.shortcuts import render, redirect


def blog_home_page(request):
    return redirect('/blogs/page')


def get_blog_page(request):
    try:
        name = request.GET['name'] + '.md'

    except Exception:
        name = 'blog_index.md'

    finally:
        return render(request, 'blog_home.html', {'md_name': name})


