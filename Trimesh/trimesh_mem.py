import trimesh
import psutil
import time
import os
import gc
import statistics
from src.medir_mem import medir_memoria

def carregar_mem_trimesh(caminho):
    gc.collect()

    tempos = []
    memorias = []

    for i in range(3):
        mesh = trimesh.load("standforbunny.ply")
        
        del mesh
        gc.collect()

    for i in range(15):
        memoria_antes = medir_memoria()
        start = time.time()
        
        mesh = trimesh.load("standforbunny.ply")
        
        end = time.time()
        memoria_final = medir_memoria()
        
        tempos.append(end-start)
        memorias.append(memoria_final-memoria_antes)
        
        del mesh
        gc.collect()

    print("tempo total: ", statistics.mean(tempos))
    print("memoria total: ", statistics.mean(memorias))

    return statistics.mean(tempos), statistics.mean(memorias)

