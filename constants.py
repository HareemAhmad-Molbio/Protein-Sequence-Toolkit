"""
Biological constants used throughout the Protein Sequence Toolkit.

These data are reused by multiple analysis modules
including molecular weight, amino acid composition,
hydrophobicity analysis, pI estimation, and future tools.
"""

AMINO_ACIDS = {

    "A": {
        "name": "Alanine",
        "three_letter": "Ala",
        "mass": 89.09,
        "group": "Hydrophobic",
        "charge": "Neutral",
        "aromatic": False,
    },

    "R": {
        "name": "Arginine",
        "three_letter": "Arg",
        "mass": 174.20,
        "group": "Positive",
        "charge": "Positive",
        "aromatic": False,
    },

    "N": {
        "name": "Asparagine",
        "three_letter": "Asn",
        "mass": 132.12,
        "group": "Polar",
        "charge": "Neutral",
        "aromatic": False,
    },

    "D": {
        "name": "Aspartic Acid",
        "three_letter": "Asp",
        "mass": 133.10,
        "group": "Negative",
        "charge": "Negative",
        "aromatic": False,
    },                                  

    "C": {
        "name": "Cysteine",
        "three_letter": "Cys", 
        "mass": 121.16,
        "group": "Polar",
        "charge": "Neutral",
        "aromatic": False,
    },

    "E": {
        "name": "Glutamic Acid",
        "three_letter": "Glu",
        "mass": 147.13,
        "group": "Negative",
        "charge": "Negative",
        "aromatic": False,
    },      

    "Q": {
        "name": "Glutamine",
        "three_letter": "Gln",
        "mass": 146.15,
        "group": "Polar",
        "charge": "Neutral",
        "aromatic": False,
    },  

    "G": {
        "name": "Glycine",
        "three_letter": "Gly",
        "mass": 75.07,
        "group": "Hydrophobic",
        "charge": "Neutral",
        "aromatic": False,
    },

    "H": {
        "name": "Histidine",
        "three_letter": "His",
        "mass": 155.16,
        "group": "Positive",
        "charge": "Positive",
        "aromatic": True,
    },

    "I": {
        "name": "Isoleucine",
        "three_letter": "Ile",
        "mass": 131.17,
        "group": "Hydrophobic",
        "charge": "Neutral",
        "aromatic": False,
    },

    "L": {
        "name": "Leucine",
        "three_letter": "Leu",
        "mass": 131.17,
        "group": "Hydrophobic",
        "charge": "Neutral",
        "aromatic": False,
    },

    "K": {
        "name": "Lysine",
        "three_letter": "Lys",
        "mass": 146.19,
        "group": "Positive",
        "charge": "Positive",
        "aromatic": False,
    },  

    "M": {
        "name": "Methionine",
        "three_letter": "Met",
        "mass": 149.21,
        "group": "Hydrophobic",
        "charge": "Neutral",
        "aromatic": False,
    },

    "F": {
        "name": "Phenylalanine",
        "three_letter": "Phe",
        "mass": 165.19,
        "group": "Hydrophobic",
        "charge": "Neutral",
        "aromatic": True,
    },

    "P": {
        "name": "Proline",
        "three_letter": "Pro",
        "mass": 115.13,
        "group": "Hydrophobic",
        "charge": "Neutral",
        "aromatic": False,
    },

    "S": {
        "name": "Serine",
        "three_letter": "Ser",
        "mass": 105.09,
        "group": "Polar",
        "charge": "Neutral",
        "aromatic": False,
    },

    "T": {
        "name": "Threonine",
        "three_letter": "Thr",
        "mass": 119.12,
        "group": "Polar",
        "charge": "Neutral",
        "aromatic": False,
    },

    "W": {
        "name": "Tryptophan",
        "three_letter": "Trp",
        "mass": 204.23,
        "group": "Hydrophobic",
        "charge": "Neutral",
        "aromatic": True,
    },

    "Y": {
        "name": "Tyrosine",
        "three_letter": "Tyr",
        "mass": 181.19,
        "group": "Polar",
        "charge": "Neutral",
        "aromatic": True,
    },

    "V": {
        "name": "Valine",
        "three_letter": "Val",
        "mass": 117.15,
        "group": "Hydrophobic",
        "charge": "Neutral",
        "aromatic": False,
    },

}       

# Set of valid one-letter amino acid codes
VALID_AMINO_ACIDS = set(AMINO_ACIDS.keys())

HYDROPHOBIC = {
    "A", "V", "I", "L", "M",
    "F", "W", "P", "G"
}

POLAR = {
    "S", "T", "N", "Q", "C", "Y"
}

POSITIVE = {
    "K", "R", "H"
}

NEGATIVE = {
    "D", "E"
}

AROMATIC = {
    "F", "W", "Y"
}

GROUP_COLORS = {
    "Hydrophobic": "#4E79A7",   # Blue
    "Polar": "#59A14F",         # Green
    "Positive": "#F28E2B",      # Orange
    "Negative": "#E15759",      # Red
}

# Molecular weight of water (Da)
WATER_MASS = 18.015