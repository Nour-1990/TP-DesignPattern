# Structure de classe 
from enum import Enum

class Categorie(Enum):
    ALIMENTAIRE = "Alimentaire"
    ELECTRONIQUE = "Électronique"
    VETEMENT = "Vêtement"

class Produit:
    def __init__(self, nom, prix, categorie, description):
        self.nom = nom
        self.prix = prix
        self.categorie = categorie
        self.description = description

    def __str__(self):
        return f"{self.nom} ({self.categorie.value}) - {self.prix}€\n{self.description}"

# Creation du produitbuilder
class ProduitBuilder:
    def __init__(self):
        self._nom = None
        self._prix = 0.0
        self._categorie = None
        self._description = ""

    def set_nom(self, nom: str):
        self._nom = nom
        return self

    def set_prix(self, prix: float):
        self._prix = prix
        return self

    def set_categorie(self, categorie: Categorie):
        self._categorie = categorie
        return self

    def set_description(self, description: str):
        self._description = description
        return self

    def build(self) -> Produit:
        if not all([self._nom, self._categorie]):
            raise ValueError("Nom et catégorie sont obligatoires.")
        return Produit(self._nom, self._prix, self._categorie, self._description)

# Exemple d'utilisation builder.py
if __name__ == "__main__":
    builder = ProduitBuilder()
    produit = (
        builder
        .set_nom("Fromage Bio")
        .set_prix(8.5)
        .set_categorie(Categorie.ALIMENTAIRE)
        .set_description("Un fromage de chèvre local et biologique.")
        .build()
    )

    print(produit)
    
