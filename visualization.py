import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Patch


from constants import AMINO_ACIDS, GROUP_COLORS


def plot_amino_acid_composition(
    composition,
    output_path=None,
    ax=None,
    ):
    """
    Create a publication-quality amino acid composition figure.
    """

    labels = []
    counts = []
    colors = []

    for aa, data in composition.items():

        labels.append(aa)

        counts.append(data["count"])

        group = AMINO_ACIDS[aa]["group"]

        colors.append(
            GROUP_COLORS[group]
        )

    if ax is None:

        fig, ax = plt.subplots(
            figsize=(12,6)
        )

    else:

        fig = ax.figure

    bars = ax.bar(
        labels,
        counts,
        color=colors,
        edgecolor="black",
        linewidth=0.8,
    )

    ax.set_title(
        "Amino Acid Composition",
        fontsize=16,
        fontweight="bold",
    )

    ax.set_xlabel(
        "Amino Acid",
        fontsize=12,
    )

    ax.set_ylabel(
        "Residue Count",
        fontsize=12,
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.3,
    )

    # Annotate bars
    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.2,
            f"{int(height)}",
            ha="center",
            fontsize=9,
        )
    

    legend_elements = [
        Patch(facecolor=color, label=group)
        for group, color in GROUP_COLORS.items()
    ]

    ax.legend(
        handles=legend_elements,
        title="Residue Class",
        frameon=False,
    )
    
    if output_path:

        fig.tight_layout()

        fig.savefig(
            output_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.close(fig)


def plot_residue_class_distribution(
    classes,
    output_path=None,
    ax=None,
    ):
    """
    Create a publication-quality residue class distribution
    donut chart.
    """

    labels = []
    sizes = []
    colors = []

    for group, data in classes.items():

        labels.append(
            f"{group}\n{data['percentage']:.1f}%"
        )

        sizes.append(data["count"])

        colors.append(
            GROUP_COLORS[group]
        )

    if ax is None:

        fig, ax = plt.subplots(figsize=(8, 8))

    else:

        fig = ax.figure

    ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        startangle=90,
        wedgeprops=dict(
            width=0.45,
            edgecolor="white",
        ),
    )

    ax.set_title(
        "Residue Class Distribution",
        fontsize=16,
        fontweight="bold",
    )

    if output_path:

        fig.tight_layout()

        fig.savefig(
            output_path,
            dpi=300,
            bbox_inches="tight",
        )

        plt.close(fig)

def create_dashboard(
    protein,
    composition,
    residue_classes,
    molecular_weight,
    protein_name,
    output_path,
):

    fig = plt.figure(
        figsize=(16, 10),
        dpi=300,
    )

    fig.patch.set_facecolor("#FAFAFA")

    gs = GridSpec(
        3,
        2,
        figure=fig,
        height_ratios=[2.0, 4.3, 0.4],
    )

    fig.suptitle(
        "Protein Sequence Analysis Dashboard",
        fontsize=22,
        fontweight="bold",
        y=0.999,
        color="#2F5D9F",
    )

    fig.text(
        0.5,
        0.955,
        "Research-Oriented Protein Sequence Analysis",
        ha="center",
        fontsize=12,
        color="gray",
    )

    summary_ax = fig.add_subplot(gs[0, :])

    summary_ax.axis("off")

    most_common = max(
        composition.items(),
        key=lambda item: item[1]["count"]
    )

    aa = most_common[0]

    label = f"{AMINO_ACIDS[aa]['name']} ({aa})"
    
    least_common = min(
        (
            item for item in composition.items()
            if item[1]["count"] > 0
        ),
        key=lambda item: item[1]["count"] 
    )

    least_aa = least_common[0]

    least_label = (
        f"{AMINO_ACIDS[least_aa]['name']} ({least_aa})"
    )

    cards = [

         ("Protein", protein_name),

        ("Length", f"{protein.length()} aa"),

        ("Molecular Weight", f"{molecular_weight/1000:.2f} kDa"),

        (
            "Hydrophobic",
            f"{residue_classes['Hydrophobic']['percentage']:.1f}%"
        ),

        ("Most Common", label),
        ("Least Common", least_label),
    ]



    x_positions = [0.10, 0.28, 0.40, 0.56, 0.70, 0.85]

    for (title, value), x in zip(cards, x_positions):

        summary_ax.text(

            x,

            0.55,

            f"{title}\n{value}",

            ha="center",

            va="center",

            fontsize=15,

            bbox=dict(

                boxstyle="round,pad=0.9",

                facecolor="white",

                edgecolor="gray",

            ),
        )

    left_ax = fig.add_subplot(gs[1, 0])

    right_ax = fig.add_subplot(gs[1, 1])

    plot_amino_acid_composition(
        composition,
        ax=left_ax,
    )

    plot_residue_class_distribution(
        residue_classes,
        ax=right_ax,
    )

    footer = fig.add_subplot(gs[2, :])

    footer.axis("off")

    footer.text(
        0.5,
        0.5,
        "Generated by Protein Sequence Toolkit • Version 1.0",
        ha="center",
        fontsize=10,
        color="gray",
    )

    fig.tight_layout(
        rect=[0, 0, 1, 0.94]
    )

    fig.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

   
    for ax in [left_ax, right_ax]:

        ax.spines["top"].set_visible(False)

        ax.spines["right"].set_visible(False)

    plt.close(fig)