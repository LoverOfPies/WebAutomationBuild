from peewee import Model, CharField


# Наследование поля код
class ClsIdExtender(Model):
    cls_id = CharField(verbose_name='Код')
