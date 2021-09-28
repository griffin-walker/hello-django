from django.urls import path

from . import views

kwargs = {"text_to_render" : "different"}
urlpatterns = [
    path(route='blah', view=views.index, name='index'), # http://localhost:8000/polls/blah
    path(route='', view=views.index, name='index', kwargs=dict(text_to_render="different")),
]