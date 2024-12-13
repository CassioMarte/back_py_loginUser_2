# back_py_loginUser_2

user_auth_backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # Ponto de entrada da aplicação
│   ├── config.py          # Configurações da aplicação
│   ├── database.py        # Conexão e gerenciamento do banco de dados
│   ├── models.py          # Modelos do SQLAlchemy
│   ├── schemas.py         # Esquemas Pydantic (validação e tipagem)
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py      # Rotas de autenticação
│   │   ├── services.py    # Lógica de autenticação (hashing e geração de tokens)
│   │   ├── dependencies.py # Middleware de autenticação
│   └── utils/
│       └── __init__.py    # Utilitários gerais
│
├── requirements.txt       # Dependências do projeto
└── .env                   # Variáveis de ambiente
