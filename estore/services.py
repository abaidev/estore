from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.db import connection

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)

# check for db table in DB, otherwise throws migration errors
# even first migrate command throws Exceptions without it
def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()


def get_all_object_list(model):
    obj_list = []
    query_key = str(model._meta.model_name) + '_LIST'
    table_name = model._meta.db_table
    isTable = db_table_exists(table_name)
    if isTable and query_key in cache:
        obj_list = cache.get(query_key)
    elif isTable and query_key not in cache:
        obj_list = model.objects.all()
        cache.set(query_key, obj_list, timeout=CACHE_TTL)
    return obj_list


def get_object_cache(queryset, lookup_field, lookup_field_value):
    query_key = str(queryset.model._meta.model_name) + "_DETAIL_"+ str(hash(queryset.explain()))
    table_name = queryset.model._meta.db_table
    isTable = db_table_exists(table_name)
    item = None
    if isTable and query_key in cache:
        item = cache.get(query_key)
    elif isTable and query_key not in cache:
        item = queryset.filter(**{lookup_field: lookup_field_value})
        cache.set(query_key, item, timeout=CACHE_TTL)
    return item
