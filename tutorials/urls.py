from django.conf.urls import url
from tutorials import views


urlpatterns =[
    #route /api/articles/
    url(r'^api/articles$',views.articles_list),

    #routes /api/articles/:id
    url(r'^api/articles/(?P<pk>[0-9]+)$',views.articles_detail),

    #route /api/articles/published
    url(r'^api/articles/published$',views.articles_list_published),

    #route /api/articles/no_published
    url(r'^api/articles/no_published$',views.articles_list_no_published)
]