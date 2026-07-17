def read_fasta(filepath):
    """
    Read a protein sequence and FASTA header.

    Returns
    -------
    tuple
        (header, sequence)
    """

    header = None
    sequence = []

    with open(filepath, "r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):

                header = line[1:].strip()

                continue

            sequence.append(line)

    return header, "".join(sequence)