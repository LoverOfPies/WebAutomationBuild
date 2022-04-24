from peewee import IntegerField, DateField, Model, BooleanField


# Версионность
class VersioningExtender(Model):
    version_number = IntegerField(default=0, verbose_name='Номер версии')
    date_version = DateField(verbose_name='Дата последнего изменения')
    enable_version = BooleanField(verbose_name='Действующая версия', default=True)
