class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError


class Methods(Enum):
    token = "/api/v1/token" 