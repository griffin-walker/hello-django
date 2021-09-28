from django.http import HttpResponse


def index(request, text_to_render=None):
    if text_to_render:
        return HttpResponse(f"Hello, world. You're at the polls index. {text_to_render}")
    else:
        return HttpResponse(f"Hello, world. You're at the polls index.")