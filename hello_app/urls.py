from django.urls import path
from hello_app import views
from hello_app.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="hello_app/home.html",
)

urlpatterns = [
    path("", home_list_view , name = "home"),
    path("hello_app/about", views.about, name = "about"),
    path("hello_app/contact", views.contact, name ="contact"),
    path("hello_app/<name>", views.hello_there, name="hello_there"),
    path("log/", views.log_message, name="log")
]


