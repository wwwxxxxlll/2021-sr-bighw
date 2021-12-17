from django.urls import path
from .views import aboutus, Index, Error, Explain
from . import contribution

urlpatterns = [
    path('',Index.as_view()),
    path('about-us/',aboutus.as_view(), name='about-us'),
    path('404/',Error.as_view(), name='404'),
    path('说明/',Explain.as_view(), name='说明'),
    path('贡献/',contribution.Contribution_from, name='贡献'),
]