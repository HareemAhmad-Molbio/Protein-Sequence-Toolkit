from constants import AMINO_ACIDS, VALID_AMINO_ACIDS


class Protein:
    """
    Represents a protein sequence and provides
    basic information about the protein.
    """

    def __init__(self, sequence):
        """
        Initialize a Protein object.

        Parameters
        ----------
        sequence : str
            Protein sequence.
        """

        self.sequence = sequence.upper()

        self.validate()

    def validate(self):

        if not self.sequence:

            raise ValueError(
                "Protein sequence cannot be empty."
            )

        invalid = set(self.sequence) - VALID_AMINO_ACIDS

        if invalid:

            raise ValueError(
                f"Invalid amino acid(s): {', '.join(sorted(invalid))}"
            )

    def length(self):
        """
        Return protein length.
        """

        return len(self.sequence)

    def get_sequence(self):
        """
        Return protein sequence.
        """

        return self.sequence
    
    def amino_acid_composition(self):
        """
        Calculate amino acid composition.

        Returns
        -------
        dict
            Amino acid counts.
        """

        composition = {}

        for amino_acid in AMINO_ACIDS:
            composition[amino_acid] = self.sequence.count(amino_acid)

        return composition