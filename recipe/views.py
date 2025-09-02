from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Category, Recipe, Ingredient, Instruction
from .forms import RecipeForm, IngredientsForm, InstructionForm

@login_required
def view_recipes(request):
    return render(request, 'recipe/view_recipes.html', {
        'title': 'Recipes',
    })

@login_required
def create_recipe(request):
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            messages.success(request, "Recipe saved successfully")
        else:
            messages.error(request, "failed to create recipe")
    else:
        form = RecipeForm()
    return render(request, 'recipe/form.html', {
        'title': 'Create Recipe',
        'form': form,
    })

@login_required
def update_recipe(request, recipe_primary_key):
    recipe = get_object_or_404(Recipe, pk=recipe_primary_key, created_by = request.user)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()
            messages.success(request, "dish updated successfully")
        else:
            messages.error(request, "failed to update dish")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/form.html', {
        'title': 'Update Recipe',
        'form': form,
    })

@login_required   #delete function not working, lets work on that later sometime.
def delete_recipe(request, recipe_primary_key):
    recipe = get_object_or_404(Recipe, pk=recipe_primary_key, created_by = request.user)
    recipe.delete()

    messages.success(request, "recipe deleted successfully")
    return redirect('core:home')

@login_required
def create_ingredient(request, recipe_primary_key):
    if request.method == 'POST':
        form = IngredientsForm(request.POST)

        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe_id = recipe_primary_key
            ingredient.save()
            messages.success(request, "ingredient created successfully")
        else:
            messages.error(request, "Failed to create the ingredient")
    else:
        form = IngredientsForm()
    return render(request, 'recipe/form.html', {
        'titel': 'Create Recipe Ingredient',
        'form': form,
    })

@login_required
def update_ingredient(request, recipe_primary_key, ingredient_primary_key):
    recipe = get_object_or_404(Recipe, pk=recipe_primary_key, created_by = request.user)
    ingredient = get_object_or_404(Ingredient, pk=ingredient_primary_key, recipe=recipe)

    if request.method == 'POST':
        form = IngredientsForm(request.POST, instance=ingredient)

        if form.is_valid():
            form.save()
            messages.success(request, "ingredient updated successfully")
        else:
            messages.error(request, "failed to update ingredient")

    else:
        form = IngredientsForm(instance=ingredient)
    return render(request, 'recipe/form.html', {
        'title': 'Update Recipe Ingredient',
        'form': form,
        'recipe': recipe,
        'ingredient': ingredient,
    })


@login_required
def delete_ingredient(request, recipe_primary_key, ingredient_primary_key):
    recipe = get_object_or_404(Recipe, pk=recipe_primary_key, created_by = request.user)
    ingredient = get_object_or_404(Ingredient, pk=ingredient_primary_key, recipe=recipe)
    ingredient.delete()

    messages.success(request, "Ingredient deleted successfully")
    return redirect('core:home')


@login_required
def create_instruction(request, recipe_primary_key):
    if request.method == 'POST':
        form = InstructionForm(request.POST)

        if form.is_valid():
            instruction = form.save(commit=False)
            instruction.recipe_id = recipe_primary_key
            instruction.save()
            messages.success(request, "instruction created successfully")
        else:
            messages.error(request, "Failed to create the instruction")
    else:
        form = InstructionForm()
    return render(request, 'recipe/form.html', {
        'titel': 'Create Recipe Instruction',
        'form': form,
    })


@login_required
def update_instruction(request, recipe_primary_key, instruction_primary_key):
    recipe = get_object_or_404(Recipe, pk=recipe_primary_key, created_by = request.user)
    instruction = get_object_or_404(Ingredient, pk=instruction_primary_key, recipe=recipe)

    if request.method == 'POST':
        form = InstructionForm(request.POST, instance=instruction)

        if form.is_valid():
            form.save()
            messages.success(request, "instruction updated successfully")
        else:
            messages.error(request, "failed to update instruction")

    else:
        form = InstructionForm(instance=instruction)
    return render(request, 'recipe/form.html', {
        'title': 'Update Recipe instruction',
        'form': form,
        'recipe': recipe,
        'instruction': instruction,
    })


@login_required
def delete_instruction(request, recipe_primary_key, instruction_primary_key):
    recipe = get_object_or_404(Recipe, pk=recipe_primary_key, created_by = request.user)
    instruction = get_object_or_404(Instruction, pk=instruction_primary_key, recipe=recipe)
    instruction.delete()

    messages.success(request, "instruction deleted successfully")
    return redirect('core:home')
