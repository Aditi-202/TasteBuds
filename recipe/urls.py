from django.urls import path
from . import views

app_name = 'recipe'
urlpatterns = [
    path('create/', views.create_recipe, name='create_recipe'),
    path('update/<int:recipe_primary_key>/', views.update_recipe, name='update_recipe'),
    path('delete/<int:recipe_primary_key>/', views.delete_recipe, name='delete_recipe'),
    path('<int:recipe_primary_key>/ingredient/create/', views.create_ingredient, name="create_ingredient"),
    path('<int:recipe_primary_key>/ingredient/update/<int:ingredient_primary_key>/', views.update_ingredient, name="update_ingredient"),
    path('<int:recipe_primary_key>/ingredient/delete/<int:ingredient_primary_key>/', views.delete_ingredient, name="delete_ingredient"),
    path('<int:recipe_primary_key>/instruction/create/', views.create_instruction, name="create_instruction"),
    path('<int:recipe_primary_key>/instruction/update/<int:instruction_primary_key>/', views.update_instruction, name="update_instruction"),
    path('<int:recipe_primary_key>/instruction/delete/<int:instruction_primary_key>/', views.delete_instruction, name="delete_instruction"),
    path('', views.view_recipes, name='view_recipes'),
    path('me/', views.view_user_recipes, name="view_user_recipes"),
    path('detail/<int:recipe_primary_key>/', views.view_recipe_detail, name="view_recipe_detail"),

]