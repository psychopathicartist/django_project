from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_categories_from_cache():
    """
    Получает данные о категориях из кэша,
    если кэш пуст - получает данные из базы данных
    """

    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'categories_list'
    cache_data = cache.get(key)
    if cache_data is None:
        cache_data = Category.objects.all()
        cache.set(key, cache_data)
    return cache_data
