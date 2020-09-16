from django.urls import path
from . views import AllVisitor, create_visitor

urlpatterns = [
    path('all-vistiors/', AllVisitor.as_view()),
    path('create-visitor/', create_visitor),
]
