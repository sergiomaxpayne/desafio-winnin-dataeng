# Parte 2 - Arquitetura e Pipeline de Dados

Esta parte do projeto foca no **desenho e documentação de um pipeline de dados escalável** para coleta e atualização contínua de informações de criadores e posts.

## 🎯 Objetivo
Criar uma solução capaz de **ingestão, transformação e disponibilização** de dados de forma automatizada, sem depender de arquivos JSON locais, mas conectando diretamente às **APIs oficiais**.

## ⚙️ Orquestração
O orquestrador escolhido é o **Apache Airflow**, pela maturidade, escalabilidade e forte integração com nuvens (AWS, GCP, Azure). Ele permite:
- Agendamento e monitoramento de DAGs;
- Retry automático em caso de falhas;
- SLA e alertas via e-mail/Slack.

## 🗄️ Modelagem de Dados
A modelagem é organizada em **três camadas** no Data Lake:

- **Bronze:** dados crus vindos das APIs (sem tratamento).
- **Silver:** dados limpos e padronizados (chaves normalizadas).
- **Gold/Platinum:** dados analíticos para dashboards e data science.

As tabelas principais são:
- `creators` → informações do criador.
- `posts` → posts com métricas de engajamento.
- `daily_engagement` → histórico temporal de métricas.

👉 Mais detalhes em [`data_model.md`](./data_model.md).

## 📤 Extração
- **Wikipedia API:** metadados dos criadores.
- **YouTube API:** estatísticas dos posts e canais.
- **Atualizações contínuas:** rodando diariamente via Airflow, apenas novos registros ou atualizações incrementais.

## 🔄 Fluxo do Pipeline
1. **Ingestão:** APIs → Data Lake Bronze.  
2. **Transformação:** Spark/Databricks → tabelas Silver.  
3. **Curadoria:** enriquecimento + métricas → tabelas Gold.  
4. **Consumo:** BI (PowerBI/Looker) e modelos de machine learning.

## 📊 Monitoramento e Qualidade
- Logs e retries via Airflow.  
- Validação de dados com **Great Expectations** (ex.: campos obrigatórios, ranges esperados).  
- Métricas de completude e frescor monitoradas em dashboards de observabilidade.

## ✅ Boas Práticas
- Versionamento com **Gitflow**.  
- Testes unitários e integração contínua (CI/CD).  
- Pipelines **idempotentes** (reprocessar sem duplicar dados).  
- Observabilidade e métricas desde a ingestão até o consumo.
