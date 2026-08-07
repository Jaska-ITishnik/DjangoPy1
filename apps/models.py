from django.db.models.base import Model
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, EmailField


class Student(Model):
    class Grade(TextChoices):
        ONE = "1_grade", "1 - Sinf"
        TWO = "2_grade", "2 - Sinf"
        THREE = "3_grade", "3 - Sinf"
        FOUR = "4_grade", "4 - Sinf"
        FIVE = "5_grade", "5 - Sinf"
        SIX = "6_grade", "6 - Sinf"
        SEVEN = "7_grade", "7 - Sinf"
        EIGHT = "8_grade", "8 - Sinf"
        NINE = "9_grade", "9 - Sinf"

    class Status(TextChoices):
        ACTIVE = "active", "✅Faol"
        INACTIVE = "inactive", "❌Nofaol"

    fullname = CharField("To'liq ismi", max_length=50)
    grade = CharField(choices=Grade.choices)  # noqa
    email = EmailField(max_length=50, unique=True)
    status = CharField(choices=Status.choices)  # noqa
