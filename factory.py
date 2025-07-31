from enum import Enum

# Classes et enumeration
class Unite(Enum):
    GRAMME = "g"
    MILLI_GRAMME = "mg"
    LITRE = "L"


class Element:
    def __init__(self, nom: str, valeur: float, unite: Unite):
        self.nom = nom
        self.valeur = valeur
        self.unite = unite

    def __str__(self):
        return f"{self.nom} : {self.valeur} {self.unite.value}"


class Ingredient(Element):
    pass


class Allergene(Element):
    pass


class Additif(Element):
    pass
# classe elements et factory 
class ElementType(Enum):
    INGREDIENT = "INGREDIENT"
    ALLERGENE = "ALLERGENE"
    ADDITIF = "ADDITIF"


class ElementFactory:
    @staticmethod
    def creer_element(element_type: ElementType, nom: str, valeur: float, unite: Unite) -> Element:
        if element_type == ElementType.INGREDIENT:
            return Ingredient(nom, valeur, unite)
        elif element_type == ElementType.ALLERGENE:
            return Allergene(nom, valeur, unite)
        elif element_type == ElementType.ADDITIF:
            return Additif(nom, valeur, unite)
        else:
            raise ValueError(f"Type d'élément non reconnu : {element_type}")


# exemple de test factory 
if __name__ == "__main__":
    factory = ElementFactory()

    sucre = factory.creer_element(ElementType.INGREDIENT, "Sucre", 5.0, Unite.GRAMME)
    gluten = factory.creer_element(ElementType.ALLERGENE, "Gluten", 0.01, Unite.GRAMME)
    e330 = factory.creer_element(ElementType.ADDITIF, "E330", 0.005, Unite.MILLI_GRAMME)

    print(sucre)
    print(gluten)
    print(e330)



