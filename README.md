
# Caruaru Aedes Dashboard – Starter Kit

Este pacote ajuda a montar um **dashboard Streamlit** para apresentar na sua **ExpoTech**.
Inclui **templates de dados**, **estrutura de indicadores** e um **app base**.

## Indicadores essenciais (sugestão)
- **IIP (LIRAa) por bairro e ciclo** (iip_percent).
- **Classificação de risco**: <1% (baixo), 1–3,9% (médio), ≥4% (alto).
- **Principais criadouros** por bairro/ciclo (tipo_recipient: positivos / inspecionados).
- **Ações de campo**: domicílios visitados, depósitos eliminados, data e tipo de ação.
- **Casos por semana epidemiológica** (dengue/zika/chikungunya) pelo menos em nível municipal.
- **Clima**: chuva (mm) e temperatura (°C) – sazonalidade é forte para vetores.
- **Socioambiental**: população, densidade, coleta de lixo, abastecimento intermitente, renda (*se disponível*).
- **Mapa por bairro** (GeoJSON) para heatmaps e priorização espacial.

## Arquivos de dados
- `data/bairros.csv`
- `data/liraa_por_bairro_2024_2025.csv`
- `data/criaderos_por_bairro_2024_2025.csv`
- `data/intervencoes_exemplo.csv`
- `data/casos_semanas_arboviroses.csv`
- `data/clima_diario.csv`
- `data/socioambiental_por_bairro.csv`
- `geo/caruaru_bairros_placeholder.geojson` (substitua por um GeoJSON real de bairros)

## Ideias de análises e visualizações
- **Mapa de calor** do IIP por ciclo/ano + camada de casos (se houver por bairro).
- **Ranking de bairros** por IIP e por criadouro predominante.
- **Correlação** entre chuva e IIP com defasagem (lag) de 1–8 semanas.
- **Efeito das ações**: evolução do IIP antes/depois das intervenções.
- **Prioridade operacional**: pontuação = normalizar(IIP) + normalizar(casos) + normalizar(densidade) + bônus se abastecimento intermitente=1.
- **What-if**: simular redução de um tipo de criadouro em X% e ver impacto no IIP.

## Como obter dados oficiais
- LIRAa por bairro: Vigilância em Saúde de Caruaru (solicite por **LAI**).
- Casos por semana: SES-PE/municipal.
- Clima: INMET/CPTEC (estações regionais).
- Socioambiental: IBGE/Prefeitura.
Substitua `None` pelos valores coletados.

## Dicionário de dados (resumo)
- `bairro_id`: ID do bairro (veja `bairros.csv`).
- `iip_percent`: índice de infestação predial (0–100).
- `ciclo`: 1..6 (ciclos do LIRAa no ano).
- `tipo_recipient`: categoria do criadouro inspecionada.
- `positivos`/`inspecionados`: contagem de recipientes.
- `semana_epi`: semana epidemiológica ISO.
- `chuva_mm`, `temp_c`: clima diário.
- `abastecimento_intermittente`: 0/1 (sim/não).

Boa apresentação! 💪
