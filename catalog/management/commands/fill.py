import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """
        Получение данных о категориях из фикстуры
        """

        with open('data/category_data.json', encoding='utf-8') as file:
            category_data = json.load(file)
        return category_data

    @staticmethod
    def json_read_products():
        """
        Получение данных о продуктах из фикстуры
        """

        with open('data/product_data.json', encoding='utf-8') as file:
            product_data = json.load(file)
        return product_data

    def handle(self, *args, **options):

        # Удаление всех продуктов и всех категорий
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание списков для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обход всех значений категорий из фикстуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        # Создание категорий в базе данных
        Category.objects.bulk_create(category_for_create)

        # Обход всех значений продуктов из фикстуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        image=product['fields']['image'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'])
            )

        # Создание продуктов в базе данных
        Product.objects.bulk_create(product_for_create)