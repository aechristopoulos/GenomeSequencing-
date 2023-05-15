from collections import namedtuple

SequenceRecordInformation = namedtuple("SequenceRecordInformation",["Segment", "Strain", "Sequence", "SequenceLength", "Id", "Description"])
EditedSequenceRecordInformation = namedtuple("EditedSequenceRecordInformation", ["Segment", "Strain", "EditedSequence", "EditedSequenceLength", "Id", "Description"])
DirectoryInformation = namedtuple("DirectoryInformation", ["Sequences", "EditedSequences"])