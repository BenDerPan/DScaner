# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: settings_provider\__init__.py
__author__ = 'sanyi'

class Settings:
    no_value = object()

    def __init__(self):
        self._document = {}

    def load(self, document):
        self._document = document

    @property
    def document(self):
        return self._document

    def __getitem__(self, item):
        if not item:
            raise KeyError(item)
        result = self.get(item, self.no_value)
        if result == self.no_value:
            raise KeyError(item)
        return result

    def set(self, path, value):
        keys = path.split('.')
        data_location = self._document
        for i in range(0, len(keys) - 1):
            key = keys[i]
            if key not in data_location:
                data_location[key] = {}
            data_location = data_location[key]

        data_location[keys[-1]] = value

    def get(self, path, default=None):
        if not path:
            return default
        if not isinstance(path, (list, tuple)):
            path = path.split('.')
        try:
            result = self._document
            for part in path:
                result = result[part]

            return result
        except KeyError:
            return default


settings = Settings()