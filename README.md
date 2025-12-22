# InfoHelp v2

## Sobre o projeto
O **InfoHelp v2** é a segunda versão do sistema [Descreva aqui o propósito, ex: de Help Desk / Suporte de TI / Base de Conhecimento]. Este projeto foi desenvolvido para facilitar o gerenciamento de solicitações e a organização de informações.

## Tecnologias Utilizadas
* [cite_start]**Linguagem:** Python 3.11.9 [cite: 5]
* [cite_start]**Framework:** Django 5.2.7 [cite: 6]
* [cite_start]**Banco de Dados:** SQLite (padrão do Django) [cite: 7]
* **Front-end:** [HTML / CSS / Tailwind CSS / JavaScript]
* [cite_start]**Outras bibliotecas:** [django-tailwind / (demais dependências listadas no requirements.txt)] [cite: 8]

## Pré-requisitos
Antes de começar, certifique-se de ter instalado em sua máquina:
* [cite_start]Python 3.8 ou superior [cite: 10]
* [cite_start]Git [cite: 12]
* [cite_start][MySQL ou PostgreSQL - caso utilize um banco diferente do SQLite] [cite: 11]

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

### 1. Clone o repositório
```bash
git clone [https://github.com/tonhoantunes/infohelp-v2.git](https://github.com/tonhoantunes/infohelp-v2.git)
cd infohelp-v2
```

### 2. Crie e ative um ambiente virtual
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
Este comando irá instalar todas as bibliotecas necessárias listadas no arquivo requirements.txt:
```bash
pip install -r requirements.txt
```

### 4. Execute as migrações do banco de dados
```bash
python manage.py migrate
````

### 5. (Opcional) Crie um superusuário
````bash
python manage.py createsuperuser
````

### 6. Execute o servidor
````bash
python manage.py runserver
````
Acesse o projeto em seu navegador através do endereço: http://localhost:8000

### Estrutura do Projeto
````plaintext
infohelp-v2/
│
├── config/              # Configurações do projeto Django
├── infohelp/            # Aplicação principal
├── scripts/             # Scripts auxiliares
├── usuarios/            # Aplicação de usuários e autenticação
│
├── .gitignore           # Arquivos ignorados pelo Git
├── HIERARQUIA.md        # Documentação detalhada de cargos, permissões e regras de negócio
├── README.md            # Este arquivo
├── manage.py            # Script principal do Django
├── requirements.txt     # Dependências do projeto
├── run_migrations.py    # Automação para criar e aplicar migrações (foco em usuários)
````

### Funcionalidades

1. Autenticação de usuários (registro, login e logout)
2. Gestão de conteúdo (cursos e aulas)
3. Área do Aluno (dashboard personalizado, biblioteca, perfil do usuário) 
4. Interface e Experiência (UI/UX)

### Manual do Usuário

Para instruções detalhadas sobre o uso do sistema, consulte o Manual do Usuário disponível em: [Manual do Usuário](https://github.com/tonhoantunes/manual-user-infohelp-v2)

### Autores

1. Antônio Antunes
2. Pedro Isaac
3. João Maria
