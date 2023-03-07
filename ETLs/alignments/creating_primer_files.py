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
# #reverse
# reverse_primers("GTAGAAACAAGGTCGTTTTTAAACTATTC", "PB2_Reverse_2.3", "PB2 reverse primer")
# reverse_primers("CGAATAATTTAAAAACGACCTTGAA", "PB2_End_1.1", "Sanger Sequencing end primer, position 2297 into noncoding region")


# #PB1 primers:
# #forward 
# forward_primers("AGCAAAAGCAGGCAAACCATTT", "PB1_Forward_1.2", "PB1 forward primer")
# forward_primers("TCAATCCGACATTACTTTTCTTAA", "PB1_Begining_1.1", "PB1 Sanger Sequencing begining primer, positions 1 through 33")
# forward_primers("GAAACTGAGAACTCAAATACCTG", "PB1_Middle_1.1", "PB1 Sanger Sequencing middle primer, positions 1084 to 1111")
# #reverse
# reverse_primers("AGAAACAAGGCATTTTTTCATGAAGGA", "PB1_Reverse_2.3", "PB1 reverse primer")
# reverse_primers("CATGAAGGACAAGCCAAATTC", "PB1_End-1.1", "PB1 Sanger Sequencing end prime 1, positions 2273 to 2300")
# reverse_primers("ATGAAGGACAAGCCAAATTC", "PB1_End_1.2", "PB1 Sanger Sequencing end primer 2, positions 2273 to 2299")


# #PA primers:
# # forward
# forward_primers("GCAAAAGCAGGTACTGATYCAAA", "PA_Forward_1.4", "PA forward primer, mixed base")
# # reverse
# reverse_primers("GGACAGTATGGATAGCAAATAGTAGCA", "PA_Reverse_2.4", "PA reverse primer")


# #HA primers: 
# # forward: 
# forward_primers("AGCAAAAGCAGGGGATAATTCTATTAAC", "HA_Forward_1.6", "HA forward primer 1")
# forward_primers("CAAAAGCAGGGGGAAAACAAAAGAA", "HA_Forward_1.7", "HA forward primer 2")
# forward_primers("AGCAAAAGCAGGGGATAATAAAAACAAC", "HA_Forward_1.8_Brisbane", "HA forward primer, Brisbane 2007 sequence specific")
forward_primers("GGAAAACAAAAGCAACAAAAATGAAGGC", "HA_Forward_1.9", "HA forward primer 3 H1 specific")
forward_primers("AGGGGATAATTCTATTAACCATGAAGACT", "HA_Forward_1.10", "HA forward primer 4 H3 specific")
# # reverse
# reverse_primers("CAAGGGTGTTTTTCTCATGATTCTGAA", "HA_Reverse_2.3", "HA reverse primer")
# reverse_primers("GAAACAAGGGTGTTTTTCCTTATATTTCTG", "HA_Reverse_2.4_Brisbane", "HA reverse primer, Brisbane 2007 sequence specific")
reverse_primers("CTACATTGTAGAGACCCATTAGAGCAC", "HA_Reverse_2.5", "HA revrrse primer 2 H1 specific")
reverse_primers("AATGTTGCATCTAATGTTGCCCTTTTG", "HA_Reverse_2.6", "HA reverse primer 3 H3 specific")


# #NP primers: 
# # forward
# forward_primers("GCAGGGTWGATAATCACTCA", "NP_Forward_1.5", "NP forward primer, mixed base")
# # reverse
# reverse_primers("GATCAGTAGAAACAAGGGTATTTTTT", "NP_Reverse_2.3", "NP reverse primer")


# #NA primers: 
# # forward 
# forward_primers("ATGAATCCAAASCAAAAGATAATAACV", "NA_Forward_1.2", "NA internal forward primer, mixed base")
# # reverse
# reverse_primers("CGCATATTAGTAGAAACAAGGAGTT", "NA_Reverse_2.1", "NA enhanced reverse primer, includes part of noncoding region and enchanced 5' prime tail")


# #MP primers: 
# # forward 
# forward_primers("AGCAGCAAAAGCAGGTAGATATTGAAA", "MP_Forward_1.1", "MP forward primer")
# # reverse
# reverse_primers("AGACAGGATCAGTAGAAACAAGGTAGTT", "MP_Reverse_2.1", "MP reverse primer")


# #NS primers: 
# # forward
# forward_primers("GCAAAAGCAGGGTGACAAA", "NS_Forward_1.2", "NS forward primer")
# forward_primers("ATGGATTCCCACACTGTGT", "NS_Forward_1.3_Brisbane", "NS forward primer, Brisbane 2007 sequence specific")
# # reverse
# reverse_primers("GATCAGTAGAAACAAGGGTGTT", "NS_Reverse_2.1", "NS reverse primer")




