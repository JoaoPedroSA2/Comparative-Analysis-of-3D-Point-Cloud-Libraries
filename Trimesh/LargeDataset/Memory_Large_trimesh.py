import trimesh
import psutil
import time
import os
import gc
import statistics  

def medir_memoria():
    return psutil.Process(os.getpid()).memory_info().rss / (1024*1024)

#leitura do arquivo
gc.collect()

tempos = []
memorias = []

for i in range(3):
    mesh = trimesh.load(r"C:\Users\joao.santana\Downloads\lucy.ply\lucy.ply")
    
    del mesh
    gc.collect()

for i in range(15):
    memoria_antes = medir_memoria()
    start = time.time()
    
    mesh = trimesh.load(r"C:\Users\joao.santana\Downloads\lucy.ply\lucy.ply")
    
    end = time.time()
    memoria_final = medir_memoria()
    
    tempos.append(end-start)
    memorias.append(memoria_final-memoria_antes)
    
    del mesh
    gc.collect()

print("tempo total: ", statistics.mean(tempos))
print("memoria total: ", statistics.mean(memorias))