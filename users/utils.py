from enum import IntEnum


class UserGenders(IntEnum):
    FEMALE = 1
    MALE = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name.lower()) for key in cls]
