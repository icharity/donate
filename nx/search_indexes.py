from haystack import indexes

from .models import Note

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    username = indexes.CharField(model_attr='username')
    phone_number = indexes.CharField(model_attr='phone_number')
    address = indexes.CharField(model_attr='address')
    donation_type = indexes.CharField(model_attr='donation_type')
    new = indexes.BooleanField(model_attr='new')
    number = indexes.IntegerField(model_attr='number')
    photo = indexes.CharField(model_attr='photo')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Note