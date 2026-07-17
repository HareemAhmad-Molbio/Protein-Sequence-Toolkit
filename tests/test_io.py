from io_utils import read_fasta


def test_read_albumin():

    header, sequence = read_fasta(
        "sample_data/albumin.fasta"
    )

    assert header == "Human Serum Albumin"

    assert len(sequence) > 0


def test_sequence_is_string():

    _, sequence = read_fasta(
        "sample_data/albumin.fasta"
    )

    assert isinstance(sequence, str)


def test_sequence_uppercase():

    _, sequence = read_fasta(
        "sample_data/albumin.fasta"
    )

    assert sequence.isupper()