from django.shortcuts import  get_object_or_404
from django.template.response import TemplateResponse
import logging

from diplomapp.models import SubCategory, User, Product, Category
from diplomapp.forms import FormUserAdd

logger = logging.getLogger(__name__)

def index(request):
    logger.info(f'{request} request received')
    subcategories = SubCategory.objects.all()
    context = {
        'title': f'Главная страница дипломной работы',
        'subcategories' : subcategories,
        }
    if request.method == 'POST':
        form = FormUserAdd(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            logger.info(f'Получили {name=}, {email=}, {phone_number=}.')
            user1 = User.objects.filter(email=email).first()
            user2 = User.objects.filter(phone_number=phone_number).first()
            if not (user1 and user2):
                user = User(
                    name=name,
                    email=email,
                    phone_number=phone_number
                )
                user.save()
                logger.info(f'{user}')
                context['answer'] = 'Отправлено!'
                return TemplateResponse(request, 'diplomapp/index.html', context)
    else:
        form = FormUserAdd()
        context['form'] = form
    return TemplateResponse(request, 'diplomapp/index.html', context)

def catalog(request):
    logger.info(f'{request} request received')
    products = Product.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    context = {
        'title': 'Список товаров',
        'products' : products,
        'categories' : categories,
        'subcategories' : subcategories
        }
    return TemplateResponse(request, 'diplomapp/catalog.html', context)

def product(request, product_id):
    logger.info(f'{request} request received')
    product = get_object_or_404(Product, pk=product_id)
    subcategory = SubCategory.objects.filter(pk=product.sub_category.pk).first()
    category = Category.objects.filter(pk=subcategory.category.pk).first()
    logger.info(f'{product}')
    context = {
        'title' : f'{product.name}',
        'product' : product,
        'category' : category.name, 
        'subcategory' : subcategory.name
    }
    return TemplateResponse(request, 'diplomapp/product.html', context)

def about(request):
    logger.info(f'{request} request received')
    context = {'title' : 'О нас'}
    return TemplateResponse(request, 'diplomapp/about.html', context)

def contacts(request):
    logger.info(f'{request} request received')
    context = {'title' : 'Контакты'}
    return TemplateResponse(request, 'diplomapp/contacts.html', context)
