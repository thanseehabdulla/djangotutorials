from django.conf.urls import url
from django.urls import include

from .resources import NoteResource

note_resource = NoteResource()
urlpatterns = [

    url(r'^api/', include(note_resource.urls)),
]
