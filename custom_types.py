from collections import namedtuple

SequenceRecordInformation = namedtuple("SequenceRecordInformation",["Sequence", "SequenceLength", "Id", "Description"])
EditedSequenceRecordInformation = namedtuple("EditedSequenceRecordInformation", ["ForwardSequence", "ReverseSequence", "ForwardSequenceLength", "ReverseSequenceLength", "Id", "Description"])
PrimerInformation = namedtuple("PrimerInformation", ["Segment", "Direction", "Version", "Revcomp", "Sequence", "Id", "Description"])
DirectoryInformation = namedtuple("DirectoryInformation", ["EditedSequences", "Primers", "Sequences"])
