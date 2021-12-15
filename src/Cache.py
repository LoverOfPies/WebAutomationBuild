import json
import sys


def load_class(s):
    path, klass = s.rsplit('.', 1)
    __import__(path)
    mod = sys.modules[path]
    return getattr(mod, klass)


class Cache(object):
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
            self._table_info_model = load_class("src.db.models.info.TableInfo.TableInfo")
        return self._table_info_model

    def get_table_info(self, name):
        return self.get_table_info_model().select().where(self.get_table_info_model().name == name)

    def get_filter_info_model(self):
        if not self._filter_info_model:
            self._filter_info_model = load_class("src.db.models.info.FilterInfo.FilterInfo")
        return self._filter_info_model

    def get_action_info_model(self):
        if not self._action_info_model:
            self._action_info_model = load_class("src.db.models.info.ActionInfo.ActionInfo")
        return self._action_info_model

    def get_sidebar_fields(self):
        if not self._sidebar_fields:
            with open('table_info.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self._sidebar_fields = data['sidebar_fields']
        return self._sidebar_fields

    def get_model_by_name(self, name):
        if not hasattr(self, name):
            model_path = self.get_table_info(name).get().path
            if model_path is None:
                return None
            setattr(self, name, load_class(model_path))
        return getattr(self, name)
