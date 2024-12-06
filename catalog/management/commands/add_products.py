from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_on_create(name='Настольные игры', description='Игры для компании')

        products = [
            {'name': 'Монополия', 'description': 'Игра связонной с экономикой для компании', 'image': '',
             'price': 1500, 'created_at': '2020-10-02 12:12:12', 'updated_at': '2021-01-14 11:11:11',
             'category': category},
            {'name': 'Мафия', 'description': 'Игра для компании', 'image': '',
             'price': 500, 'created_at': '2015-03-11 13:13:13', 'updated_at': '2019-12-12 10:10:10',
             'category': category}
        ]
        for product_in_data in products:
            product, created = Product.objects.get_on_create(**product_in_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {product.name}'))
