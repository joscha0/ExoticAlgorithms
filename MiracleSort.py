import time

def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

def miracleSort(list):
    if(is_sorted(list)):
        return list
    else:
        time.sleep(1000)
        miracleSort(list)
