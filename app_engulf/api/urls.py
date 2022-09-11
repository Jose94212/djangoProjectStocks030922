from django.urls import path
from app_engulf.api import views

urlpatterns = [
    path('bull/', views.fetch_bullish_engulfing, name='fetch_bullish_engulfing')
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
