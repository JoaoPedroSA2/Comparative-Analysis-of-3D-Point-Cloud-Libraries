import trimesh
import psutil
import time
import os
import gc
import statistics  

def carregar_cpu_trimesh(caminho):
    
    process = psutil.Process(os.getpid())
    tempos = []
    cpus_tempo = []
    cpus_porcentagem = []

    for i in range(3):
        mesh = trimesh.load(caminho)

    for j in range(15):
        start = time.perf_counter()
        
        cpu_antes = process.cpu_times()
        
        mesh = trimesh.load("standforbunny.ply")
        
        cpu_final = process.cpu_times()
        
        end = time.perf_counter()
        
        cpu_total = (cpu_final.user - cpu_antes.user) + (cpu_final.system - cpu_antes.system)
        cpu_media = (cpu_total/(end-start)) * 100
        
        tempos.append(end-start)
        cpus_porcentagem.append(cpu_media)
        cpus_tempo.append(cpu_total)

    print(f"Tempo médio: {statistics.mean(tempos):.5f}s")
    print(f"Tempo mediano: {statistics.median(tempos):.5f}s")

    print(f"CPU média (%): {statistics.mean(cpus_porcentagem):.2f}%")
    print(f"CPU mediana (%): {statistics.median(cpus_porcentagem):.2f}%")

    print(f"CPU tempo médio: {statistics.mean(cpus_tempo):.5f}s")

    return statistics.mean(tempos), statistics.mean(cpus_porcentagem), statistics.mean(cpus_tempo)