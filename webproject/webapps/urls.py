from django.urls import path
from webapps import views
app_name="movie"
urlpatterns = [
    path('',views.index,name="index"),
    path('webapps/<int:web_id>',views.detail,name='detail'),
    path('add/',views.addmovie,name='addmovie'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]