from pyntcloud import PyntCloud
import psutil
import time
import os
import gc
import statistics  

#leitura do arquivo
process = psutil.Process(os.getpid())
num_cpus = psutil.cpu_count()

tempo = []
cpus_porcentagem = []
cpus_tempo = []

for i in range(3):
    point_cloud = PyntCloud.from_file("standforbunny.ply")

for j in range(15):
    start = time.perf_counter()
    
    cpu_antes = process.cpu_times()
    
    point_cloud = PyntCloud.from_file("standforbunny.ply")
    
    cpu_final = process.cpu_times()
    
    end = time.perf_counter()
    
    tempo_total = (end-start)
    
    cpu_total = ((cpu_final.user - cpu_antes.user) + (cpu_final.system - cpu_antes.system))
    cpu_media = (cpu_total/(end-start)) * 100
    
    tempo.append(tempo_total)
    cpus_porcentagem.append(cpu_media)
    cpus_tempo.append(cpu_total)
    

print(f"Tempo médio: {statistics.mean(tempo):.5f}s")
print(f"Tempo mediano: {statistics.median(tempo):.5f}s")

print(f"CPU média (%): {statistics.mean(cpus_porcentagem):.2f}%")
print(f"CPU mediana (%): {statistics.median(cpus_porcentagem):.2f}%")

print(f"CPU tempo médio: {statistics.mean(cpus_tempo):.5f}s")

#downsampling
process = psutil.Process(os.getpid())

tempo = []
cpus_porcentagem = []
cpus_tempo = []

point_cloud = PyntCloud.from_file("standforbunny.ply")

for i in range(3):
    voxelgrid_id = point_cloud.add_structure("voxelgrid", size_x = 0.01, size_y = 0.01, size_z = 0.01)
    
    voxelgrid = point_cloud.structures[voxelgrid_id]
    
    sample = point_cloud.get_sample("voxelgrid_centers", voxelgrid_id = voxelgrid_id)

for j in range(15):
    start = time.perf_counter()
    
    cpu_antes = process.cpu_times()
    
    voxelgrid_id = point_cloud.add_structure("voxelgrid", size_x = 0.01, size_y = 0.01, size_z = 0.01)
    
    voxelgrid = point_cloud.structures[voxelgrid_id]
    
    sample = point_cloud.get_sample("voxelgrid_centers", voxelgrid_id = voxelgrid_id)
    
    cpu_final = process.cpu_times()
    
    end = time.perf_counter()
    
    tempo_total = (end-start)
    cpu_total = ((cpu_final.user - cpu_antes.user) + (cpu_final.system - cpu_antes.system))
    cpu_media = (cpu_total/(tempo_total)) * 100
    
    tempo.append(tempo_total)
    cpus_porcentagem.append(cpu_media)
    cpus_tempo.append(cpu_total)

print(f"Tempo médio: {statistics.mean(tempo):.5f}s")
print(f"Tempo mediano: {statistics.median(tempo):.5f}s")

print(f"CPU média (%): {statistics.mean(cpus_porcentagem):.2f}%")
print(f"CPU mediana (%): {statistics.median(cpus_porcentagem):.2f}%")

print(f"CPU tempo médio: {statistics.mean(cpus_tempo):.5f}s")