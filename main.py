# main.py
from singleton import ConfigurationSingleton

def main():
    config1 = ConfigurationSingleton()
    config2 = ConfigurationSingleton()

    print("URL:", config1.get("db.url"))
    print("User:", config2.get("db.user"))
    print("Les deux instances sont les mêmes ?", config1 is config2)

if __name__ == "__main__":
    main()
