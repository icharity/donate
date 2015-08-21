# encoding: utf-8

from django.core.exceptions import ValidationError
from django.forms.models import modelform_factory
from haystack.forms import SearchForm
from nx.models import Note,Need

class NeedsSearchForm(SearchForm):
    def no_query_found(self):
        return self.searchqueryset.filter(type='need')


class NotesSearchForm(SearchForm):
    def no_query_found(self):
        return self.searchqueryset.filter(type='note')


BaseNoteForm = modelform_factory(Note, fields=["username", "phone_number","address", "donation_type",
                                               "new", "number", "photo", "description"])


BaseNeedForm = modelform_factory(Need, fields=["publisher", "publisher_phone_number", "image",
                                                "address", "contact_person", "contact_person_telephone", "description"])

class NotesForm(BaseNoteForm):
    def clean(self):
        username = self.cleaned_data.get("username", None)
        donation_type = self.cleaned_data.get("donation_type", None)
        phone_number = self.cleaned_data.get("phone_number", None)
        address = self.cleaned_data.get("address", None)
        photo = self.cleaned_data.get("photo", None)
        description = self.cleaned_data.get("description", None)

        if not username:
            raise ValidationError("请输入用户名")
        if not donation_type:
            raise ValidationError("请输入类型")
        if not description:
            raise ValidationError("请输入描述")
        if not phone_number:
            raise ValidationError("请输入手机号码")
        if not address:
            raise ValidationError("请输入地址")
        if not photo:
            raise ValidationError("请选择照片")
        return self.cleaned_data

class NeedsForm(BaseNeedForm):
    def clean(self):
        publisher = self.cleaned_data.get("publisher", None)
        description = self.cleaned_data.get("description", None)
        contact_person_telephone = self.cleaned_data.get("contact_person_telephone", None)
        address = self.cleaned_data.get("address", None)

        if not publisher:
            raise ValidationError("请输入发布者姓名")
        if not description:
            raise ValidationError("请输入描述")
        if not contact_person_telephone:
            raise ValidationError("请输入联系人手机号码")
        if not address:
            raise ValidationError("请输入地址")
        return self.cleaned_data
