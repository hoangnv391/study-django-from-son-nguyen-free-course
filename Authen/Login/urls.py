from django.urls import path
from .views import IndexClass, LoginClass, ViewUser, view_product, AddPost

app_name = 'Login'
urlpatterns = [
    path('', IndexClass.as_view(), name='Index'),
    path('login/', LoginClass.as_view(), name='Login'),
    path('userview/', ViewUser.as_view(), name='ViewUser'),
    path('view-product/', view_product, name='view-product'),
    path('add-post/', AddPost.as_view(), name='add-post')
]