"""
These functions were made to read in the compressed 
data file from Amazon. A csv version of the data
will be written the first time openFile is called, 
so that subsequent times it is called openFile
just reads in the csv which is faster than
uncompressing the file and reading it in.
"""

import gzip
import os.path
import pandas as pd

def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)

def openFile(path):
    """
    Unzip's the file and read into if reviews.csv doesn't exist
    write to it so it will be faster to read in next time.
       
    :param: path (str) : path of .gz jason file
    :returns: DataFrame of file contents
    :rvalue: Pandas DataFrame
    """
    if os.path.isfile('reviews.csv') is False:
        i = 0
        df = {}
        for d in parse(path):
            df[i] = d
            i += 1

        df = pd.DataFrame.from_dict(df, orient='index')
        df.to_csv('reviews.csv')
    else:
        df = pd.read_csv('reviews.csv')
    
    return df 