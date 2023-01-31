from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
import custom_types



#Turning edited sequences into sequence record object to be used in alignments 
def sequence_record_objects(edited_sequence_record_information):
        forward_sequence_records = []
        reverse_sequence_records = []

        for record_information in edited_sequence_record_information: 
                forward_record = SeqRecord(record_information.ForwardSequence, id = record_information.Id, description = record_information.Description)
                reverse_record = SeqRecord(record_information.ReverseSequence, id = record_information.Id, description= record_information.Description)
                forward_sequence_records.append(forward_record)
                reverse_sequence_records.append(reverse_record)
        return forward_sequence_records, reverse_sequence_records
