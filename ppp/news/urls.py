from django.urls import path
from .views import ArticleList, OneArticlelDetail, SearchArticleList, AddArticleList, DelArticleView, UpdateArticleView  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', ArticleList.as_view()),
    path('<int:pk>', OneArticlelDetail.as_view(), name='article'),
    path('search/', SearchArticleList.as_view(), name='search'),
    path('add/', AddArticleList.as_view(), name='add'),
    path('delete/<int:pk>', DelArticleView.as_view(), name='delete'),
    path('update/<int:pk>', UpdateArticleView.as_view(), name='update'),
]