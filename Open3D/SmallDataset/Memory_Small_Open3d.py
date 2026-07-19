import open3d as o3d
import psutil
import time
import os
import gc
import statistics

def medir_memoria():
    return psutil.Process(os.getpid()).memory_info().rss / (1024*1024)


valores_tempo = []
valores_memoria = []

for i in range(10):
    gc.collect()

    memoria_antes = medir_memoria()

    start = time.time()
    point_cloud = o3d.io.read_point_cloud('standforbunny.ply')
    end = time.time()

    memoria_final = medir_memoria()

    valores_tempo.append(end - start)
    valores_memoria.append(memoria_final - memoria_antes)

    del point_cloud
    gc.collect()
    gc.collect()

print("tempo medio gasto: ", sum(valores_tempo)/len(valores_tempo))
print("memoria media gasta: ", sum(valores_memoria)/len(valores_memoria))

print("desvio tempo: ", statistics.stdev(valores_tempo))
print("desvio memoria: ", statistics.stdev(valores_memoria))

gc.collect()

point_cloud = o3d.io.read_point_cloud('standforbunny.ply')

print(f"pontos originais: {len(point_cloud.points)}")

valores_tempo = []
valores_memoria = []

for i in range(10):
    gc.collect()

    memoria_antes = medir_memoria()

    start = time.time()

    downsampling = point_cloud.voxel_down_sample(voxel_size = 0.01)

    end = time.time()

    memoria_final = medir_memoria()

    valores_tempo.append(end - start)
    valores_memoria.append(memoria_final - memoria_antes)

    del downsampling
    gc.collect()

downsampling = point_cloud.voxel_down_sample(voxel_size = 0.01)

print(f"pontos apos downsampling: {len(downsampling.points)}")

print("tempo medio gasto: ", sum(valores_tempo) / len(valores_tempo))
print("memoria media gasta: ", sum(valores_memoria) / len(valores_memoria))

print("desvio tempo: ", statistics.stdev(valores_tempo))
print("desvio memoria: ", statistics.stdev(valores_memoria))

downsampling = point_cloud.voxel_down_sample(voxel_size=0.01)

start = time.time()

memoria_antes = medir_memoria()

downsampling.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30)
)

memoria_final = medir_memoria()

end = time.time()

memoria_total = memoria_final - memoria_antes

tempo_final = end - start

print("tempo gasto para aplicar as normais: ", tempo_final)
print("memoria gasta para carregar as normais: ", memoria_total)

memoria_visu_antes = medir_memoria()
start_visu = time.time()

o3d.visualization.draw_geometries([downsampling], point_show_normal=True)

end_visu = time.time()
memoria_visu_final = medir_memoria()

memoria_visu = memoria_visu_final - memoria_visu_antes
tempo_visu = end_visu - start_visu

print("tempo no visualizador: ", tempo_visu)
print("memoria gasta no visualizador: ", memoria_visu)