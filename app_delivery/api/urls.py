from django.urls import path
from app_delivery.api import views

urlpatterns = [
    path('', views.fetch_delivery_percentage,name='get_shares_delivery_percentage'),
    path('custom/',views.fetch_custom_shares_delivery_details,name='get_custom_delivery'),
    path('deliverygreaterthanyesterday/',views.fetch_delivery_greater_than_yesterday,
            name="get delivery greater than yesterday"),
    path('deliverygreaterthanyesterday/custom/',views.fetch_custom_shares_delivery_greater_than_yesterday,
            name="custom_shares_delivery_greater_than_yesterday"),
    # ex: /polls/
    # path('', views.list_post_platforms, name='list_post_platforms'),
    # ex: /polls/5/
    # path('<pk>/', views.get_update_delete, name='get_update_platform')
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]