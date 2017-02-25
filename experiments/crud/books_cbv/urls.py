from django.conf.urls import url, include
# from books_cbv.views import (BookList,
from .views import (BookList,
                    BookCreate,
                    BookUpdate,
                    BookDelete)
urlpatterns = [
  url(r'^$', BookList.as_view(), name='book_list'),
  url(r'^list$', BookList.as_view(), name='book_list'),
  url(r'^new$', BookCreate.as_view(), name='book_new'),
  url(r'^edit/(?P<pk>\d+)$', BookUpdate.as_view(), name='book_edit'),
  url(r'^delete/(?P<pk>\d+)$', BookDelete.as_view(), name='book_delete'),
]
