from django.urls import path, include

# from rest_framework.routers import DefaultRouter

from core import views


# router = DefaultRouter()
# router.register('tags', views.TagViewSet)
# router.register('ingredients', views.IngredientViewSet)
# router.register('recipes', views.RecipeViewSet)

# app_name = 'recipe'

urlpatterns = [
    path('', views.index, name='index'),
    path('baea-nests', views.baea_nests, name='baea-nests'),
    path('baea-surveys', views.baea_surveys, name='baea-surveys'),
    path('buowl-habitat', views.buowl_habitat, name='buowl-habitat'),
    path('buowl-surveys', views.buowl_surveys, name='buowl-surveys'),
    path('raptor-nests', views.raptor_nests, name='raptor-nests'),
    path('raptor-surveys', views.raptor_surveys, name='raptor-surveys'),
    path('gbh-rookeries', views.gbh_rookeries, name='gbh-rookeries'),
    path('linear-projects', views.gbh_rookeries, name='linear-projects'),
]
