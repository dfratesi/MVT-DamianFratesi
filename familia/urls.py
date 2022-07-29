from django.urls import path
from .views import list_familia, create_familiar

app_name = 'familia'
urlpatterns = [
    path('', list_familia, name='familiares'),
    path('create/', create_familiar, name='crear-familia'),
    #path('<pk>', FamiliaDetailView.as_view(), name='familiar-detail')
]
