from src.item import Item


class MixinLang:
    lang = 'EN'

    def __init__(self):
        self.__language = self.lang

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixinLang):
    pass
