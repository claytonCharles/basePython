# Requisito principal
=> Baixar o Python Globalmete na maquina! Href="https://www.python.org/"

# Inicializando Clone

=> Ao fazer o clone do repositorio, caso queira para sites, basta seguir o ultimo item da lista # Inicializando Clone.
=> Caso queira para API, siga para a lista abaixo # Configurações adicionais para API, nos ultimos itens.
=> abrir o terminal e entra na pasta raiz no projeto, e digitar - ( py manage.py runserver )


# Criação do sistema

=> Criar o env local dentro na pasta no terminal digite - ( py -m venv nomeDeSuaEscolha || python -m venv nomeDeSuaEscolha ).
=> Ativar o env local no terminal digite - ( .\nomeEscolhido\Scripts\activate ).
=> Fazer o upgrade do pip - (python.exe -m pip install --upgrade pip)
=> Instalar o framework Django - (pip install django || pip install flask)
=> Iniciar a primeira pasta do framework desejada, na pasta raiz do projeto - ( django-admin startproject nomeDesejado1 . )
=> Iniciar o manage.py para finalizar este processo - ( py manage.py startapp nomeDesejado2)
=> Finalizado, sua pasta raiz deve ter 3 pastas, e 1 arquivo manage.py!

# Configurações iniciais basicas

=> Para conseguir desenvolver você deve liberar o acesso ao localhost, indo em nomeDesejado1/settings.py
    achando ALLOWED_HOSTS = [] e habilitando seu ip local, ALLOWED_HOSTS = ['localhost']
    caso contratio não conseguirar rodar o servidor.
=> Logo após no mesmo arquivo adicionar a nomeDesejado2, na lista de **INSTALLED_APPS**
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nomeDesejado2',
]

# Configurações adicionais para API

=> Instalar os cors da API desejada, no caso estou utilzando o Django - ( pip install django-cors-headers ).
=> Configurando os cors da API indo em nomeDesejado1/settings.py localizar **INSTALLED_APPS** e adicionar -> 'corsheaders',
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nomeDesejado2',
    'corsheaders',
]

=> No mesmo arquivo em **MIDDLEWARE**, adicionar -> 'corsheaders.middleware.CorsMiddleware',
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

=> No mesmo arquivo de configuração, adicionar mais 2 variaveis.
CORS_ORIGIN_ALLOW_ALL = False || True
CORS_ORIGIN_WHITELIST = ()

=> CORS_ORIGIN_ALLOW_ALL = False, ninguem conseguirar fazer requisições a api || True e aberto para todos.
=> No caso de limitar apenas alguns para acessar a API, CORS_ORIGIN_ALLOW_ALL = False, e configurar o,
    CORS_ORIGIN_WHITELIST com os ips desejados!, um exemplo liberando a porta para desenvolvimento local com REACT,
    CORS_ORIGIN_WHITELIST = ('localhost:3000/',)

# Configurações de Rotas

=> As rotas são recebidas em nomeDesejado1/urls.py, com um exemplo de como chamar uma view.

from django.contrib import admin
from django.urls import path
from nomeDesejado2.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', Home),
]

=> Como mostrado no exemplo acima, as chamadas de views/serviços são feita na nomeDesejado2/views.py

# iniciando o servidor

=> Para rodar o servidor basta digitar no terminal - ( py manage.py runserver )