from constants import AMINO_ACIDS


def amino_acid_composition(protein):
    """
    Calculate amino acid composition.

    Parameters
    ----------
    protein : Protein

    Returns
    -------
    dict
        Amino acid composition.
    """

    sequence = protein.get_sequence()

    length = protein.length()

    composition = {}

    for aa in AMINO_ACIDS:

        count = sequence.count(aa)

        percentage = (count / length) * 100

        composition[aa] = {
            "count": count,
            "percentage": percentage,
        }

    return composition


from constants import AMINO_ACIDS, WATER_MASS

def molecular_weight(protein):
    """
    Calculate protein molecular weight.

    Notes
    -----
    Protein molecular weight is calculated by summing the masses
    of all amino acid residues and subtracting the mass of one
    water molecule (18.015 Da) for each peptide bond formed.

    References
    ----------
    Lehninger Principles of Biochemistry
    ExPASy ProtParam
    """

    sequence = protein.get_sequence()

    total_mass = 0

    for aa in sequence:

        total_mass += AMINO_ACIDS[aa]["mass"]

    peptide_bonds = protein.length() - 1

    total_mass -= peptide_bonds * WATER_MASS

    return total_mass

from constants import (
    HYDROPHOBIC,
    POLAR,
    POSITIVE,
    NEGATIVE,
)

def residue_class_distribution(composition):
    """
    Calculate residue class distribution.

    Parameters
    ----------
    composition : dict
        Amino acid composition.

    Returns
    -------
    dict
        Residue class counts and percentages.
    """

    total = sum(
        data["count"]
        for data in composition.values()
    )

    classes = {
        "Hydrophobic": 0,
        "Polar": 0,
        "Positive": 0,
        "Negative": 0,
    }

    for aa, data in composition.items():

        count = data["count"]

        if aa in HYDROPHOBIC:
            classes["Hydrophobic"] += count

        elif aa in POLAR:
            classes["Polar"] += count

        elif aa in POSITIVE:
            classes["Positive"] += count

        elif aa in NEGATIVE:
            classes["Negative"] += count

    results = {}

    for group, count in classes.items():

        results[group] = {
            "count": count,
            "percentage": (count / total) * 100,
        }

    return results