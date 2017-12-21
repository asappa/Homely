from django.conf.urls import url

from .views import (
    CreateUserProfileView, UserProfileView,
    HomeViewSerializerView, HomeReadUpdateDeleteView,
    CreateHomeRentAPIView, HomeRentReadUpdateDelete
)

urlpatterns = [
    url(r'^create-user/$', CreateUserProfileView.as_view(), 
        name='create-user'),
    url(r'^get-user/(?P<pk>\d+)/$', UserProfileView.as_view()),
    url(r'^get-home/(?P<pk>\d+)/$', HomeReadUpdateDeleteView.as_view()),
    url(r'^create-home/$', HomeViewSerializerView.as_view()),
    url(r'^create-rent/$', CreateHomeRentAPIView.as_view()),
    url(r'^get-rent/(?P<pk>\d+)/$', HomeRentReadUpdateDelete.as_view()),

]