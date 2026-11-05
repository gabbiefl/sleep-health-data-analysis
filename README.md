<div align="center">

<img src="assets/sleep-panda-icon.svg" alt="Ícone do projeto" width="140" />

# Sono, Qualidade do Descanso e Estresse

### Dormir mais horas garante descansar melhor?

Análise de ciência de dados sobre a relação entre duração do sono, qualidade percebida do descanso e níveis de estresse.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge)

![Método](https://img.shields.io/badge/M%C3%A9todo-Correla%C3%A7%C3%A3o%20de%20Pearson-141B2D?style=for-the-badge)
![Amostra](https://img.shields.io/badge/Amostra-374%20indiv%C3%ADduos-141B2D?style=for-the-badge)
![Mostra Científica](https://img.shields.io/badge/Mostra%20Cient%C3%ADfica-CESUCA-F2D66B?style=for-the-badge&labelColor=141B2D)

</div>

---

## Sobre o projeto

É comum assumir que mais horas de sono resultam automaticamente em um descanso melhor. Este estudo questiona essa premissa ao tratar a eficiência do sono diante das interferências psicossociais e comportamentais da rotina moderna.

A partir de dados secundários de 374 indivíduos, o projeto analisa como **duração do sono**, **qualidade percebida do descanso** e **níveis de estresse** se relacionam, e se o estresse interfere no vínculo entre o tempo dormindo e a qualidade do descanso.

Desenvolvido para a Mostra Científica do Centro Universitário CESUCA.

## Pergunta de pesquisa

> Dormir mais horas resulta, necessariamente, em um descanso de melhor qualidade, e em que medida o estresse interfere nessa relação?

## Base de dados

- **Fonte:** Sleep Health and Lifestyle Dataset
- **Amostra:** 374 indivíduos
- **Variáveis de interesse:** duração do sono, qualidade percebida do descanso e nível de estresse

## Metodologia

- **Desenho:** quantitativo e correlacional, com dados secundários.
- **Estatística:** correlação de Pearson, adotada por ser adequada a variáveis contínuas (ou tratadas como tais) e por quantificar a direção e a intensidade de relações lineares.
- **Tratamento dos dados e estatística descritiva:** Python e Pandas (médias, desvios padrão, mínimos, máximos e matriz de correlação).
- **Visualização:** Seaborn e Matplotlib.

## Principais resultados

| Medida | Resultado |
| --- | --- |
| Duração média do sono | 7,13 h (DP = 0,79; amplitude de 5,8 a 8,5 h) |
| Qualidade média do descanso | 7,31 (entre 4 e 9) |
| Duração do sono × qualidade do descanso | r ≈ 0,88 |
| Estresse × qualidade do descanso | r ≈ −0,90 |
| Estresse × duração do sono | r ≈ −0,81 |

- A duração média do sono está dentro da faixa usualmente recomendada, então o problema central não se reduz à privação de horas.
- Duração e qualidade apresentam forte correlação positiva, o que, isoladamente, pareceria confirmar a premissa inicial.
- O estresse, porém, mostra a relação mais intensa de todas: correlaciona-se negativamente tanto com a qualidade do descanso quanto com a duração do sono, destacando-se como um fator limitante mais crítico do que o tempo na cama.

## Conclusão

Prolongar o sono não é condição suficiente para um descanso efetivo quando os níveis de estresse estão elevados. A eficiência e a regeneração do sono dependem, sobretudo, do equilíbrio emocional, da gestão do estresse e de fatores associados ao estilo de vida.

## Limitações

- O desenho é correlacional, portanto os resultados descrevem associações e não estabelecem causalidade.
- A análise utiliza dados secundários, e a qualidade do descanso é uma medida percebida (autorrelatada).

## Como executar

```bash
# Clone o repositório
git clone https://github.com/<seu-usuario>/<nome-do-repositorio>.git
cd <nome-do-repositorio>

# Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Instale as dependências
pip install pandas numpy matplotlib seaborn
```

Baixe o Sleep Health and Lifestyle Dataset, coloque o arquivo CSV na pasta do projeto e execute a análise:

```bash
python <arquivo-de-analise>.py
```

## Tecnologias

| Ferramenta | Uso |
| --- | --- |
| Python | Linguagem principal |
| Pandas | Limpeza dos dados e estatística descritiva |
| NumPy | Operações numéricas |
| Seaborn | Visualização das associações |
| Matplotlib | Gráficos |
