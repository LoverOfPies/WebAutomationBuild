from peewee import Model, CharField


# Наследование поля код
class ClsIdExtender(Model):
    cls_id = CharField(default=0, verbose_name='Код')
