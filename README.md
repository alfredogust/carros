# Sistema de Gerenciamento de Concessionária de Carros

## Visão Geral

Este projeto é um Sistema de Gerenciamento de Concessionária de Carros construído com Django, proporcionando funcionalidades completas de CRUD (Create, Read, Update, Delete) para gerenciar o inventário de carros. A aplicação é projetada para implantação em larga escala utilizando AWS e uWSGI para garantir alto desempenho e confiabilidade.

## Funcionalidades

- **Operações CRUD**: Gerencie o inventário de carros com funcionalidades de criar, ler, atualizar e deletar.
- **Autenticação**: Autenticação e autorização de usuários para acesso seguro.
- **Design Responsivo**: Interface amigável que funciona em todos os dispositivos.
- **Implantação Escalável**: Utiliza AWS e uWSGI para uma implantação web escalável e eficiente.
- **Endpoints de API**: API RESTful para integração com outros serviços.

## Stack Tecnológico

- **Backend**: Django, Django REST framework
- **Frontend**: HTML, CSS, JavaScript (Bootstrap)
- **Banco de Dados**: PostgreSQL (RDS na AWS)
- **Implantação**: AWS (EC2, RDS, S3), uWSGI, Nginx

## Configuração e Instalação

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)
- PostgreSQL
- Conta AWS com permissões necessárias
- uWSGI
- Nginx
- Django DRF

### Desenvolvimento Local

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seuusuario/concessionaria-carros.git
    cd concessionaria-carros
    ```

2. **Crie e ative um ambiente virtual**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados**:
    Atualize a configuração `DATABASES` no `settings.py` para apontar para sua instância local do PostgreSQL.

5. **Execute as migrações**:
    ```bash
    python manage.py migrate
    ```

6. **Crie um superusuário**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

### Implantação na AWS

#### Configuração AWS

1. **Provisionar uma instância EC2**: 
    - Use Amazon Linux 2 ou Ubuntu.
    - Garanta que a instância tenha um grupo de segurança permitindo tráfego HTTP/HTTPS.

2. **Configurar RDS para PostgreSQL**:
    - Crie uma instância RDS para PostgreSQL.
    - Configure grupos de segurança e rede para permitir conexões da sua instância EC2.

3. **Configurar S3 para arquivos estáticos e de mídia**:
    - Crie um bucket S3.
    - Atualize `settings.py` para usar `django-storages` com S3 para arquivos estáticos e de mídia.

#### Configuração da Instância EC2

1. **SSH na instância EC2**:
    ```bash
    ssh -i caminho/para/chave.pem ec2-user@seu-ip-ec2
    ```

2. **Instalar pacotes necessários**:
    ```bash
    sudo yum update -y
    sudo yum install python3 python3-devel postgresql-devel nginx git
    ```

3. **Clone o repositório**:
    ```bash
    git clone https://github.com/seuusuario/concessionaria-carros.git
    cd concessionaria-carros
    ```

4. **Configurar um ambiente virtual e instalar dependências**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

5. **Configurar variáveis de ambiente**:
    Defina as variáveis de ambiente necessárias para o Django, como `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, etc.

6. **Executar migrações e coletar arquivos estáticos**:
    ```bash
    python manage.py migrate
    python manage.py collectstatic
    ```

7. **Configurar uWSGI**:
    Crie um arquivo `uwsgi.ini`:
    ```ini
    [uwsgi]
    module = concessionaria_carros.wsgi:application
    master = true
    processes = 5
    socket = /tmp/concessionaria_carros.sock
    chmod-socket = 660
    vacuum = true
    die-on-term = true
    ```

    Iniciar uWSGI:
    ```bash
    uwsgi --ini uwsgi.ini
    ```

8. **Configurar Nginx**:
    Atualize a configuração do Nginx para servir a aplicação Django:
    ```nginx
    server {
        listen 80;
        server_name seu-dominio.com;

        location / {
            include uwsgi_params;
            uwsgi_pass unix:/tmp/concessionaria_carros.sock;
        }

        location /static/ {
            alias /caminho/para/staticfiles;
        }

        location /media/ {
            alias /caminho/para/mediafiles;
        }
    }
    ```

    Reinicie o Nginx:
    ```bash
    sudo systemctl restart nginx
    ```

## Uso

Acesse a aplicação via seu domínio ou IP público:
```plaintext
http://seu-dominio.com
