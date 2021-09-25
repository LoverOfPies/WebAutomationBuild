from peewee import IntegerField, DateField, Model


# Версионность
class Versioning(Model):
    version_number = IntegerField(default=0, verbose_name='Номер версии')
    date_version = DateField(verbose_name='Дата версии')
