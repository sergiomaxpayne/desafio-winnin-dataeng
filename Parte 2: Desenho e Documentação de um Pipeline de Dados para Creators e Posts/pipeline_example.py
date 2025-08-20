
---

## 📑 4. `pipeline_example.py`

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract_creators():
    print("Extraindo dados da Wikipedia API (creators)...")

def extract_posts():
    print("Extraindo dados da YouTube API (posts)...")

def transform():
    print("Transformando dados no Spark/Databricks...")

def load():
    print("Carregando dados tratados em Silver/Gold...")

with DAG(
    "pipeline_creators_posts",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="extract_creators", python_callable=extract_creators)
    t2 = PythonOperator(task_id="extract_posts", python_callable=extract_posts)
    t3 = PythonOperator(task_id="transform", python_callable=transform)
    t4 = PythonOperator(task_id="load", python_callable=load)

    [t1, t2] >> t3 >> t4
