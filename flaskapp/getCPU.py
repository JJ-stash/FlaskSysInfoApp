import psutil

def getCPU():
    cpu_dict = {}

    cpu_cores = psutil.cpu_count(logical = False)
    cpu_threads = psutil.cpu_count()

    cpu_dict.update({'Cores': cpu_cores, 'Threads': cpu_threads})

    return cpu_dict