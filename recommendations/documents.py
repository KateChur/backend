from elasticsearch_dsl import Document, Text


class RecommendationIndex(Document):
    title = Text()
    description = Text()
    foto_file = Text()

    class Index:
        name = 'products-1'
