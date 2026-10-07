<h1 align="center"; style="font-weight: bold;">School Microservices</h1>

<h3 align="center"><img  alt="Faculdade Impacta" width = "400px" src="https://www.impacta.edu.br/themes/wc_agenciar3/images/logo-new.png"></h3>

<p>
    <img src="https://img.shields.io/badge/Status-Concluído-brightgreen" alt="Status = Concluído">
    <img src="https://img.shields.io/badge/Documentação-Completa-brightgreen" alt="Documentação: Completa">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License = MIT">
</p>

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

<p align="center">
    <a href="#sobre">Sobre</a> • 
    <a href="#grupo">Integrantes do Grupo</a> •
    <a href="#requisitos">Requisitos</a> •
    <a href="#arquitetura">Arquitetura do Sistema</a> •
    <a href="sistema">Funcionalidades</a> •
    <a href="#licença">Licença</a>
</p>

<h2 id="sobre">📖 Sobre</h2>
Sistema de Microsserviços referente ao Projeto Acadêmico da Disciplina de Desenvolvimento de APIs e Microsserviços, ministrada pelo professor Giovani Bontempo na Faculdade Impacta, durante o terceiro semestre do curso Análise e Desenvolvimento de Sistemas cursado no 2º Semestre de 2025.
<br>

<h2 id="grupo">👥 Integrantes do Grupo</h2>
<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/ErickXr.png" width="100" alt="Foto"/><br>
      <b>Erick Xavier Ribeiro</b><br><br>
        <a href="https://www.linkedin.com/in/erick-xavier-0a0b572a9/" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
        <a href="https://github.com/ErickXr" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/Jloren051.png" width="100" alt="Foto"/><br>
      <b>Julia Lourenço Nogueira</b><br><br>
        <a href="https://www.linkedin.com/in/julia-louren%C3%A7o-8065082ba/" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
      <a href="https://github.com/Jloren051" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/LucasAguiarN.png" width="100"  alt="Foto"/><br>
      <b>Lucas Aguiar Nunes</b><br><br>
      <a href="https://www.linkedin.com/in/lucas-aguiar-nunes" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
      <a href="https://github.com/LucasAguiarN" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
  </tr>
</table>

<h2 id="requisitos">📦 Requisitos</h2>

[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)<br>
Tenha o Docker instalado caso queria rodar o projeto num container

No diretório raiz do projeto, construa as imagens dos containers via Docker Compose
```bash
docker-compose up --build
```

<h2 id="arquitetura">🧩 Arquitetura do Sistema</h2>
📦SchoolMicroservices<br>
 ┣ 🧩SchoolActivitiesAPI<br>
 ┃ ┣ 📂controllers<br>
 ┃ ┃ ┣ 📜atividade_controller.py<br>
 ┃ ┃ ┗ 📜nota_controller.py<br>
 ┃ ┣ 📂models<br>
 ┃ ┃ ┣ 📜__init__.py<br>
 ┃ ┃ ┣ 📜atividade.py<br>
 ┃ ┃ ┗ 📜nota.py<br>
 ┃ ┣ 🚀app.py<br>
 ┃ ┣ ⚙️config.py<br>
 ┃ ┣ 🐳Dockerfile<br>
 ┃ ┣ 📖README.md<br>
 ┃ ┣ 📦requirements.txt<br>
 ┃ ┗ 📑swagger.yml<br>
 ┣ 🧩SchoolManagerAPI<br>
 ┃ ┣ 📂controllers<br>
 ┃ ┃ ┣ 📜aluno_controller.py<br>
 ┃ ┃ ┣ 📜professor_controller.py<br>
 ┃ ┃ ┗ 📜turma_controller.py<br>
 ┃ ┣ 📂models<br>
 ┃ ┃ ┣ 📜__init__.py<br>
 ┃ ┃ ┣ 📜aluno.py<br>
 ┃ ┃ ┣ 📜professor.py<br>
 ┃ ┃ ┗ 📜turma.py<br>
 ┃ ┣ 🚀app.py<br>
 ┃ ┣ ⚙️config.py<br>
 ┃ ┣ 🐳Dockerfile<br>
 ┃ ┣ 📖README.md<br>
 ┃ ┣ 📦requirements.txt<br>
 ┃ ┗ 📑swagger.yml<br>
 ┣ 🧩SchoolReservationAPI<br>
 ┃ ┣ 📂controllers<br>
 ┃ ┃ ┗ 📜reserva_controller.py<br>
 ┃ ┣ 📂models<br>
 ┃ ┃ ┣ 📜__init__.py<br>
 ┃ ┃ ┗ 📜reserva.py<br>
 ┃ ┣ 🚀app.py<br>
 ┃ ┣ ⚙️config.py<br>
 ┃ ┣ 🐳Dockerfile<br>
 ┃ ┣ 📖README.md<br>
 ┃ ┣ 📦requirements.txt<br>
 ┃ ┗ 📑swagger.yml<br>
 ┣ 🚫.gitignore<br>
 ┣ 🐳docker-compose.yml<br>
 ┣ ⚖️LICENSE<br>
 ┗ 📖README.md<br>

<h2 id="sistema">⚙️ Funcionalidades</h2>
Para utilização do Sistema e Endpoints, pode verificar a documentação disponível de cada microserviço:
<br><a href="./SchoolActivitiesAPI/README.md">SchoolActivitiesAPI</a>
<br><a href="./SchoolManagerAPI/README.md">SchoolManagerAPI</a>
<br><a href="./SchoolReservationAPI/README.md">SchoolReservationAPI</a>

<h2 id="licença">📜 Licença</h2>
Este projeto é para fins educacionais e está disponível sob a <a href="./LICENSE">Licença MIT.</a>