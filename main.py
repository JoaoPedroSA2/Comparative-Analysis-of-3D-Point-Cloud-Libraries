from src.dataset_config import DATASETS
from Open3D.o3d_mem import carregar_mem_o3d, downsample_mem_o3d, normais_mem_o3d
from Open3D.o3d_cpu import carregar_cpu_o3d, downsample_cpu_o3d, normais_cpu_o3d
from PyntCloud.pynt_mem import carregar_mem_pynt, downsample_mem_pynt
from PyntCloud.pynt_cpu import carregar_cpu_pynt, downsample_cpu_pynt
from Trimesh.trimesh_mem import carregar_mem_trimesh
from Trimesh.trimesh_cpu import carregar_cpu_trimesh
from src.salvar_resultado import salvar_resultado

def executar():
    for dataset, info in DATASETS.items():
        caminho = info["caminho"]
        tipo = info["tipo"] 

        print(f"="*30)
        print(f"Dataset: {dataset}")
        print(f"Tipo: {tipo}")
        print(f"="*30)



        print(f"Iniciando Benchmark para Open3d")
        #memoria
        media_tempo_o3d, media_mem_o3d = carregar_mem_o3d(caminho)
        media_tempo_downsample_o3d, media_mem_downsample_o3d = downsample_mem_o3d(caminho)
        media_tempo_normais_o3d, media_mem_normais_o3d = normais_mem_o3d(caminho)

        #cpu
        media_tempo_cpu_o3d, media_cpu_porcentagem_o3d, media_cpu_tempo_o3d = carregar_cpu_o3d(caminho)
        media_tempo_downsample_cpu_o3d, media_cpu_porcentagem_downsample_o3d, media_cpu_tempo_downsample_o3d = downsample_cpu_o3d(caminho)
        media_tempo_normais_cpu_o3d, media_cpu_porcentagem_normais_o3d, media_cpu_tempo_normais_o3d = normais_cpu_o3d(caminho)

        #salvando resultados
        salvar_resultado(
        biblioteca="Open3D",
        dataset=dataset,
        tipo=tipo,

        carregamento=(
            media_tempo_o3d,
            media_mem_o3d
        ),

        downsampling=(
            media_tempo_downsample_o3d,
            media_mem_downsample_o3d
        ),

        normais=(
            media_tempo_normais_o3d,
            media_mem_normais_o3d
        ),

        carregamento_cpu=(
            media_tempo_cpu_o3d,
            media_cpu_porcentagem_o3d,
            media_cpu_tempo_o3d
        ),

        downsampling_cpu=(
            media_tempo_downsample_cpu_o3d,
            media_cpu_porcentagem_downsample_o3d,
            media_cpu_tempo_downsample_o3d
        ),

        normais_cpu=(
            media_tempo_normais_cpu_o3d,
            media_cpu_porcentagem_normais_o3d,
            media_cpu_tempo_normais_o3d
        )
    )
        
    print(f"Benchmark para Open3d concluído com sucesso!")

    print(f"Iniciando Benchmark para PyntCloud")
    media_tempo_pynt, media_mem_pynt = carregar_mem_pynt(caminho)
    media_tempo_downsample_pynt, media_mem_downsample_pynt = downsample_mem_pynt(caminho)

    media_tempo_cpu_pynt, media_cpu_porcentagem_pynt, media_cpu_tempo_pynt = carregar_cpu_pynt(caminho)
    media_tempo_downsample_cpu_pynt, media_cpu_porcentagem_downsample_pynt, media_cpu_tempo_downsample_pynt = downsample_cpu_pynt(caminho)

    salvar_resultado(
        biblioteca="PyntCloud",
        dataset=dataset,
        tipo=tipo,

        carregamento=(
            media_tempo_pynt,
            media_mem_pynt
        ),

        downsampling=(
            media_tempo_downsample_pynt,
            media_mem_downsample_pynt
        ),

        carregamento_cpu=(
            media_tempo_cpu_pynt,
            media_cpu_porcentagem_pynt,
            media_cpu_tempo_pynt
        ),

        downsampling_cpu=(
            media_tempo_downsample_cpu_pynt,
            media_cpu_porcentagem_downsample_pynt,
            media_cpu_tempo_downsample_pynt
        )
    )

    print(f"Benchmark para PyntCloud concluído com sucesso!")

    print(f"Iniciando Benchmark para Trimesh")
    media_tempo_trimesh, media_mem_trimesh = carregar_mem_trimesh(caminho)

    media_tempo_cpu_trimesh, media_cpu_porcentagem_trimesh, media_cpu_tempo_trimesh = carregar_cpu_trimesh(caminho)

    salvar_resultado(
        biblioteca="Trimesh",
        dataset=dataset,
        tipo=tipo,

        carregamento=(
            media_tempo_trimesh,
            media_mem_trimesh
        ),

        carregamento_cpu=(
            media_tempo_cpu_trimesh,
            media_cpu_porcentagem_trimesh,
            media_cpu_tempo_trimesh
        )
)
    print(f"Benchmark para Trimesh concluído com sucesso!")

    print(f"Benchmark concluído com sucesso para todos os datasets!")

if __name__ == "__main__":
    executar()