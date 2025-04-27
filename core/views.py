from django.shortcuts import render
from core.models import *

def home(request):
    stories = Story.objects.order_by('-id')[:4]
    last_story = stories.first()
    categories = Category.objects.all()
    holiday = Story.objects.filter(category__title='Holiday')
    context = {
        'stories': stories,
        'last_story': last_story,
        'categories': categories,
        'holiday': holiday,
    }
    return render(request, 'index.html', context)


def story_detail(request, id):
    story = Story.objects.get(id=id)
    categories = Category.objects.all()
    recents = Story.objects.order_by('-id')[:2]
    tags = Tag.objects.all()
    context = {
        'data': story,
        'categories': categories,
        'recents': recents,
        'tags': tags,
    }
    return render(request, 'single.html', context)


def about(request):
    return render(request, 'about.html')


def stories(request):
    stories = Story.objects.order_by('-id')
    categories = Category.objects.all()
    context = {
        'stories': stories,
        'categories': categories,
    }
    return render(request, 'stories.html', context)