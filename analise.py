import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. DOWNLOAD DO DATASET
# ============================================================

path = kagglehub.dataset_download(
    "uom190346a/sleep-health-and-lifestyle-dataset"
)

print("Path to dataset files:", path)


# ============================================================
# 2. LOCALIZAR E CARREGAR O CSV
# ============================================================

import os

# Listar os arquivos baixados
arquivos = os.listdir(path)

print("\nArquivos encontrados:")
for arquivo in arquivos:
    print(arquivo)


# Carregar o arquivo CSV
arquivo_csv = [arquivo for arquivo in arquivos if arquivo.endswith(".csv")][0]

caminho_csv = os.path.join(path, arquivo_csv)

df = pd.read_csv(caminho_csv)

print("\nDataset carregado com sucesso!")


# ============================================================
# 3. VISÃO INICIAL DOS DADOS
# ============================================================

print("\nPrimeiras linhas:")
print(df.head())

print("\nInformações do dataset:")
df.info()

print("\nDimensões do dataset:")
print(df.shape)

print("\nEstatísticas descritivas:")
print(df.describe())


# ============================================================
# 4. VERIFICAR AS VARIÁVEIS UTILIZADAS
# ============================================================

print("\nColunas disponíveis:")
print(df.columns.tolist())


# ============================================================
# 5. CALCULAR A MEDIANA DA DURAÇÃO DO SONO
# ============================================================

mediana_sono = df["Sleep Duration"].median()

print("\n========================================")
print("MEDIANA DA DURAÇÃO DO SONO")
print("========================================")
print(f"Mediana de Sleep Duration: {mediana_sono} horas")


# ============================================================
# 6. DIVIDIR OS INDIVÍDUOS EM DOIS GRUPOS
# ============================================================

# Pessoas que dormem acima da mediana

grupo_mais_sono = df.query("`Sleep Duration` > @mediana_sono")

# Pessoas que dormem na mediana ou abaixo dela

grupo_menos_sono = df.query("`Sleep Duration` <= @mediana_sono")


# ============================================================
# 7. VERIFICAR O TAMANHO DOS GRUPOS
# ============================================================

print("\n========================================")
print("TAMANHO DOS GRUPOS")
print("========================================")

print(f"Pessoas que dormem acima da mediana: {len(grupo_mais_sono)}")
print(f"Pessoas que dormem na/abaixo da mediana: {len(grupo_menos_sono)}")


# ============================================================
# 8. ANALISAR A QUALIDADE DO SONO
# ============================================================

print("\n========================================")
print("QUALIDADE DO SONO - GRUPO QUE DORME MAIS")
print("========================================")

print(grupo_mais_sono["Quality of Sleep"].describe())


print("\n========================================")
print("QUALIDADE DO SONO - GRUPO QUE DORME MENOS/IGUAL")
print("========================================")

print(grupo_menos_sono["Quality of Sleep"].describe())


# ============================================================
# 9. COMPARAR AS MÉDIAS
# ============================================================

media_qualidade_mais = grupo_mais_sono["Quality of Sleep"].mean()

media_qualidade_menos = grupo_menos_sono["Quality of Sleep"].mean()

diferenca = media_qualidade_mais - media_qualidade_menos


print("\n========================================")
print("COMPARAÇÃO DOS GRUPOS")
print("========================================")

print(
    f"Qualidade média - acima da mediana: "
    f"{media_qualidade_mais:.2f}"
)

print(
    f"Qualidade média - na/abaixo da mediana: "
    f"{media_qualidade_menos:.2f}"
)

print(f"Diferença entre as médias: {diferenca:.2f} pontos")


# ============================================================
# 10. CONCLUSÃO
# ============================================================

print("\n========================================")
print("CONCLUSÃO")
print("========================================")

if diferenca > 0:
    print(
        "O grupo que dorme acima da mediana apresentou "
        "maior qualidade média de sono."
    )

elif diferenca < 0:
    print(
        "O grupo que dorme acima da mediana apresentou "
        "menor qualidade média de sono."
    )

else:
    print(
        "Os dois grupos apresentaram a mesma qualidade "
        "média de sono."
    )


# ============================================================
# 11. RESUMO DOS RESULTADOS
# ============================================================

print("\n========================================")
print("RESUMO DA PESQUISA")
print("========================================")

print(f"Mediana de Sleep Duration: {mediana_sono} horas")
print(f"Grupo acima da mediana: {len(grupo_mais_sono)} pessoas")
print(f"Grupo na/abaixo da mediana: {len(grupo_menos_sono)} pessoas")
print(f"Qualidade média do primeiro grupo: {media_qualidade_mais:.2f}")
print(f"Qualidade média do segundo grupo: {media_qualidade_menos:.2f}")
print(f"Diferença: {diferenca:.2f} pontos")

# ============================================================
# 12. GRÁFICOS DE BARRAS PARA O BANNER
# ============================================================

# Fontes grandes: o banner é lido a distância
plt.rcParams.update({
    "font.size": 16,
    "axes.titlesize": 22,
    "axes.labelsize": 18,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
})

COR_POSITIVA = "#2E75B6"   # azul
COR_NEGATIVA = "#C0504D"   # vermelho


# ============================================================
# GRÁFICO 1 (principal): correlação de Pearson entre as variáveis
# ============================================================

corr = df[["Sleep Duration", "Quality of Sleep", "Stress Level"]].corr()

pares = {
    "Duração × Qualidade": corr.loc["Sleep Duration", "Quality of Sleep"],
    "Estresse × Qualidade": corr.loc["Stress Level", "Quality of Sleep"],
    "Estresse × Duração": corr.loc["Stress Level", "Sleep Duration"],
}

rotulos = list(pares.keys())
valores = list(pares.values())
cores = [COR_POSITIVA if v > 0 else COR_NEGATIVA for v in valores]

fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.bar(rotulos, valores, color=cores, width=0.55)

ax.axhline(0, color="black", linewidth=1)
ax.set_ylim(-1.1, 1.1)
ax.set_ylabel("Coeficiente de correlação (r)")
ax.set_title("Correlação de Pearson entre sono, qualidade e estresse")

# Valor de r
for barra, v in zip(barras, valores):
    deslocamento = 0.04 if v > 0 else -0.04
    alinhamento = "bottom" if v > 0 else "top"
    ax.text(
        barra.get_x() + barra.get_width() / 2,
        v + deslocamento,
        f"{v:.2f}",
        ha="center",
        va=alinhamento,
        fontsize=18,
        fontweight="bold",
    )

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.text(
    0.99, -0.14, f"n = {len(df)}  |  Fonte: Sleep Health and Lifestyle Dataset",
    transform=ax.transAxes, ha="right", fontsize=11, color="gray",
)

plt.tight_layout()
plt.savefig("grafico_correlacoes.png", dpi=300, bbox_inches="tight")
plt.show()


# ============================================================
# GRÁFICO 2: qualidade média por grupo de duração do sono
# ============================================================

grupos = [
    f"Acima da mediana\n(> {mediana_sono} h)\nn = {len(grupo_mais_sono)}",
    f"Na mediana ou abaixo\n(≤ {mediana_sono} h)\nn = {len(grupo_menos_sono)}",
]
medias = [media_qualidade_mais, media_qualidade_menos]

fig, ax = plt.subplots(figsize=(9, 6))
barras = ax.bar(grupos, medias, color=[COR_POSITIVA, "#7F7F7F"], width=0.5)

ax.set_ylim(0, 10)
ax.set_ylabel("Qualidade média do sono (0–10)")
ax.set_title("Qualidade do sono por grupo de duração")

for barra, m in zip(barras, medias):
    ax.text(
        barra.get_x() + barra.get_width() / 2,
        m + 0.15,
        f"{m:.2f}",
        ha="center",
        va="bottom",
        fontsize=18,
        fontweight="bold",
    )

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("grafico_qualidade_por_grupo.png", dpi=300, bbox_inches="tight")
plt.show()