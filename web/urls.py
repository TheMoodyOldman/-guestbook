from django.urls import path
from .views import * 

urlpatterns = [
    path('', MsgList.as_view(), name='msglist_url'),
    path('msg<int:pk>/', MsgDetail.as_view(), name='msgdetail_url'),
    path('create/', MsgCreate.as_view(), name='msgcreate_url'),
    path('msg<int:pk>/delete/', MsgDelete.as_view(), name='msgdelete_url'),
]
