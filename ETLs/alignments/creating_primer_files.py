from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord 

def forward_primers(primer_sequence, id, description):
    x = id.split("_")
    forward_primer = SeqRecord(Seq(primer_sequence), id = id, description = description)
    SeqIO.write(forward_primer, "./db/"+ x[0] + "/primers/" + id +"_primer.fasta", "fasta")


def reverse_primers(primer_sequence, id, description):
    x = id.split("_")
    reverse_primer = Seq(primer_sequence)
    reverse_complement = Seq(reverse_primer.reverse_complement())
    revcomp_primer = SeqRecord(Seq(reverse_complement), id = id, description = description)
    SeqIO.write(revcomp_primer, "./db/" + x[0] + "/primers/" + id +"_revcomp_primer.fasta", "fasta")


# # PB2 primers: 
# # forward
# forward_primers("AGCAAAAGCAGGTCAATTATATTCA", "PB2_Forward_1.1", "PB2 forward primer")
# forward_primers("GCAGGTCAATTATATTCAATATGGA", "PB2_Begining_1.1", "Sanger Sequencing begining primer 1, noncoding to position 6")
# forward_primers("ATTCAATATGGAAAGAATAAAAGAGC", "PB2_Begining_1.2", "Sanger Sequencing begining primer 2, noncoding to position 19")
# forward_primers("GCAACCAGGAGATTGATTC", "PB2_Middle_1.1", "Sanger Sequencing middle primer, position 1141 to 1166")
forward_primers("AGCAAAAGCAGGTCAAATATATTCA", "PB2_Forward_1.2", "PB2 foward universal NCR primer for H1, H5, H7, and H9 strains, 5' tail not included here")
forward_primers("AGCAAAAGCAGGTCAATTATATTCA", "PB2_Forward_1.3", "PB2 forward NCR primer for H3 strains, 5' tail not included here")
forward_primers("AGCAAAAGCAGGTCAAWTATATTCA", "PB2_Forward_1.4", "PB2 forward universal NCR primer, mixed base, 5' tail not included here")


# #reverse
# reverse_primers("GTAGAAACAAGGTCGTTTTTAAACTATTC", "PB2_Reverse_2.3", "PB2 reverse primer")
# reverse_primers("CGAATAATTTAAAAACGACCTTGAA", "PB2_End_1.1", "Sanger Sequencing end primer, position 2297 into noncoding region")
reverse_primers("AGTAGAAACAAGGTCGTTTTTAAAC", "PB2_Reverse_2.4", "PB2 reverse universal NCR primer, 5' tail not included here")


# #PB1 primers:
# #forward 
# forward_primers("AGCAAAAGCAGGCAAACCATTT", "PB1_Forward_1.2", "PB1 forward primer")
# forward_primers("TCAATCCGACATTACTTTTCTTAA", "PB1_Begining_1.1", "PB1 Sanger Sequencing begining primer, positions 1 through 33")
# forward_primers("GAAACTGAGAACTCAAATACCTG", "PB1_Middle_1.1", "PB1 Sanger Sequencing middle primer, positions 1084 to 1111")
forward_primers("AGCAAAAGCAGGCAAACCATTTG", "PB1_Forward_1.3", "PB1 forward universal NCR primer")

# #reverse
# reverse_primers("AGAAACAAGGCATTTTTTCATGAAGGA", "PB1_Reverse_2.3", "PB1 reverse primer")
# reverse_primers("CATGAAGGACAAGCCAAATTC", "PB1_End-1.1", "PB1 Sanger Sequencing end prime 1, positions 2273 to 2300")
# reverse_primers("ATGAAGGACAAGCCAAATTC", "PB1_End_1.2", "PB1 Sanger Sequencing end primer 2, positions 2273 to 2299")
reverse_primers("AGTAGAAACAAGGCATTTTTTCATGAAGG", "PB1_Reverse_2.4", "PB1 reverse universal NCR primer, 5' tail not included here")

# #PA primers:
# # forward
# forward_primers("GCAAAAGCAGGTACTGATYCAAA", "PA_Forward_1.4", "PA forward primer, mixed base")
forward_primers("AGCAAAAGCAGGTACTGATCCAAAAT", "PA_Forward_1.5", "PA forward NCR primer for H1, H7, and H9 strains")
forward_primers("AGCAAAAGCAGGTACTGATTCAAAATG", "PA_Forward_1.6", "PA forward NCR primer for H3 and H5 strains")
forward_primers("AGCAAAAGCAGGTACTGATYCAAAATG", "PA_Forward_1.7", "PA forward universal NCR primer, mixed base")

# # reverse
# reverse_primers("GGACAGTATGGATAGCAAATAGTAGCA", "PA_Reverse_2.4", "PA reverse primer")
reverse_primers("AGTAGAAACAAGGTACTTTTTTGGACA", "PA_Reverse_2.7", "PA reverse universal NCR primer, 5' tail not included here")


# #HA primers: 
# # forward: 
# forward_primers("AGCAAAAGCAGGGGATAATTCTATTAAC", "HA_Forward_1.6", "HA forward primer 1")
# forward_primers("CAAAAGCAGGGGGAAAACAAAAGAA", "HA_Forward_1.7", "HA forward primer 2")
# forward_primers("AGCAAAAGCAGGGGATAATAAAAACAAC", "HA_Forward_1.8_Brisbane", "HA forward primer, Brisbane 2007 sequence specific")
# forward_primers("GGAAAACAAAAGCAACAAAAATGAAGGC", "HA_Forward_1.9", "HA forward primer 3 H1 specific")
# forward_primers("AGGGGATAATTCTATTAACCATGAAGACT", "HA_Forward_1.10", "HA forward primer 4 H3 specific")
forward_primers("AGCAAAAGCAGGGGA", "HA_Forward_1.13", "HA Forward universal NCR primer, 5' tail not included here")

# # reverse
# reverse_primers("CAAGGGTGTTTTTCTCATGATTCTGAA", "HA_Reverse_2.3", "HA reverse primer")
# reverse_primers("GAAACAAGGGTGTTTTTCCTTATATTTCTG", "HA_Reverse_2.4_Brisbane", "HA reverse primer, Brisbane 2007 sequence specific")
# reverse_primers("CTACATTGTAGAGACCCATTAGAGCAC", "HA_Reverse_2.5", "HA revrrse primer 2 H1 specific")
# reverse_primers("AATGTTGCATCTAATGTTGCCCTTTTG", "HA_Reverse_2.6", "HA reverse primer 3 H3 specific")
reverse_primers("AGTAGAAACAAGGGTGTTTTT", "HA_Reverse_2.7", "HA reverse universal NCR primer, 5' tail not included here")

# #NP primers: 
# # forward
# forward_primers("GCAGGGTWGATAATCACTCA", "NP_Forward_1.5", "NP forward primer, mixed base")
forward_primers("AGCAAAAGCAGGGTAGATAATCACTCA", "NP_Forward_1.6", "NP forward universal NCR primer for strains H1, H5, H7, and H9")
forward_primers("AGCAAAAGCAGGGTWGATAATCACTCA", "NP_Forward_1.7", "NP forward universal NCR primer, mixed base")
forward_primers("AGCAAAAGCAGGGTTGATAATCACTCA", "NP_Forward_1.8", "NP forward NCR primer for H3 strains")

# # reverse
# reverse_primers("GATCAGTAGAAACAAGGGTATTTTTT", "NP_Reverse_2.3", "NP reverse primer")
reverse_primers("AGTAGAAACAAGGGTATTTTT", "NP_Reverse_2.5", "NP reverse universal NCR primer, 5' tail not included here")



# #NA primers: 
# # forward 
# forward_primers("ATGAATCCAAASCAAAAGATAATAACV", "NA_Forward_1.2", "NA internal forward primer, mixed base")
forward_primers("AGCAAAAGCAGGAGT", "NA_Forward_1.3", "NA forward NCR primer for strains H1, H3, and H9, 5' tail not included here")
forward_primers("AGCAAAAGCAGGGT", "NA_Forward_1.4", "NA forward NCR primer for strains H5 and H7, 5' tail not included here")

# # reverse
# reverse_primers("CGCATATTAGTAGAAACAAGGAGTT", "NA_Reverse_2.1", "NA enhanced reverse primer, includes part of noncoding region and enchanced 5' prime tail")
reverse_primers("AGTAGAAACAAGGAGTT", "NA_Reverse_2.2", "NA reverse NCR primer for strains H1, H3, H7, and H9, 5' tail not included here")
reverse_primers("AGTAGAAACAAGGGTGT", "NA_Reverse_2.3", "NA reverse NCR primer for H5 strains, 5' tail not included here")

# #MP primers: 
# # forward 
# forward_primers("AGCAGCAAAAGCAGGTAGATATTGAAA", "MP_Forward_1.1", "MP forward primer")
forward_primers("AGCAAAAGCAGGTAGATGTTTAAAGATGAG", "MP_Forward_1.4", "MP forward NCR primer for strains H1, H7, and H9")
forward_primers("AGCAAAAGCAGGTAGATATTGAAAGATGAG", "MP_Forward_1.5", "MP forward NCR primer for strains H3 and H5")
forward_primers("AGCAAAAGCAGGTAGATRTTKAAAGATGAG", "MP_Forward_1.6", "MP forward universal NCR primer, mixed base")
# # reverse
# reverse_primers("AGACAGGATCAGTAGAAACAAGGTAGTT", "MP_Reverse_2.1", "MP reverse primer")
reverse_primers("AGTAGAAACAAGGTAGTTTTTTACT", "MP_Reverse_2.2", "MP reverse universal NCR primer, 5' tail not included here")


# #NS primers: 
# # forward
# forward_primers("GCAAAAGCAGGGTGACAAA", "NS_Forward_1.2", "NS forward primer")
# forward_primers("ATGGATTCCCACACTGTGT", "NS_Forward_1.3_Brisbane", "NS forward primer, Brisbane 2007 sequence specific")
forward_primers("AGCAAAAGCAGGGTGACAAA", "NS_Forward_1.4", "NS forward universal NCR primer, 5' tail not included here")
# # reverse
# reverse_primers("GATCAGTAGAAACAAGGGTGTT", "NS_Reverse_2.1", "NS reverse primer")
reverse_primers("AGTAGAAACAAGGGTGTT", "NS_Reverse_2.2", "NS reverse universal NCR primer, 5' tail not included here")


