from django.db import models
from django.core.validators import MaxLengthValidator, FileExtensionValidator

# from solo.models import SingletonModel

from .utils import upload_favicon



# class Settings(SingletonModel):
#     title = models.CharField('Meta Title', max_length=100, blank=True, null=True, help_text='до 100 символов')
#     description = models.TextField('Meta Description', validators=[MaxLengthValidator(150)], blank=True, null=True, help_text='до 150 символов')
#     telegram = models.CharField('Telegram', max_length=100, blank=True, null=True, help_text='до 100 символов')
#     email = models.EmailField('Email', max_length=100, blank=True, null=True, help_text='до 100 символов')
#     favicon_ico = models.FileField('favicon (.ico)', upload_to=upload_favicon, validators=[FileExtensionValidator(['ico'])], blank=True, null=True)
#     favicon_png = models.ImageField('favicon (.png)', upload_to=upload_favicon, validators=[FileExtensionValidator(['png'])], blank=True, null=True)

#     def __str__(self) -> str:
#         return 'Настройки'

#     class Meta:
#         verbose_name = "Настройки"

