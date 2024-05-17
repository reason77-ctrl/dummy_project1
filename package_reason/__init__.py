import collections

class my_default_dict(collections.UserDict):
    def __init__(self, default_factory=None, *args, **kwargs):
        super().__init__(*args,**kwargs)
        if not callable(default_factory) and default_factory is not None:
            raise TypeError('first argument must be callable or None')
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        if key not in self:
            self[key] = self.default_factory()
        return self[key]