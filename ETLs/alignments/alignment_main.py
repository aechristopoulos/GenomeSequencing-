import a_extract
import a_transform
import a_load

def align(absolute_path): 
    segment_information = a_extract.extract(absolute_path)
    a_transform.transform(absolute_path, segment_information)
    a_load.load(absolute_path)
