from django.core.management.base import BaseCommand
from catalog.models import Brand, Part


class Command(BaseCommand):
    help = 'Загружает тестовые данные'

    def handle(self, *args, **options):
        # Добавляем бренды
        brands = ['Toyota', 'Honda', 'Nissan', 'BMW', 'Mercedes', 'Audi', 'Hyundai', 'Kia']
        for name in brands:
            Brand.objects.get_or_create(name=name)

        # Добавляем запчасти
        parts_data = [
            {'article': 'TOY-001', 'name': 'Тормозные колодки передние', 'brand': 'Toyota', 'category': 'brake',
             'price': 2500, 'stock': 50},
            {'article': 'TOY-002', 'name': 'Масляный фильтр', 'brand': 'Toyota', 'category': 'filters', 'price': 450,
             'stock': 100},
            {'article': 'HND-001', 'name': 'Ремень ГРМ', 'brand': 'Honda', 'category': 'engine', 'price': 1800,
             'stock': 30},
            {'article': 'BMW-001', 'name': 'Свечи зажигания (4 шт)', 'brand': 'BMW', 'category': 'engine',
             'price': 3200, 'stock': 25},
            {'article': 'NSS-001', 'name': 'Амортизатор передний', 'brand': 'Nissan', 'category': 'suspension',
             'price': 5500, 'stock': 15},
            {'article': 'MB-001', 'name': 'Воздушный фильтр', 'brand': 'Mercedes', 'category': 'filters', 'price': 890,
             'stock': 40},
        ]

        for data in parts_data:
            brand = Brand.objects.get(name=data['brand'])
            Part.objects.get_or_create(
                article=data['article'],
                defaults={
                    'name': data['name'],
                    'brand': brand,
                    'category': data['category'],
                    'price': data['price'],
                    'stock': data['stock'],
                    'description': f'Оригинальная запчасть для {brand.name}',
                }
            )

        self.stdout.write(self.style.SUCCESS('Тестовые данные загружены!'))