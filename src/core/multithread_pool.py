import multiprocessing

class Multiprocessing:
    pool = multiprocessing.Pool(multiprocessing.cpu_count() - 1)
