import argparse
from itertools import count

from constants import AMINO_ACIDS
from protein import Protein

import os
from io_utils import read_fasta
import protein

from calculations import amino_acid_composition

from constants import AMINO_ACIDS

from visualization import (
    plot_amino_acid_composition,
    plot_residue_class_distribution,
    create_dashboard,
)

from calculations import (
    amino_acid_composition,
    molecular_weight,
)

from calculations import residue_class_distribution

def main():

    parser = argparse.ArgumentParser(
        description="Protein Sequence Toolkit"
    )

    parser.add_argument(
        "sequence",
        help="Protein sequence",
    )

    args = parser.parse_args()

    input_data = args.sequence

    if os.path.isfile(input_data):
        header,sequence = read_fasta(input_data)
   
    else:
        header = "User Input Sequence"

        sequence = input_data

    protein = Protein(sequence)

    print("Protein Sequence Toolkit")
    print("=" * 30)

    print()

    print("Sequence")
    print("--------")

    print(protein.get_sequence())

    print()

    print("Length")
    print("------")

    print(f"{protein.length()} amino acids")

    composition = amino_acid_composition(protein)

    print()
    print("Amino Acid Composition")
    print("----------------------")

    for aa, data in composition.items():

        if data["count"] > 0:

            print(
            f"{aa} ({AMINO_ACIDS[aa]['name']})"
            )

            print(
            f"  Count      : {data['count']}"
            )

            print(
            f"  Percentage : {data['percentage']:.2f}%"
            )

            print()

    mw = molecular_weight(protein)

    print()

    print("Molecular Weight")
    print("----------------")

    print(f"{mw:.2f} Da")

    plot_amino_acid_composition(
        composition,
            "output/amino_acid_composition.png",
    )

    print()

    classes = residue_class_distribution(composition)

    print()
    print("Residue Class Distribution")
    print("--------------------------")

    for group, data in classes.items():

        print(
            f"{group:<15}"
            f"{data['count']:>3} "
            f"({data['percentage']:.2f}%)"
        )

    print(
        "Figure saved to output/amino_acid_composition.png"
    )

    plot_residue_class_distribution(
        classes,
            "output/residue_class_distribution.png",
    )

    print(
        "Figure saved to output/residue_class_distribution.png"
    )

    create_dashboard(
        protein,
        composition,
        classes,
        mw,
        header,
        "output/protein_dashboard.png",
    )

    print("Dashboard saved to output/protein_dashboard.png")

if __name__ == "__main__":
    main()