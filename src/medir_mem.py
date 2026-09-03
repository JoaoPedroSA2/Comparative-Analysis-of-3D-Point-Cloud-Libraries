import psutil
import os

def medir_memoria():
    return psutil.Process(os.getpid()).memory_info().rss / (1024*1024)
