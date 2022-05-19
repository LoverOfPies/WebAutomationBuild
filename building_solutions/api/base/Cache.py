from peewee import Model

from api import load_class
from api.base.MyAppException import MyAppException


class Cache(object):
    """
    Класс для кэширования объектов моделей БД и мета ифнормации проекта
    """
    _table_info_model = None
    _filter_info_model = None
    _action_info_model = None
    _sidebar_fields = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cache, cls).__new__(cls)
        return cls.instance

    def get_table_info_model(self):
        if not self._table_info_model:
            self._table_info_model = load_class("db.models.info.TableInfo.TableInfo")
        return self._table_info_model

    def get_table_info(self, name):
        return self.get_table_info_model().select().where(self.get_table_info_model().name == name)

    def get_filter_info_model(self):
        if not self._filter_info_model:
            self._filter_info_model = load_class("db.models.info.FilterInfo.FilterInfo")
        return self._filter_info_model

    def get_action_info_model(self):
        if not self._action_info_model:
            self._action_info_model = load_class("db.models.info.ActionInfo.ActionInfo")
        return self._action_info_model

    def get_sidebar_fields(self):
        if not self._sidebar_fields:
            table_info_model = self.get_table_info_model()
            self._sidebar_fields = [row.name for row in
                               table_info_model.select().where(table_info_model.show_in_sidebar == True)]
        return self._sidebar_fields

    def get_model_by_name(self, name: str) -> Model:
        if not hasattr(self, name):
            model_path = self.get_table_info(name).get().path
            if model_path is None:
                raise MyAppException("Не указан путь модели в проекте, смотрите TableInfo")
            setattr(self, name, load_class(model_path))
        return getattr(self, name)
