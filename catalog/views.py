from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Part, Brand


def catalog_view(request):
    """Главная страница каталога"""
    parts = Part.objects.filter(is_active=True)

    # Получаем параметры фильтрации
    brand_id = request.GET.get('brand')
    category = request.GET.get('category')
    search = request.GET.get('search')

    # Фильтр по бренду
    if brand_id and brand_id != '':
        try:
            parts = parts.filter(brand_id=int(brand_id))
        except ValueError:
            pass

    # Фильтр по категории
    if category and category != '':
        parts = parts.filter(category=category)

    # Поиск по артикулу или названию
    if search and search != '':
        parts = parts.filter(
            Q(article__icontains=search) | Q(name__icontains=search)
        )

    # Пагинация
    paginator = Paginator(parts, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    brands = Brand.objects.all()

    context = {
        'page_obj': page_obj,
        'brands': brands,
        'selected_brand': brand_id if brand_id else '',
        'selected_category': category if category else '',
        'search_query': search if search else '',
    }
    return render(request, 'catalog/catalog.html', context)


def part_detail(request, part_id):
    """Страница товара"""
    part = get_object_or_404(Part, id=part_id, is_active=True)
    return render(request, 'catalog/part_detail.html', {'part': part})