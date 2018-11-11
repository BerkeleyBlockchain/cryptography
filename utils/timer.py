"""timer.py"""

import time

def timer(f):
    def timed(*args):
        start = time.time()
        out = f(*args)
        print('Took {0} seconds'.format(time.time() - start))
        return out
    return timed
