import open3d as o3d
import psutil
import time
import os
import gc
import statistics

#leitura do arquivo
process = psutil.Process(os.getpid())
num_cpus = psutil.cpu_count()

tempos = []
cpus_porcentagem = []
cpus_tempo = []

for i in range(3):
    point_cloud = o3d.io.read_point_cloud("standforbunny.ply")

for _ in range(15):
    start = time.perf_counter()
    cpu_antes = process.cpu_times()

    point_cloud = o3d.io.read_point_cloud("standforbunny.ply")

    cpu_final = process.cpu_times()
    end = time.perf_counter()

    tempo_total = (end - start)

    cpu_total = ((cpu_final.user - cpu_antes.user) + (cpu_final.system - cpu_antes.system))
    cpu_media = (cpu_total / (tempo_total)) * 100 / num_cpus

    tempos.append(tempo_total)
    cpus_porcentagem.append(cpu_media)
    cpus_tempo.append(cpu_total)

print(f"Tempo médio: {statistics.mean(tempos):.5f}s")
print(f"Tempo mediano: {statistics.median(tempos):.5f}s")

print(f"CPU média (%): {statistics.mean(cpus_porcentagem):.2f}%")
print(f"CPU mediana (%): {statistics.median(cpus_porcentagem):.2f}%")

print(f"CPU tempo médio: {statistics.mean(cpus_tempo):.5f}s")

#downsampling
process = psutil.Process(os.getpid())
num_cpus = psutil.cpu_count()

tempos = []
cpus_percent = []
cpus_time = []

point_cloud = o3d.io.read_point_cloud("standforbunny.ply")

for _ in range(3):
    point_cloud.voxel_down_sample(voxel_size=5)

for i in range(15):
    start = time.perf_counter()
    cpu_start = process.cpu_times()

    downsampling = point_cloud.voxel_down_sample(voxel_size=0.01)

    cpu_end = process.cpu_times()
    end = time.perf_counter()

    wall_time = (end - start)

    cpu_time = ((cpu_end.user - cpu_start.user) + (cpu_end.system - cpu_start.system))

    cpu_percent = (cpu_time / wall_time) * 100 / num_cpus

    tempos.append(wall_time)
    cpus_percent.append(cpu_percent)
    cpus_time.append(cpu_time)

print(f"Tempo médio: {statistics.mean(tempos):.5f}s")
print(f"Tempo mediano: {statistics.median(tempos):.5f}s")

print(f"CPU média (%): {statistics.mean(cpus_percent):.2f}%")
print(f"CPU mediana (%): {statistics.median(cpus_percent):.2f}%")

print(f"CPU tempo médio: {statistics.mean(cpus_time):.5f}s")

#normais
process = psutil.Process(os.getpid())
num_cpus = psutil.cpu_count()

tempos = []
cpus_percent = []
cpus_time = []

point_cloud = o3d.io.read_point_cloud("standforbunny.ply")
downsampling = point_cloud.voxel_down_sample(voxel_size=0.01)

search_param = o3d.geometry.KDTreeSearchParamHybrid(radius=1, max_nn=30)

for _ in range(3):
    downsampling.estimate_normals(search_param)

for i in range(15):
    start = time.perf_counter()
    cpu_start = process.cpu_times()

    downsampling.estimate_normals(search_param)

    cpu_end = process.cpu_times()
    end = time.perf_counter()

    wall_time = (end - start)
    cpu_time = ((cpu_end.user - cpu_start.user) + (cpu_end.system - cpu_start.system))
    cpu_percent = (cpu_time / wall_time) * 100 / num_cpus

    tempos.append(wall_time)
    cpus_percent.append(cpu_percent)
    cpus_time.append(cpu_time)

print(f"Tempo médio: {statistics.mean(tempos):.4f}s")
print(f"Tempo mediano: {statistics.median(tempos):.4f}s")

print(f"CPU média (%): {statistics.mean(cpus_percent):.2f}%")
print(f"CPU mediana (%): {statistics.median(cpus_percent):.2f}%")

print(f"CPU tempo médio: {statistics.mean(cpus_time):.5f}s")