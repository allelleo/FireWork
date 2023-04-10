from transliterate import translit
import re


def slugify(string: str) -> str:
    return re.sub(
        r'^-+|-+$', '', re.sub(
            r'[\s_-]+', '-', re.sub(
                r'[^\w\s-]', '', translit(
                    u"" + string, "ru", reversed=True
                )
                .lower()
                .strip())))