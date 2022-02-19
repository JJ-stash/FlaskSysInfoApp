import psutil

def getMemory():
    memory_b = dict(psutil.virtual_memory()._asdict()).get('total', None)

    memory_gb = format(memory_b / 1024**3, '.2f')

    return memory_gb