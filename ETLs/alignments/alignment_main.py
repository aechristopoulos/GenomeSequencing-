import extract
import transform
import load

def align(absolute_path): 
    segment_information = extract.extract(absolute_path)
    transform.transform(absolute_path, segment_information)
    load.load(absolute_path)
