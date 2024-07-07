from django.contrib import admin
from django.urls import path
from app.views import List, Detail, Create, Update, Delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List.as_view(), name='list'),
    path('detail/<int:id>/', Detail.as_view(), name='detail'),
    path('create/', Create.as_view(), name='create'),
    path('update/<int:id>', Update.as_view(), name='update'),
    path('delete/<int:id>', Delete.as_view(), name='delete'),
]
