"""
 arquivo principal 

 constrola entradas e saidas

 # __init__.py no pacote my_app
from .routes import router  # Importa e expõe o router do módulo routes
from .utils import helper_function  # Exemplo de função utilitária exportada

__all__ = ["router", "helper_function"]  # Define explicitamente o que será exportado
"""


"""
auth/
Subdiretório específico para lidar com autenticação.
Contém rotas, lógica de hashing (senhas) e geração de tokens JWT,
equivalente ao que você criaria em Express.js com middlewares e serviços.
"""