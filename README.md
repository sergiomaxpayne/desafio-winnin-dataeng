# 🚀 Desafio Técnico – Engenheiro de Dados Sênior

## 👨‍💻 Visão Geral

Neste desafio, eu recebi a tarefa de criar uma base de dados no **Databricks Community Edition**, trabalhando a partir de arquivos JSON e de chamadas à API da Wikipedia.  
O objetivo principal era montar tabelas, enriquecer os dados e realizar análises exploratórias sobre os criadores de conteúdo e seus posts.

Eu segui exatamente o que foi pedido, mas também acrescentei minhas próprias ideias para tornar o pipeline mais robusto, confiável e analítico.  
Assim, além de entregar o que foi solicitado, consegui mostrar meu pensamento crítico e minha forma de estruturar um projeto de dados.

---

## ✅ Parte 1 – Implementação no Databricks

### O que foi pedido e como eu resolvi

1. **Notebook 1 – Criar tabela `creators_scrape_wiki`**  
   - Li o arquivo `wiki_pages.json.gz` e criei a tabela `default.creators_scrape_wiki`.

2. **Notebook 2 – Criar tabela `posts_creator`**  
   - Li o arquivo `posts_creator.json.gz` e criei a tabela `default.posts_creator`.

3. **Notebook 3 – Criar tabela `users_yt` a partir da API da Wikipedia**  
   - Fiz chamadas à API da Wikipedia, relacionei `user_id` com `wiki_page` e salvei na tabela `default.users_yt`.

4. **Notebook 4 – Analisar criadores**  
   - Realizei joins entre `users_yt` e `posts_creator`.  
   - Criei análises de:
     - Top 3 posts por likes e views nos últimos 6 meses.  
     - Usuários que não tinham posts associados.  
     - Contagem de posts por mês.  
   - Extras implementados:  
     - Completei meses sem posts com valor 0.  
     - Criei pivotagem com `user_id` por mês.

### 💡 Minhas melhorias além do solicitado

Além dos quatro notebooks obrigatórios, eu criei mais dois, por iniciativa própria:

- **Notebook 5 – `platinum_features`**  
  - Agreguei métricas por criador: total de posts, soma/média/desvio de views e likes, taxa de engajamento, etc.  
  - Criei rankings globais de creators.  
  - Tratei nulos e garanti consistência das métricas.  
  - Salvei em uma tabela Delta (`platinum.creators_features`) para servir de base a análises futuras.  
  - Adicionei logging para monitorar a execução (ex: quantos creators processados e data da execução).

- **Notebook 6 – `data_quality_checks`**  
  - Desenvolvi um módulo de checagem de qualidade de dados com regras de:  
    - Not null,  
    - Valores positivos,  
    - Contagem mínima de registros.  
  - Padronizei a saída em DataFrame para facilitar auditoria.  
  - Assim, além de processar os dados, eu também garanti confiabilidade no pipeline.

---

## ✅ Parte 2 – Arquitetura do Pipeline em Produção

### 🎯 Objetivo
Projetar um **pipeline escalável e robusto** para ingestão e atualização contínua de dados de **criadores e posts**, sem depender de arquivos locais, mas sim das **APIs oficiais** e de scraping quando necessário.

---

### ⚙️ Orquestrador
- **Apache Airflow** (ou Managed Airflow em GCP/AWS/Azure).  
  - DAGs para orquestração e agendamento.  
  - Suporte a dependências, retries e monitoramento.  
  - Integração nativa com Spark, APIs e Data Lakes.  

---

### 🗂️ Modelagem de Dados
Tabelas principais:

- **Creators** → informações dos criadores (canal, nome, país, categoria).  
- **Posts** → publicações (título, data, views, likes, tags).  
- **Engagement** → métricas históricas e temporais (opcional).

📄 [Documentação completa do modelo de dados](docs/data_model.md)

---

### 🌐 Extração de Dados
- **Wikipedia API** → coleta de nomes e informações de criadores.  
- **YouTube Data API (v3)** → canais, vídeos e estatísticas.  
- **Web Scraping (fallback)** → quando não houver API disponível.  

---

### 🔄 Etapas do Pipeline
1. **Ingestão** → APIs para Data Lake (JSON bruto).  
2. **Bronze Layer** → dados crus armazenados em Delta/Parquet.  
3. **Silver Layer** → normalização, tabelas `creators` e `posts`.  
4. **Gold/Platinum** → métricas derivadas (ex.: engajamento).  
5. **Consumo** → dashboards BI e modelos de ML.

---

### 📐 Arquitetura (alto nível)

```mermaid
flowchart TD
    A[Wikipedia API] --> B[Ingestao Airflow]
    C[YouTube API] --> B
    B --> D[Data Lake - Bronze]
    D --> E[Transformacao Spark e Databricks]
    E --> F[Tabelas Silver]
    F --> G[Tabelas Gold e Platinum]
    G --> H[Dashboards BI e Data Science]
