# Dermasys

**Dermasys** é um sistema web desenvolvido com Django para gestão de processos voltados à área dermatológica (ou ajuste conforme teu foco). O projeto tem como objetivo facilitar o gerenciamento de atendimentos, prontuários, agendamentos e outras funcionalidades essenciais para clínicas e profissionais da área.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Django 4.x
- SQLite (ou outro banco que estiver usando)
- HTML/CSS/JS
- Bootstrap (se aplicável)

---

## 📦 Instalação e uso local

1. Clone o repositório:

```bash
git init
git remote add origin https://github.com/MateusZeferino/Dermasys.git
git branch -M main

git pull origin main --allow-unrelated-histories
git push -u origin main

2. Crie e ative um ambiente virtual:

```terminal 
python -m venv venv

# Windows
venv\Scripts\activate.ps1

# Linux/Mac
source venv/bin/activate.ps1

3. Instale as dependências

```Terminal
pip install -r requirements.txt

4. Rode as migrações:

python manage.py migrate