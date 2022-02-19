import psutil

def getProcs():
    process_list = []

    for process in psutil.process_iter(['pid', 'name']):
        process_list.append(process.info)
        
    return process_list