import time
import multiprocessing

def sleepy_man(sec):
    print('Starting to sleep for {} seconds'.format(sec))
    time.sleep(sec)
    print('Done sleeping for {} seconds'.format(sec))

if __name__ ==  '__main__':
    tic = time.time()

    pool = multiprocessing.Pool(5)
    pool.map(sleepy_man, range(1,11))
    pool.close()

    toc = time.time()

    print('Done in {:.4f} seconds'.format(toc-tic))
