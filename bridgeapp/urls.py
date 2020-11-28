from django.urls import path
from bridgeapp.veiws import(
    blog_post_detail_page,
    blog_post_list_page,
)


urlpatterns = [
    path('', blog_post_list_page, name='words'),
    path('<str:slug>/', blog_post_detail_page),
    ]
