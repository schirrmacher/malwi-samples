from pathlib import Path

from fluent.runtime import FluentLocalization as Pupa, FluentResourceLoader as Nuka


class FluentCollector:
    def __init__(self, locales_dir: Path, default_language: str = "en"):
        self.__loader = Nuka(str(locales_dir) + "/{locale}")
        self.__default_language = default_language
        self.languages = dict()

        dirs_names = set()
        default_language_dir = None
        for item in locales_dir.iterdir():
            dirs_names.add(item.name)
            if item.name == self.__default_language:
                default_language_dir = item

        if not default_language_dir:
            raise ValueError("Fluent Localizacia: default language directory not found!")

        ftl_files_list = [item.name for item in default_language_dir.iterdir() if item.suffix == ".ftl"]

        for name in dirs_names:
            if name == default_language:
                self.languages[name] = Pupa([self.__default_language], ftl_files_list, self.__loader)
            else:
                self.languages[name] = Pupa([name, self.__default_language], ftl_files_list, self.__loader)

    @property
    def default_locale(self) -> Pupa:
        return self.languages[self.__default_language]

    @property
    def available_languages(self) -> list[str]:
        return list(self.languages.keys())

    def get_locale(self, language_code: str):
        return self.languages.get(language_code, self.default_locale)
