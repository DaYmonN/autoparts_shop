from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Brand(models.Model):
    """Марка автомобиля"""
    name = models.CharField('Название марки', max_length=50, unique=True)
    logo = models.ImageField('Логотип', upload_to='brands/', blank=True, null=True)
    order = models.IntegerField('Порядок сортировки', default=0)

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Part(models.Model):
    """Автозапчасть"""
    # Категории запчастей
    CATEGORY_CHOICES = [
        ('engine', 'Двигатель'),
        ('transmission', 'Трансмиссия'),
        ('brake', 'Тормозная система'),
        ('suspension', 'Подвеска'),
        ('electrics', 'Электрика'),
        ('body', 'Кузовные детали'),
        ('filters', 'Фильтры'),
        ('oil', 'Масла и жидкости'),
    ]

    article = models.CharField('Артикул', max_length=50, unique=True)
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Марка авто', related_name='parts')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.IntegerField('На складе', default=0, validators=[MinValueValidator(0)])
    image = models.ImageField('Изображение', upload_to='parts/', blank=True, null=True)
    compatibility = models.CharField('Совместимость (модели авто)', max_length=500, blank=True,
                                     help_text='Например: Toyota Camry 2007-2011')
    created_at = models.DateTimeField('Добавлен', auto_now_add=True)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.article} - {self.name}"

    def get_absolute_url(self):
        return reverse('catalog:part_detail', args=[self.id])