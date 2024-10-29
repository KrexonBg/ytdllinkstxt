import os
# a helper function to check if a .txt file has non-zero length or not
# returns False when the length is zero
def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0
