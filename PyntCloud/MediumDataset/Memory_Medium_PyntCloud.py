from pyntcloud import PyntCloud
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
    point_cloud = PyntCloud.from_file(r"C:\Users\joao.santana\Downloads\xyzrgb_statuette.ply\xyzrgb_statuette.ply")
    
    del point_cloud
    gc.collect()

for j in range(15):
    memoria_antes = medir_memoria()
    
    start = time.time()
    
    point_cloud = PyntCloud.from_file(r"C:\Users\joao.santana\Downloads\xyzrgb_statuette.ply\xyzrgb_statuette.ply")
    
    memoria_final = medir_memoria()
    
    end = time.time()
    
    tempos.append(end-start)
    memorias.append(memoria_final - memoria_antes)
    
    del point_cloud
    gc.collect()

print("tempo gasto: ", statistics.mean(tempos))
print("memoria gasta: ", statistics.mean(memorias))

#downsampling
gc.collect()

tempos = []
memorias = []

point_cloud = PyntCloud.from_file(r"C:\Users\joao.santana\Downloads\xyzrgb_statuette.ply\xyzrgb_statuette.ply")
print("pontos originais: ", point_cloud.points)

for j in range(15):
    memoria_antes = medir_memoria()
    
    start = time.time()
    
    voxelgrid_id = point_cloud.add_structure("voxelgrid", size_x = 5, size_y = 5, size_z = 5)
    
    voxelgrid = point_cloud.structures[voxelgrid_id]
    
    sample = point_cloud.get_sample("voxelgrid_centers", voxelgrid_id = voxelgrid_id)
    
    memoria_final = medir_memoria()
    
    end = time.time()
    
    tempos.append(end-start)
    memorias.append(memoria_final - memoria_antes)
    
    del point_cloud.structures[voxelgrid_id]
    del voxelgrid_id, voxelgrid, sample,
    gc.collect()

print("tempo medio gasto: ", statistics.mean(tempos))
print("memoria media gasta: ", statistics.mean(memorias))