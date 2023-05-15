import ta_extract
import ta_transform
import ta_load

def tree_alignment_main(absolute_path): 
    segment_information = ta_extract.extract(absolute_path)
    ta_transform.transform(absolute_path, segment_information)
    ta_load.load(absolute_path)