from django.urls import include, path
from rest_framework import routers
from employeetest.emp import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'userdetails', views.userdetails)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('userdetails/', views.userdetails.as_view(), name="userdetails"),
    path('addauthuser/', views.addauthuser.as_view(), name="addauthuser"),
    path('addemployee/', views.addemployee.as_view(), name="addemployee"),
]
