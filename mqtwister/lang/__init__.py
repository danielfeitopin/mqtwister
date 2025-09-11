from mqtwister.config import DEFAULT_LANGUAGE
from mqtwister.utils.logging import logger


class LanguageManager:

    language: str = ''
    messages: dict[str, str] = {}

    @classmethod
    def set_language(cls, lang: str) -> None:
        """Set the current language and load corresponding messages."""
        cls.language = lang

        if lang == 'en':
            from .en import MESSAGES
        elif lang == 'es':
            from .es import MESSAGES
        else:
            from .en import MESSAGES  # Fallback to English
            logger.warning(
                f"Language '{lang}' not supported. Falling back to English.")

        cls.messages = MESSAGES

    @classmethod
    def get_message(cls, key: str, *args) -> str:
        """Retrieve a message by key and format it with the provided arguments."""
        return cls.messages.get(key, '').format(*args)


def get_message(key: str, *args) -> str:
    """Convenience function to get messages using the LanguageManager."""
    return LanguageManager.get_message(key, *args)
