from Bio.Align import AlignInfo
from Bio import AlignIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


# file = "HA_H1_edited_forward_alignment.fasta"
# format = "fasta"
# for alignment in AlignIO.parse(file, format):
#     print(alignment)

# alignment = AlignIO.read("db/HA/alignments/HA_H7_edited_forward_alignment.fasta", "fasta")

# summary_align = AlignInfo.SummaryInfo(alignment)

# consensus = summary_align.dumb_consensus(threshold= 0.9, ambiguous= "N")
# print(consensus)

def create_consensus_sequence(alignment_file, id, description):
    x= id.split("_")
    alignment = AlignIO.read(alignment_file, "fasta")
    summary_align = AlignInfo.SummaryInfo(alignment)
    consensus= summary_align.dumb_consensus(threshold= 0.9, ambiguous="N")
    consensus_sequence = SeqRecord(Seq(consensus), id= id, description= description)
    SeqIO.write(consensus_sequence, "./db/" + x[0] + "/consensus_sequences/" + id + "_CS.fasta", "fasta")
    

# HA consensus sequences: 
create_consensus_sequence("db/HA/alignments/HA_H1_edited_forward_alignment.fasta", "HA_H1_Forward", "HA H1 forward consensus sequence")
create_consensus_sequence("db/HA/alignments/HA_H1_edited_reverse_alignment.fasta", "HA_H1_Reverse", "HA H1 reverse consensus sequence")
create_consensus_sequence("db/HA/alignments/HA_H3_edited_forward_alignment.fasta", "HA_H3_Forward", "HA H3 forward consensus sequence")
create_consensus_sequence("db/HA/alignments/HA_H3_edited_reverse_alignment.fasta", "HA_H3_Reverse", "HA H# reverse consensus sequence")
create_consensus_sequence("db/HA/alignments/HA_H5_edited_forward_alignment.fasta", "HA_H5_Forward", "HA H5 forward consensus sequence")
create_consensus_sequence("db/HA/alignments/HA_H5_edited_reverse_alignment.fasta", "HA_H5_Reverse", "HA H5 reverse consensus sequence")
create_consensus_sequence("db/HA/alignments/HA_H7_edited_forward_alignment.fasta", "HA_H7_Forward", "HA H7 forward consensus sequence")
create_consensus_sequence("db/HA/alignments/HA_H7_edited_reverse_alignment.fasta", "HA_H7_Reverse", "HA H7 reverse consensus sequence")
create_consensus_sequence("db/HA/alignments/HA_H9_edited_forward_alignment.fasta", "HA_H9_Forward", "HA H9 forward consensus sequence")
create_consensus_sequence("db/HA/alignments/HA_H9_edited_reverse_alignment.fasta", "HA_H9_Reverse", "HA H9 forward consensus sequence")

# MP consensus sequences 
create_consensus_sequence("db/MP/alignments/MP_H1_edited_forward_alignment.fasta", "MP_H1_Forward", "MP H1 forward consensus sequence")
create_consensus_sequence("db/MP/alignments/MP_H1_edited_reverse_alignment.fasta", "MP_H1_Reverse", "MP H1 reverse consensus sequence")
create_consensus_sequence("db/MP/alignments/MP_H3_edited_forward_alignment.fasta", "MP_H3_Forward", "MP H3 forward consensus sequence")
create_consensus_sequence("db/MP/alignments/MP_H3_edited_reverse_alignment.fasta", "MP_H3_Reverse", "MP H3 reverse consensus sequence")
create_consensus_sequence("db/MP/alignments/MP_H5_edited_forward_alignment.fasta", "MP_H5_Forward", "MP H5 forward consensus sequence")
create_consensus_sequence("db/MP/alignments/MP_H5_edited_reverse_alignment.fasta", "MP_H5_Reverse", "MP H5 reverse consensus sequence")
create_consensus_sequence("db/MP/alignments/MP_H7_edited_forward_alignment.fasta", "MP_H7_Forward", "MP H7 forward consensus sequence")
create_consensus_sequence("db/MP/alignments/MP_H7_edited_reverse_alignment.fasta", "MP_H7_Reverse", "MP H7 reverse consensus sequence")
create_consensus_sequence("db/MP/alignments/MP_H9_edited_forward_alignment.fasta", "MP_H9_Forward", "MP H9 forward consensus sequence")
create_consensus_sequence("db/MP/alignments/MP_H9_edited_reverse_alignment.fasta", "MP_H9_Reverse", "MP H9 reverse consensus sequence")

# NA consensus sequences 
create_consensus_sequence("db/NA/alignments/NA_H1_edited_forward_alignment.fasta", "NA_H1_Forward", "NA H1 forward consensus sequence")
create_consensus_sequence("db/NA/alignments/NA_H1_edited_reverse_alignment.fasta", "NA_H1_Reverse", "NA H1 reverse consensus sequence")
create_consensus_sequence("db/NA/alignments/NA_H3_edited_forward_alignment.fasta", "NA_H3_Forward", "NA H3 forward consensus sequence")
create_consensus_sequence("db/NA/alignments/NA_H3_edited_reverse_alignment.fasta", "NA_H3_Reverse", "NA H3 reverse consensus sequence")
create_consensus_sequence("db/NA/alignments/NA_H5_edited_forward_alignment.fasta", "NA_H5_Forward", "NA H5 forward consensus sequence")
create_consensus_sequence("db/NA/alignments/NA_H5_edited_reverse_alignment.fasta", "NA_H5_Reverse", "NA H5 reverse consensus sequence")
create_consensus_sequence("db/NA/alignments/NA_H7_edited_forward_alignment.fasta", "NA_H7_Forward", "NA H7 forward consensus sequence")
create_consensus_sequence("db/NA/alignments/NA_H7_edited_reverse_alignment.fasta", "NA_H7_Reverse", "NA H7 reverse consensus sequence")
create_consensus_sequence("db/NA/alignments/NA_H9_edited_forward_alignment.fasta", "NA_H9_Forward", "NA H9 forward consensus sequence")
create_consensus_sequence("db/NA/alignments/NA_H9_edited_reverse_alignment.fasta", "NA_H9_Reverse", "NA H9 reverse consensus sequence")

# NS consensus sequences
create_consensus_sequence("db/NS/alignments/NS_H1_edited_forward_alignment.fasta", "NS_H1_Forward", "NS H1 forward consensus sequence")
create_consensus_sequence("db/NS/alignments/NS_H1_edited_reverse_alignment.fasta", "NS_H1_Reverse", "NS H1 reverse consensus sequence")
create_consensus_sequence("db/NS/alignments/NS_H3_edited_forward_alignment.fasta", "NS_H3_Forward", "NS H3 forward consensus sequence")
create_consensus_sequence("db/NS/alignments/NS_H3_edited_reverse_alignment.fasta", "NS_H3_Reverse", "NS H3 reverse consensus sequence")
create_consensus_sequence("db/NS/alignments/NS_H5_edited_forward_alignment.fasta", "NS_H5_Forward", "NS H5 forward consensus sequence")
create_consensus_sequence("db/NS/alignments/NS_H5_edited_reverse_alignment.fasta", "NS_H5_Reverse", "NS H5 reverse consensus sequence")
create_consensus_sequence("db/NS/alignments/NS_H7_edited_forward_alignment.fasta", "NS_H7_Forward", "NS H7 forward consensus sequence")
create_consensus_sequence("db/NS/alignments/NS_H7_edited_reverse_alignment.fasta", "NS_H7_Reverse", "NS H7 reverse consensus sequence")
create_consensus_sequence("db/NS/alignments/NS_H9_edited_forward_alignment.fasta", "NS_H9_Forward", "NS H9 forward consensus sequence")
create_consensus_sequence("db/NS/alignments/NS_H9_edited_reverse_alignment.fasta", "NS_H9_Reverse", "NS H9 reverse consensus sequence")

# NP consensus sequences 
create_consensus_sequence("db/NP/alignments/NP_H1_edited_forward_alignment.fasta", "NP_H1_Forward", "NP H1 forward consensus sequence")
create_consensus_sequence("db/NP/alignments/NP_H1_edited_reverse_alignment.fasta", "NP_H1_Reverse", "NP H1 reverse consensus sequence")
create_consensus_sequence("db/NP/alignments/NP_H3_edited_forward_alignment.fasta", "NP_H3_Forward", "NP H3 forward consensus sequence")
create_consensus_sequence("db/NP/alignments/NP_H3_edited_reverse_alignment.fasta", "NP_H3_Reverse", "NP H3 reverse consensus sequence")
create_consensus_sequence("db/NP/alignments/NP_H5_edited_forward_alignment.fasta", "NP_H5_Forward", "NP H5 forward consensus sequence")
create_consensus_sequence("db/NP/alignments/NP_H5_edited_reverse_alignment.fasta", "NP_H5_Reverse", "NP H5 reverse consensus sequence")
create_consensus_sequence("db/NP/alignments/NP_H7_edited_forward_alignment.fasta", "NP_H7_Forward", "NP H7 forward consensus sequence")
create_consensus_sequence("db/NP/alignments/NP_H7_edited_reverse_alignment.fasta", "NP_H7_Reverse", "NP H7 reverse consensus sequence")
create_consensus_sequence("db/NP/alignments/NP_H9_edited_forward_alignment.fasta", "NP_H9_Forward", "NP H9 forward consensus sequence")
create_consensus_sequence("db/NP/alignments/NP_H9_edited_reverse_alignment.fasta", "NP_H9_Reverse", "NP H9 reverse consensus sequence")

# PA consensus sequences 
create_consensus_sequence("db/PA/alignments/PA_H1_edited_forward_alignment.fasta", "PA_H1_Forward", "PA H1 forward consensus sequence")
create_consensus_sequence("db/PA/alignments/PA_H1_edited_reverse_alignment.fasta", "PA_H1_Reverse", "PA H1 reverse consensus sequence")
create_consensus_sequence("db/PA/alignments/PA_H3_edited_forward_alignment.fasta", "PA_H3_Forward", "PA H3 forward consensus sequence")
create_consensus_sequence("db/PA/alignments/PA_H3_edited_reverse_alignment.fasta", "PA_H3_Reverse", "PA H3 reverse consensus sequence")
create_consensus_sequence("db/PA/alignments/PA_H5_edited_forward_alignment.fasta", "PA_H5_Forward", "PA H5 forward consensus sequence")
create_consensus_sequence("db/PA/alignments/PA_H5_edited_reverse_alignment.fasta", "PA_H5_Reverse", "PA H5 reverse consensus sequence")
create_consensus_sequence("db/PA/alignments/PA_H7_edited_forward_alignment.fasta", "PA_H7_Forward", "PA H7 forward consensus sequence")
create_consensus_sequence("db/PA/alignments/PA_H7_edited_reverse_alignment.fasta", "PA_H7_Reverse", "PA H7 reverse consensus sequence")
create_consensus_sequence("db/PA/alignments/PA_H9_edited_forward_alignment.fasta", "PA_H9_Forward", "PA H9 forward consensus sequence")
create_consensus_sequence("db/PA/alignments/PA_H9_edited_reverse_alignment.fasta", "PA_H9_Reverse", "PA H9 reverse consensus sequence")

# PB1 consensus sequences 
create_consensus_sequence("db/PB1/alignments/PB1_H1_edited_forward_alignment.fasta", "PB1_H1_Forward", "PB1 H1 forward consensus sequence")
create_consensus_sequence("db/PB1/alignments/PB1_H1_edited_reverse_alignment.fasta", "PB1_H1_Reverse", "PB1 H1 reverse consensus sequence")
create_consensus_sequence("db/PB1/alignments/PB1_H3_edited_forward_alignment.fasta", "PB1_H3_Forward", "PB1 H3 forward consensus sequence")
create_consensus_sequence("db/PB1/alignments/PB1_H3_edited_reverse_alignment.fasta", "PB1_H3_Reverse", "PB1 H3 reverse consensus sequence")
create_consensus_sequence("db/PB1/alignments/PB1_H5_edited_forward_alignment.fasta", "PB1_H5_Forward", "PB1 H5 forward consensus sequence")
create_consensus_sequence("db/PB1/alignments/PB1_H5_edited_reverse_alignment.fasta", "PB1_H5_Reverse", "PB1 H5 reverse consensus sequence")
create_consensus_sequence("db/PB1/alignments/PB1_H7_edited_forward_alignment.fasta", "PB1_H7_Forward", "PB1 H7 forward consensus sequence")
create_consensus_sequence("db/PB1/alignments/PB1_H7_edited_reverse_alignment.fasta", "PB1_H7_Reverse", "PB1 H7 reverse consensus sequence")
create_consensus_sequence("db/PB1/alignments/PB1_H9_edited_forward_alignment.fasta", "PB1_H9_Forward", "PB1 H9 forward consensus sequence")
create_consensus_sequence("db/PB1/alignments/PB1_H9_edited_reverse_alignment.fasta", "PB1_H9_Reverse", "PB1 H9 reverse consensus sequence")

# PB2 consensus sequences 
create_consensus_sequence("db/PB2/alignments/PB2_H1_edited_forward_alignment.fasta", "PB2_H1_Forward", "PB2 H1 forward consensus sequence")
create_consensus_sequence("db/PB2/alignments/PB2_H1_edited_reverse_alignment.fasta", "PB2_H1_Reverse", "PB2 H1 reverse consensus sequence")
create_consensus_sequence("db/PB2/alignments/PB2_H3_edited_forward_alignment.fasta", "PB2_H3_Forward", "PB2 H3 forward consensus sequence")
create_consensus_sequence("db/PB2/alignments/PB2_H3_edited_reverse_alignment.fasta", "PB2_H3_Reverse", "PB2 H3 reverse consensus sequence")
create_consensus_sequence("db/PB2/alignments/PB2_H5_edited_forward_alignment.fasta", "PB2_H5_Forward", "PB2 H5 forward consensus sequence")
create_consensus_sequence("db/PB2/alignments/PB2_H5_edited_reverse_alignment.fasta", "PB2_H5_Reverse", "PB2 H5 reverse consensus sequence")
create_consensus_sequence("db/PB2/alignments/PB2_H7_edited_forward_alignment.fasta", "PB2_H7_Forward", "PB2 H7 forward consensus sequence")
create_consensus_sequence("db/PB2/alignments/PB2_H7_edited_reverse_alignment.fasta", "PB2_H7_Reverse", "PB2 H7 reverse consensus sequence")
create_consensus_sequence("db/PB2/alignments/PB2_H9_edited_forward_alignment.fasta", "PB2_H9_Forward", "PB2 H9 forward consensus sequence")
create_consensus_sequence("db/PB2/alignments/PB2_H9_edited_reverse_alignment.fasta", "PB2_H9_Reverse", "PB2 H9 reverse consensus sequence")










 






