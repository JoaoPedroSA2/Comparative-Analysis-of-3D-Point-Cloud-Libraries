import open3d as o3d
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

for i in range(5):
    point_cloud = o3d.io.read_point_cloud(r'C:\Users\joao.santana\Downloads\xyzrgb_statuette.ply\xyzrgb_statuette.ply')
    del point_cloud
    gc.collect()

for j in range(15):
    start = time.time()

    memoria_antes = medir_memoria()

    point_cloud = o3d.io.read_point_cloud(r"C:\Users\joao.santana\Downloads\xyzrgb_statuette.ply\xyzrgb_statuette.ply")
    memoria_final = medir_memoria()
    end = time.time()

    tempos.append(end-start)
    memorias.append(memoria_final - memoria_antes)

    del point_cloud
    gc.collect()

print("tempo total: ", statistics.mean(tempos))
print("memoria final: ", statistics.mean(memorias))

#downsampling
gc.collect()

tempos = []
memorias = []

point_cloud = o3d.io.read_point_cloud(
    r"C:\Users\joao.santana\Downloads\xyzrgb_statuette.ply\xyzrgb_statuette.ply"
)
print(f"pontos restantes: {len(point_cloud.points)}")

for i in range(5):
    downsampling = point_cloud.voxel_down_sample(voxel_size=5)
    del downsampling
    gc.collect()

for j in range(15):
    start = time.time()

    memoria_antes = medir_memoria()

    downsampling = point_cloud.voxel_down_sample(voxel_size=5)

    memoria_final = medir_memoria()
    end = time.time()

    tempos.append(end - start)
    memorias.append(memoria_final - memoria_antes)

print(f"pontos restantes: {len(downsampling.points)}")
print("tempo total: ", statistics.mean(tempos))
print("memoria final: ", statistics.mean(memorias))

#normais
gc.collect()

tempos = []
memorias = []

point_cloud = o3d.io.read_point_cloud(r"c:\Users\joao.santana\Downloads\xyzrgb_statuette.ply\xyzrgb_statuette.ply")

downsampling = point_cloud.voxel_down_sample(voxel_size=5)

for i in range(15):
    start = time.time()

    memoria_antes = medir_memoria()

    downsampling.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=1, max_nn=30))

    end = time.time()

    memoria_final = medir_memoria()

    tempos.append(end - start)
    memorias.append(memoria_final - memoria_antes)

print("tempo gasto: ", statistics.mean(tempos))
print("memoria gasta: ", statistics.mean(memorias))