# singleton.py

class ConfigurationSingleton:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self.__class__._initialized:
            self._config = {}
            self._load_config("configuration.ini")
            self.__class__._initialized = True

    def _load_config(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        self._config[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"Erreur : Fichier {filename} introuvable.")

    def get(self, key, default=None):
        return self._config.get(key, default)
