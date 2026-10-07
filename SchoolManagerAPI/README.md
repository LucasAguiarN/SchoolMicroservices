<h1 align="center"; style="font-weight: bold;">School Manager API</h1>

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
    <a href="#requisitos">Requisitos</a> •
    <a href="#arquitetura">Arquitetura do Sistema</a> •
    <a href="#how-it-works">Funcionalidades</a> •
    <a href="#endpoints">Endpoints da API</a>
</p>

<h2 id="sobre">📖 Sobre</h2>
API referente ao Projeto Acadêmico da Disciplina de Desenvolvimento de APIs e Microsserviços, ministrada pelo professor Giovani Bontempo na Faculdade Impacta, durante o terceiro semestre do curso Análise e Desenvolvimento de Sistemas cursado no 2º Semestre de 2025.
<br><br>O projeto consiste em uma API RESTful construída com Flask para realizar o gerenciamento de Professores, Turmas e Alunos de uma instituição de ensino.
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

[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/) <img src="https://img.shields.io/badge/python-3.13.2-blue" alt="Python = 3.13.2"><br>

Tenha o Docker instalado caso queria rodar o projeto num container

No diretório raiz do projeto, construa a imagem do container
```bash
docker build -t school-manager .
```
Execute o container
```bash
docker run --name school-manager-container -p 5000:5000 school-manager
```

Para rodar localmente sem ser via container tenho o Python instalado e no diretório raiz do projeto execute o comando para instalar as bibliotecas<br>

```bash
pip install -r requirements.txt
```

<h2 id="arquitetura">🧩 Arquitetura do Sistema</h2>
📦SchoolManagerAPI<br>
 ┣ 📂controllers<br>
 ┃ ┣ 📜aluno_controller.py<br>
 ┃ ┣ 📜professor_controller.py<br>
 ┃ ┗ 📜turma_controller.py<br>
 ┣ 📂models<br>
 ┃ ┣ 📜__init__.py<br>
 ┃ ┣ 📜aluno.py<br>
 ┃ ┣ 📜professor.py<br>
 ┃ ┗ 📜turma.py<br>
 ┣ 🚀app.py<br>
 ┣ ⚙️config.py<br>
 ┣ 🐳Dockerfile<br>
 ┣ 📖README.md<br>
 ┣ 🧩requirements.txt<br>
 ┗ 📑swagger.yml<br>

<h2 id="how-it-works">⚙️ Funcionalidades</h2>
🔹 CRUD de Alunos (Cadastro, Listagem, Atualização e Exclusão)
<br>🔹 CRUD de Professors (Cadastro, Listagem, Atualização e Exclusão)
<br>🔹 CRUD de Turmas (Cadastro, Listagem, Atualização e Exclusão)

<h2 id="endpoints">🛠️ Endpoints da API</h2>

Documentação Swagger
```bash
curl -X GET http://localhost:5000/apidocs
```
Listagem de Professores
```bash
curl -X GET http://localhost:5000/professores
```
Cadastro de Professor
```bash
curl -X POST http://localhost:5000/professores \
    -H "Content-Type: application/json" \
    -d '{
          "nome":"Carlos",
          "idade":"32", 
          "materia":"Microserviços",
          "observacoes":""
        }'
```
Exibir Professor
```bash
curl -X GET http://localhost:5000/professores/{professor_id}
```
Atualizar Professor
```bash
curl -X PUT http://localhost:5000/professores/{professor_id} \
    -H "Content-Type: application/json" \
    -d '{
          "nome":"Carlos",
          "idade":"32", 
          "materia":"Mobile",
          "observacoes":""
        }'
```
Deletar Professor
```bash
curl -X DELETE http://localhost:5000/professores/{professor_id}
```
Listagem de Turmas
```bash
curl -X GET http://localhost:5000/turmas
```
Cadastro de Turma
```bash
curl -X POST http://localhost:5000/turmas \
    -H "Content-Type: application/json" \
    -d '{
          "descricao":"ADS Periodo Manha", 
          "ativo":"True",
          "professor_id":"1"
        }'
```
Exibir Turma
```bash
curl -X GET http://localhost:5000/turmas/{turma_id}
```
Atualizar Turma
```bash
curl -X PUT http://localhost:5000/turmas/{turma_id} \
    -H "Content-Type: application/json" \
    -d '{
          "descricao":"ADS Periodo Manha", 
          "ativo":"False",
          "professor_id":"1"
        }'
```
Deletar Turma
```bash
curl -X DELETE http://localhost:5000/turmas/{turma_id}
```
Listagem de Alunos
```bash
curl -X GET http://localhost:5000/alunos
```
Cadastro de Alunos
```bash
curl -X POST http://localhost:5000/alunos \
    -H "Content-Type: application/json" \
    -d '{
          "nome":"Lucas",
          "idade":"27", 
          "data_nasc":"18/11/1998",
          "turma_id":"1"
        }'
```
Exibir Aluno
```bash
curl -X GET http://localhost:5000/alunos/{aluno_id}
```
Atualizar Aluno
```bash
curl -X PUT http://localhost:5000/alunos/{aluno_id} \
    -H "Content-Type: application/json" \
    -d '{
          "nome":"Lucas",
          "idade":"27", 
          "data_nasc":"18/11/1998",
          "turma_id":"1"
        }'
```
Deletar Alunos
```bash
curl -X DELETE http://localhost:5000/alunos/{aluno_id}
```

<h2 id="licença">📜 Licença</h2>
Este projeto é para fins educacionais e está disponível sob a <a href="./LICENSE">Licença MIT.</a>
