# encoding: utf-8

from django.core.exceptions import ValidationError
from django.forms.models import modelform_factory
from haystack.forms import SearchForm
from nx.models import Note,Need

class NeedsSearchForm(SearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()


class NotesSearchForm(SearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()


BaseNoteForm = modelform_factory(Note, fields=["username", "phone_number","address", "donation_type",
                                               "new", "number", "photo", "description"])


BaseNeedForm = modelform_factory(Need, fields=["publisher", "publisher_phone_number", "title", "image",
                                               "body", "province", "city", "address", "contact_person", "contact_person_telephone"])

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
        title = self.cleaned_data.get("title", None)
        body = self.cleaned_data.get("body", None)
        contact_persion_telephone = self.cleaned_data.get("contact_persion_telephone", None)
        province = self.cleaned_data.get("province", None)
        city = self.cleaned_data.get("city", None)
        address = self.cleaned_data.get("address", None)
        #image = self.cleaned_data.get("image", None)

        if not title and not body:
            raise ValidationError("Either a title or body is required")
        if not contact_persion_telephone:
            raise ValidationError("Either contact_persion_telephone is required")
        if not province:
            raise ValidationError("Either province is required")
        if not city:
            raise ValidationError("Either city is required")
        if not address:
            raise ValidationError("Either address is required")
        # if not image:
        #     raise ValidationError("Either image is required")
        return self.cleaned_data
