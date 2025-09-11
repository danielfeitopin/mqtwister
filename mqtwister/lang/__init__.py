from mqtwister.config import DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES
from mqtwister.utils.logging import logger
from importlib import import_module


class LanguageManager:

    language: str = ''
    messages: dict[str, str] = {}

    @classmethod
    def set_language(cls, lang: str) -> None:
        """Set the current language and load corresponding messages."""
        
        # Validate language
        if lang not in SUPPORTED_LANGUAGES:
            logger.warning(
                f"Language '{lang}' not supported. Falling back to default language '{DEFAULT_LANGUAGE}'.")
            lang = DEFAULT_LANGUAGE
            
        # Set class language
        cls.language = lang
        
        # Retrieve messages
        lang_module = import_module(f'.{lang}', package='mqtwister.lang')
        cls.messages = getattr(lang_module, 'MESSAGES', {})

    @classmethod
    def get_message(cls, key: str, *args) -> str:
        """Retrieve a message by key and format it with the provided arguments."""
        return cls.messages.get(key, '').format(*args)


def get_message(key: str, *args) -> str:
    """Convenience function to get messages using the LanguageManager."""
    return LanguageManager.get_message(key, *args)
