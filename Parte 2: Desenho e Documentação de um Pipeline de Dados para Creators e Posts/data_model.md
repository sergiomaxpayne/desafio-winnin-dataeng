# 📊 Modelagem de Dados

## Entidades Principais

### 1. Creators
| Campo         | Tipo     | Descrição                           |
|---------------|---------|-------------------------------------|
| creator_id    | STRING  | Identificador único do criador       |
| name          | STRING  | Nome do criador                     |
| channel_url   | STRING  | Link para o canal/perfil             |
| country       | STRING  | País de origem                      |
| category      | STRING  | Categoria/segmento do criador        |
| created_at    | TIMESTAMP | Data de criação do registro        |

---

### 2. Posts
| Campo         | Tipo     | Descrição                           |
|---------------|---------|-------------------------------------|
| post_id       | STRING  | Identificador único da postagem      |
| creator_id    | STRING  | Chave estrangeira (tabela creators)  |
| title         | STRING  | Título da postagem                   |
| published_at  | TIMESTAMP | Data de publicação                 |
| views         | INT     | Número de visualizações              |
| likes         | INT     | Número de curtidas                   |
| tags          | ARRAY<STRING> | Lista de tags associadas       |

---

### 3. Daily Engagement
| Campo         | Tipo     | Descrição                           |
|---------------|---------|-------------------------------------|
| post_id       | STRING  | Chave estrangeira (tabela posts)     |
| date          | DATE    | Data da métrica                     |
| views         | INT     | Visualizações no dia                 |
| likes         | INT     | Curtidas no dia                      |
| comments      | INT     | Comentários no dia                   |

---

## Relacionamentos
- Um **creator** → muitos **posts**  
- Um **post** → várias métricas no **daily_engagement**
