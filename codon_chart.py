"""
Allow other files to cleanly import codon chart

To use:

`from codon_chart import codon_chart`
 
Loads a dictionary object containing the codon charts.
Contains both codon-to-amino acid and amino acid-to-codon translations.

See codon_chart.json

"""


import json


try:
    with open("codon_chart.json", "r", encoding="utf8") as f:
        codon_chart = json.load(f)

except Exception as exc:
    codon_chart = None
    print("Failed to load codon chart: " + exc)


def get_amino(codon: str):
    """Get a mRNA codon's corresponding amino acid"""
    codon = codon.upper()
    return codon_chart["codon to amino"][codon]

def check_codon(amino=None, codon=None):
    """Check if the given codon can correspond to the given amino acid"""
    codon = codon.upper()
    amino = amino.title()
    return codon in codon_chart["possible amino codons"][amino]
