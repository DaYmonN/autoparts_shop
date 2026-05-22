from django.core.management.base import BaseCommand
from catalog.models import Brand, Part
import random


class Command(BaseCommand):
    help = 'Генерирует тестовые запчасти'

    def handle(self, *args, **options):
        brands = Brand.objects.all()

        if not brands:
            self.stdout.write(self.style.ERROR('Сначала добавьте бренды!'))
            return

        categories = ['engine', 'transmission', 'brake', 'suspension',
                      'electrics', 'body', 'filters', 'oil']

        brand_prefixes = {
            'Toyota': 'TOY', 'Honda': 'HND', 'Nissan': 'NSS',
            'BMW': 'BMW', 'Mercedes': 'MB', 'Audi': 'AUD',
            'Hyundai': 'HYD', 'Kia': 'KIA'
        }

        part_names = {
            'engine': [
                'Двигатель в сборе', 'Головка блока цилиндров', 'Коленчатый вал',
                'Распределительный вал', 'Поршневая группа', 'Шатун', 'Масляный насос',
                'Водяной насос', 'Термостат', 'Прокладка ГБЦ', 'Ремень ГРМ',
                'Ролик натяжной', 'Клапан впускной', 'Клапан выпускной', 'Форсунка'
            ],
            'transmission': [
                'Коробка передач', 'Сцепление в сборе', 'Диск сцепления',
                'Корзина сцепления', 'Выжимной подшипник', 'Привод КПП', 'Дифференциал',
                'Шестерни КПП', 'Синхронизатор', 'Масло трансмиссионное'
            ],
            'brake': [
                'Тормозные колодки передние', 'Тормозные колодки задние',
                'Тормозной диск передний', 'Тормозной диск задний', 'Тормозной барабан',
                'Главный тормозной цилиндр', 'Рабочий тормозной цилиндр',
                'Тормозной шланг', 'Скоба суппорта', 'Тормозная жидкость'
            ],
            'suspension': [
                'Амортизатор передний', 'Амортизатор задний', 'Пружина подвески',
                'Шаровая опора', 'Рычаг подвески', 'Сайлентблок', 'Стабилизатор',
                'Стойка стабилизатора', 'Подушка двигателя', 'ШРУС внутренний', 'ШРУС наружный'
            ],
            'electrics': [
                'Стартер', 'Генератор', 'Аккумулятор', 'Свеча зажигания',
                'Катушка зажигания', 'Блок управления', 'Датчик кислорода',
                'Датчик ABS', 'Датчик коленвала', 'Лампочка LED', 'Фара головная',
                'Задний фонарь', 'Стеклоочиститель', 'Двигатель стеклоочистителя'
            ],
            'body': [
                'Капот', 'Дверь передняя', 'Дверь задняя', 'Крыло переднее',
                'Крыло заднее', 'Бампер передний', 'Бампер задний', 'Крышка багажника',
                'Зеркало боковое', 'Ручка двери', 'Молдинг', 'Стекло лобовое',
                'Стекло боковое', 'Решетка радиатора', 'Порог'
            ],
            'filters': [
                'Масляный фильтр', 'Воздушный фильтр', 'Салонный фильтр',
                'Топливный фильтр', 'Фильтр АКПП', 'Фильтр кондиционера'
            ],
            'oil': [
                'Моторное масло 5W-30', 'Моторное масло 5W-40', 'Трансмиссионное масло',
                'Тормозная жидкость DOT-4', 'Антифриз G12', 'Охлаждающая жидкость',
                'Гидроусилитель жидкость', 'Масло для АКПП'
            ]
        }

        parts_created = 0

        for brand in brands:
            prefix = brand_prefixes.get(brand.name, brand.name[:3].upper())

            for category in categories:
                names = part_names.get(category, ['Запчасть'])

                num_parts = random.randint(3, 8)
                selected_names = random.sample(names, min(num_parts, len(names)))

                for i, name in enumerate(selected_names):
                    article = f"{prefix}-{category[:3].upper()}-{random.randint(100, 999)}"

                    if category in ['engine', 'transmission']:
                        price = random.randint(5000, 50000)
                    elif category in ['suspension', 'brake']:
                        price = random.randint(2000, 15000)
                    else:
                        price = random.randint(500, 8000)


                    stock = random.randint(0, 100)


                    compatibility = f"{brand.name} {random.choice(['Camry', 'Corolla', 'Accord', 'Civic', 'X5', 'A4', 'Solaris'])} {random.randint(2005, 2020)}-{random.randint(2020, 2025)}"


                    if not Part.objects.filter(article=article).exists():
                        part = Part(
                            article=article,
                            name=name,
                            description=f"Оригинальная {name.lower()} для {brand.name}. Высокое качество, гарантия 12 месяцев.",
                            category=category,
                            brand=brand,
                            price=price,
                            stock=stock,
                            compatibility=compatibility,
                            is_active=True
                        )
                        part.save()
                        parts_created += 1
                        self.stdout.write(f"✓ Добавлена: {part.name} ({part.article}) - {part.price} ₽")

        self.stdout.write(self.style.SUCCESS(f'\n✅ Успешно добавлено {parts_created} запчастей!'))