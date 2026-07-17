from protein import Protein
from calculations import (
    amino_acid_composition,
    molecular_weight,
    residue_class_distribution,
)


protein = Protein("MKWVTFISLLFLFSSAYS")


def test_composition_total():

    composition = amino_acid_composition(protein)

    total = sum(
        aa["count"] for aa in composition.values()
    )

    assert total == protein.length()


def test_percentages():

    composition = amino_acid_composition(protein)

    total = sum(
        aa["percentage"]
        for aa in composition.values()
    )

    assert abs(total - 100) < 0.01


def test_molecular_weight():

    mw = molecular_weight(protein)

    assert mw > 0


def test_residue_classes():

    composition = amino_acid_composition(protein)

    classes = residue_class_distribution(composition)

    total = sum(
        group["count"]
        for group in classes.values()
    )

    assert total == protein.length()