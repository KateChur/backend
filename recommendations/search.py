from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'

    title = fields.TextField(attr='title')
    description = fields.TextField(attr='description')
    foto_file = fields.TextField(attr='foto_file')

    class Django:
        model = Product
