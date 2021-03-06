from datetime import date

from django.db import models
from django.core.validators import MinLengthValidator

from genMerch import globals, fields as custom_fields
from customers import choices


class Person(models.Model):
    first_name = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH)
    middle_name = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH, null=True, blank=True, default='')
    last_name = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH)

    email = models.EmailField(null=True, blank=True, unique=True)
    phone_number = custom_fields.PhoneNumberField(null=True, blank=True)

    profile_pic = models.ImageField(
        upload_to='images/customers/profile-pics/')

    city = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH)
    province = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH)
    zip_code = models.PositiveIntegerField()
    country = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH)

    sex = models.CharField(
        max_length=1, choices=choices.Sex.choices, default=choices.Sex.MALE)
    birthdate = models.DateField()
    status = models.CharField(
        max_length=1, choices=choices.Status.choices, default=choices.Status.SINGLE)

    spouse_name = custom_fields.TitleCaseCharfield(
        max_length=globals.LONG_MAX_LENGTH, null=True, blank=True, default='')
    spouse_occupation = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH, null=True, blank=True, default='')
    number_of_children = models.PositiveIntegerField(default=0)

    father_name = custom_fields.TitleCaseCharfield(
        max_length=globals.LONG_MAX_LENGTH)
    father_occupation = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH, null=True, blank=True, default='')

    mother_name = custom_fields.TitleCaseCharfield(
        max_length=globals.LONG_MAX_LENGTH)
    mother_occupation = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH, null=True, blank=True, default='')

    height = models.FloatField(verbose_name='Height (cm)')
    weight = models.FloatField(verbose_name='weight (kg)')
    religion = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH, null=True, blank=True, default='')

    def __str__(self):
        # pylint: disable=no-member
        return f'{self.id} / { self.full_name }'

    @property
    def full_name(self):
        middle_name = self.middle_name
        if middle_name:
            # pylint: disable=unsubscriptable-object
            return f'{self.first_name} {middle_name[0]}. {self.last_name}'
        return f'{self.first_name} {self.last_name}'

    @property
    def address(self):
        return f'{self.city}, {self.province} {self.country} {self.zip_code}'

    class Meta:
        db_table = "Person"


class Customer(Person):
    date_registered = models.DateField(default=date.today)
    last_modified = models.DateTimeField(auto_now=True)
    employee_id = models.PositiveIntegerField()

    class Meta:
        db_table = "Customer"
