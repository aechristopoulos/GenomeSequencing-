from collections import namedtuple

PrimerInformation = namedtuple("PrimerInformation", ["Segment", "Direction", "Version", "Revcomp", "Sequence", "Id", "Description"])
AlignmentInformation = namedtuple("AlignmentInformation", ["Segment", "Strain", "Sequence", "Id", "Description"])
DirectoryInformation = namedtuple("DictoryInformation", ["Primers", "Alignments"])