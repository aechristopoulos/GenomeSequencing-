from Bio.Align import AlignInfo
from Bio import AlignIO


alignment = AlignIO.parse("db\HA\alignments\HA_H1_edited_forward_alignment.fasta", "fasta")

summary_align = AlignInfo.SummaryInfo(alignment)

consensus = summary_align.dumb_consensus(threshold= 0.9)


