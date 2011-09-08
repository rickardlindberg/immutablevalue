class ImmutableValue(object):

    def __init__(self, **kwargs):
        for key in self.FIELDS:
            object.__setattr__(self, key, self.FIELDS[key])
        for key in kwargs:
            if key not in self.FIELDS:
                raise ValueError()
            object.__setattr__(self, key, kwargs[key])
        self.validate()

    def validate(self):
        pass

    def where(self, **kwargs):
        new_values = {}
        for key in self.FIELDS:
            new_values[key] = getattr(self, key)
        for key in kwargs:
            new_values[key] = kwargs[key]
        return self.__class__(**new_values)

    def __setattr__(self, name, value):
        raise ValueError()

    def __delattr__(self, name):
        raise ValueError()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for key in self.FIELDS:
            if getattr(self, key) != getattr(other, key):
                return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return "%s<%s>" % (self.__class__.__name__, ", ".join(
            "%s=%s" % (key, getattr(self, key)) for key in self.FIELDS
        ))
