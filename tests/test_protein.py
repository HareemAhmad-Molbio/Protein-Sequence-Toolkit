from protein import Protein
import pytest


def test_valid_sequence():

    protein = Protein("ACDEFGHIKLMNPQRSTVWY")

    assert protein.length() == 20


def test_lowercase_sequence():

    protein = Protein("acdef")

    assert protein.get_sequence() == "ACDEF"


def test_invalid_sequence():

    with pytest.raises(ValueError):

        Protein("ABCD123")


def test_empty_sequence():

    with pytest.raises(ValueError):

        Protein("")


def test_sequence_storage():

    seq = "MKWVTFIS"

    protein = Protein(seq)

    assert protein.get_sequence() == seq