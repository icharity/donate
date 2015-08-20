from haystack import indexes

from .models import Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    number = indexes.IntegerField(model_attr='number')
    image = indexes.CharField(model_attr='get_image_url')
    price = indexes.IntegerField(model_attr='price')
    phone_number = indexes.IntegerField(model_attr='phone_number')

    def get_model(self):
        return Note