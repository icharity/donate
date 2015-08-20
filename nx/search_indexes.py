from haystack import indexes

from .models import Note, Need

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
    validate = indexes.BooleanField(model_attr='validate')
    status = indexes.BooleanField(model_attr='status')
    type = indexes.CharField(model_attr='type')

    def get_model(self):
        return Note


class NeedIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # BaseNeedForm = modelform_factory(Need, fields=["publisher", "publisher_phone_number", "image",
    #                                             "address", "contact_person", "contact_person_telephone", "description"])
    publisher = indexes.CharField(model_attr='publisher')
    publisher_phone_number = indexes.CharField(model_attr='publisher_phone_number')
    image = indexes.CharField(model_attr='image')
    address = indexes.CharField(model_attr='address')
    contact_person = indexes.CharField(model_attr='contact_person')
    contact_person_telephone = indexes.CharField(model_attr='contact_person_telephone')
    description = indexes.CharField(model_attr='description')
    type = indexes.CharField(model_attr='type')

    def get_model(self):
        return Need
