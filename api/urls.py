from django.urls import path,include

from .views import books_list,books_details,Index,login1,Registration
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register('books',BooksViewSet, basename="books")

urlpatterns = [
    path('api/',include(router.urls)),
    path('index/',Index,name='booklist'),
#     path('books')
    path('book_list/',books_list),
    path('book_list/<int:pk>/',books_details ),
    # path('regis/', UserViewSet.as_view()),
    path('login/',login1,name='login' ),
    path('registration/',Registration,name='registration' ),
    # path('book_update/<int:pk>/',updateBook ),
    # path('book-delete<int:pk>',deleteBook)
]
