import os

def salvar_resultado(
    biblioteca,
    dataset,
    tipo,
    carregamento=None,
    downsampling=None,
    normais=None,
    carregamento_cpu=None,
    downsampling_cpu=None,
    normais_cpu=None
):
    os.makedirs("resultados", exist_ok=True)

    caminho = f"resultados/resultados_{biblioteca}_{dataset}_{tipo}.txt"

    with open(caminho, "w", encoding="utf-8") as f:

        f.write(f"Biblioteca: {biblioteca}\n")
        f.write(f"Dataset: {dataset}\n")
        f.write(f"Tipo: {tipo}\n")
        f.write("=" * 50 + "\n\n")

        # --------------------------------------------------
        # Carregamento
        # --------------------------------------------------

        if carregamento is not None:
            tempo, memoria = carregamento

            f.write("Carregamento:\n")
            f.write(f"Tempo médio: {tempo:.5f}s\n")
            f.write(f"Memória média: {memoria:.2f} MB\n\n")

        # --------------------------------------------------
        # Downsampling
        # --------------------------------------------------

        if downsampling is not None:
            tempo, memoria = downsampling

            f.write("Downsampling:\n")
            f.write(f"Tempo médio: {tempo:.5f}s\n")
            f.write(f"Memória média: {memoria:.2f} MB\n\n")

        # --------------------------------------------------
        # Normais
        # --------------------------------------------------

        if normais is not None:
            tempo, memoria = normais

            f.write("Cálculo de Normais:\n")
            f.write(f"Tempo médio: {tempo:.5f}s\n")
            f.write(f"Memória média: {memoria:.2f} MB\n\n")

        # --------------------------------------------------
        # Carregamento CPU
        # --------------------------------------------------

        if carregamento_cpu is not None:
            tempo, cpu_porcentagem, cpu_tempo = carregamento_cpu

            f.write("Carregamento (CPU):\n")
            f.write(f"Tempo médio: {tempo:.5f}s\n")
            f.write(f"CPU média (%): {cpu_porcentagem:.2f}%\n")
            f.write(f"CPU tempo médio: {cpu_tempo:.5f}s\n\n")

        # --------------------------------------------------
        # Downsampling CPU
        # --------------------------------------------------

        if downsampling_cpu is not None:
            tempo, cpu_porcentagem, cpu_tempo = downsampling_cpu

            f.write("Downsampling (CPU):\n")
            f.write(f"Tempo médio: {tempo:.5f}s\n")
            f.write(f"CPU média (%): {cpu_porcentagem:.2f}%\n")
            f.write(f"CPU tempo médio: {cpu_tempo:.5f}s\n\n")

        # --------------------------------------------------
        # Normais CPU
        # --------------------------------------------------

        if normais_cpu is not None:
            tempo, cpu_porcentagem, cpu_tempo = normais_cpu

            f.write("Cálculo de Normais (CPU):\n")
            f.write(f"Tempo médio: {tempo:.5f}s\n")
            f.write(f"CPU média (%): {cpu_porcentagem:.2f}%\n")
            f.write(f"CPU tempo médio: {cpu_tempo:.5f}s\n")