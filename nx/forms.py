# encoding: utf-8

from django.core.exceptions import ValidationError
from django.forms.models import modelform_factory
from haystack.forms import SearchForm
from nx.models import Note


class NotesSearchForm(SearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()


BaseNoteForm = modelform_factory(Note, fields=["username", "phone_number","address", "donation_type",
                                               "new", "number", "photo", "description"])


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
