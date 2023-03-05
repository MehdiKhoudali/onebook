# example/urls.py
from example.views import index, signup, logoutPage, loginPage, catalogue, book_detail, conditions, delete_comment
from django.urls import path, include

urlpatterns = [
    path('', index, name="home"),
    path('signup/', signup, name="signup"),
    path('logout/', logoutPage, name="logout"),
    path('login/', loginPage, name="login"),
    path('catalogue/', catalogue, name="catalogue"),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('conditions/', conditions, name="conditions")
]