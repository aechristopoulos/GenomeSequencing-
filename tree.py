# Importing necessary libraries
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Phylo import PhyloXML

# Read the sequences and align
align = AlignIO.read("db/HA/tree_alignments/HA_H1_edited_NCR_alignment.fasta", "fasta")

# Calculate the distance matrix
calculator = DistanceCalculator('identity')
distMatrix = calculator.get_distance(align)

# Creating a DistanceTreeConstructor object
constructor = DistanceTreeConstructor()

# Construct the phlyogenetic tree using UPGMA algorithm
UPGMATree = constructor.upgma(distMatrix)


# Draw the phlyogenetic tree
Phylo.draw(UPGMATree)

# Printing the phlyogenetic tree using terminal
Phylo.draw_ascii(UPGMATree)



# # Construct the phlyogenetic tree using NJ algorithm
# NJTree = constructor.nj(distMatrix)

# # Draw the phlyogenetic tree
# Phylo.draw(NJTree)

# # Printing the phlyogenetic tree using terminal
# Phylo.draw_ascii(NJTree)

#Convert alignment from .fasta to "relaxed Phylip" format
# AlignIO.convert("db/HA/tree_alignments/HA_H1_edited_NCR_alignment.fasta", "fasta", "db/HA/relaxed_phylip_files/HA_H1_NCR.phy", "phylip-relaxed")


# cmdline = PhymlCommandline(input="db/HA/relaxed_phylip_files/HA_H1_NCR.phy", datatype="nt", model="HKY85", alpha="e", bootstrap=100)
# out_log, err_log = cmdline()
