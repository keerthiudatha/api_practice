from django.urls import path
from apis.v1 import views
urlpatterns = [
    path("get_books",views.all_books),
    path("post_books",views.add_books),
    path("edit_books",views.edit_books),
    path("put_books",views.put_books),
    path("delete_books",views.delete_books),
    path("one_books/<int:auth>",views.one_books)
]