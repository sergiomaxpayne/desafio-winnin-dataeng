# 🏗️ Arquitetura do Pipeline

## Fluxo de Dados

```mermaid
flowchart TD
    A[Wikipedia API] --> B[Ingestão Airflow]
    C[YouTube API] --> B
    B --> D[Data Lake - Bronze]
    D --> E[Transformação Spark/Databricks]
    E --> F[Tabelas Silver]
    F --> G[Tabelas Gold/Platinum]
    G --> H[Dashboards BI / Data Science]
