import os

import yaml


class Config:
    """
    Class for managing configuration settings.

    This class provides a simple way to manage configuration settings
    by retrieving values based on keys.

    Attributes:
        None

    Methods:
        get(key: str, default=None) -> str:
            Retrieve the value for the given key from the configuration.
            If the key is not present, return the specified default value.

    Usage:
        To access configuration settings, use Config.get(key, default).

    Example:
        Config.get("API_KEY", "default_api_key")
    """

    @classmethod
    def get(cls, key: str, default=None) -> str:
        """
        Retrieve the value for the given key from the configuration.

        Args:
            key (str): The key for the configuration setting.
            default: The default value to return if the key is not present.

        Returns:
            str: The value associated with the given key or the default value
            if the key is not present.

        Raises:
            None

        Example:
            Config.get("DB_HOST", "localhost")
        """
        if os.path.isfile(".env"):
            with open(".env", "r") as env_file:
                env_data = yaml.safe_load(env_file)
                if env_data and key in env_data:
                    return env_data[key]

        return os.environ.get(key, default)
