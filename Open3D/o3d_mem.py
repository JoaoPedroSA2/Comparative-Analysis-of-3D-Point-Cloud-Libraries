import open3d as o3d
import gc
import time
import statistics
from src.medir_mem import medir_memoria

def carregar_mem_o3d(caminho):
    gc.collect()

    tempos = []
    memorias = []

    for i in range(5):
        point_cloud = o3d.io.read_point_cloud(caminho)
        del point_cloud
        gc.collect()

    for i in range(15):
        start = time.time()

        memoria_antes = medir_memoria()

        point_cloud = o3d.io.read_point_cloud(caminho)

        memoria_final = medir_memoria()
        end = time.time()

        tempos.append(end-start)
        memorias.append(memoria_final-memoria_antes)

        del point_cloud
        gc.collect()

    print(f"Tempo total: {statistics.mean(tempos):.2f}s")
    print(f"Memória total: {statistics.mean(memorias):.2f} MB")

    return statistics.mean(tempos), statistics.mean(memorias)

def downsample_mem_o3d(caminho):
    gc.collect()

    tempos = []
    memorias = []

    point_cloud = o3d.io.read_point_cloud(caminho)
    print(f"Pontos restantes: {len(point_cloud.points)}")

    for i in range(5):
        downsampling = point_cloud.voxel_down_sample(voxel_size = 5)
        del downsampling
        gc.collect()

    for i in range(15):
        start = time.time()

        memoria_antes = medir_memoria()

        downsampling = point_cloud.voxel_down_sample(voxel_size = 5)

        memoria_final = medir_memoria()
        end = time.time()

        tempos.append(end-start)
        memorias.append(memoria_final - memoria_antes)

        del downsampling
        gc.collect()

    print(f"Tempo total: {statistics.mean(tempos):.2f}s")
    print(f"Memória total: {statistics.mean(memorias):.2f} MB")

    return statistics.mean(tempos), statistics.mean(memorias)

def normais_mem_o3d(caminho):
    gc.collect()

    tempos = []
    memorias = []

    point_cloud = o3d.io.read_point_cloud(caminho)
    downsampling = point_cloud.voxel_down_sample(voxel_size = 5)

    for i in range(5):
        aux = downsampling.copy()
        aux.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=1, max_nn=30))

        del aux
        gc.collect()

    for i in range(15):
        aux = downsampling.copy()

        start = time.time()
        memoria_antes = medir_memoria()

        aux.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=1, max_nn=30))

        end = time.time()
        memoria_final = medir_memoria()

        tempos.append(end-start)
        memorias.append(memoria_final - memoria_antes)

        del aux
        gc.collect()

    print(f"Tempo total: {statistics.mean(tempos):.2f}s")
    print(f"Memória total: {statistics.mean(memorias):.2f} MB")

    del downsampling
    gc.collect()

    return statistics.mean(tempos), statistics.mean(memorias)