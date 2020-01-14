alter_dict = dict(
    zh="zh_CN",
    zh_cn="zh_CN",
    en_us="en_US",
    en="en_US",
    en_UK="en_US",
)

alter_dict['zh-cn'] = 'zh_CN'


class Item:
    def __init__(self, **kwargs):
        """
        Item(zh_CN="语言", en_US="Language")

        :param kwargs:
        """
        self.values = kwargs

    def get(self, lang, default):
        value = self.values.get(lang, None)
        if value is not None:
            return value
        alter = alter_dict.get(lang, default)
        value = self.values.get(alter, "Unknown Language")
        return value

    def __get__(self, instance: "I18N", owner):
        lang = instance.target_lang
        default = instance.default
        return self.get(lang, default)


class I18N:
    default = "en_US"
    available_languages = {
        "简体中文": "zh_CN",
        "English": "en_US",
    }

    def __init__(self, lang=None):
        if lang is None:
            lang = self.default
        self.target_lang = lang

    @property
    def list(self):
        return set(self.available_languages.keys())

    lang = Item(zh_CN="简体中文", en_US="English")
    unknown_error = Item(zh_CN="未知错误", en_US="Unknown Error")
    no_session_login = Item(zh_CN="未登录", en_US="Please Login")
    invalid_company_id = Item(zh_CN="错误公司ID: <%s>", en_US="Wrong Company ID <%s>")
    nonexistent_id = Item(zh_CN="不存在的ID: <%s>", en_US="Nonexistent ID <%s>")
    no_record = Item(zh_CN="没有满足条件的记录", en_US="No such a record")
    duplicated_mongo_key = Item(zh_CN="重复的项`%s`", en_US="Duplicated item`%s`")
