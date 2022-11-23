from django.urls import path
from service import views

app_name = "service"
urlpatterns = [
    path("services/", views.ServiceListView.as_view(), name="service-list"),
    path("service/add/", views.ServiceCreateView.as_view(), name="service-add"),
    path("service/<int:pk>/detail/", views.ServiceDetailView.as_view(), name="service-detail"),
    path("service/<int:pk>/update/", views.ServiceUpdateView.as_view(), name="service-update"),
    path("service/<int:pk>/delete/", views.ServiceDeleteView.as_view(), name="service-delete"),
    path("comment/<int:pk>/add/", views.CommentServiceCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentServiceDeleteView.as_view(), name="comment-delete"),
]