from django.urls.conf import path

from accounts.views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup' )
]
