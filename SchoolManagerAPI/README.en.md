<h1 align="center"; style="font-weight: bold;">School Manager API</h1>

<h3 align="center"><img  alt="Impacta College" width = "400px" src="https://www.impacta.edu.br/themes/wc_agenciar3/images/logo-new.png"></h3>

<p>
    <img src="https://img.shields.io/badge/Status-Completed-brightgreen" alt="Status = Completed">
    <img src="https://img.shields.io/badge/Documentation-Complete-brightgreen" alt="Documentation: Complete">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License = MIT">
    <a href="./README.md" target="_blank"><img title="PT-BR" src="https://img.shields.io/badge/docs-pt--BR-blue" alt="README PT-BR"></a>
    <a href="./README.en.md" target="_blank"><img title="EN-US" src="https://img.shields.io/badge/docs-en--US-blue" alt="README EN-US"></a>
</p>

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

<p align="center">
    <a href="#about">About</a> • 
    <a href="#requirements">Requirements</a> •
    <a href="#architecture">System Architecture</a> •
    <a href="#how-it-works">Features</a> •
    <a href="#endpoints">API Endpoints</a>
</p>

<h2 id="about">📖 About</h2>
API for the Academic Project of the API and Microservices Development course, taught by professor Giovani Bontempo at Impacta College, during the third semester of the Systems Analysis and Development program, taken in the 2nd semester of 2025.
<br><br>The project consists of a RESTful API built with Flask to manage Teachers, Classes, and Students for an educational institution.
<br>

<h2 id="team">👥 Team Members</h2>
<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/ErickXr.png" width="100" alt="Photo"/><br>
      <b>Erick Xavier Ribeiro</b><br><br>
        <a href="https://www.linkedin.com/in/erick-xavier-0a0b572a9/" target="_blank"><img title="Connect" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Profile"/></a>
        <a href="https://github.com/ErickXr" target="_blank"><img title="Follow me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/Jloren051.png" width="100" alt="Photo"/><br>
      <b>Julia Lourenço Nogueira</b><br><br>
        <a href="https://www.linkedin.com/in/julia-louren%C3%A7o-8065082ba/" target="_blank"><img title="Connect" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Profile"/></a>
      <a href="https://github.com/Jloren051" target="_blank"><img title="Follow me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/LucasAguiarN.png" width="100"  alt="Photo"/><br>
      <b>Lucas Aguiar Nunes</b><br><br>
      <a href="https://www.linkedin.com/in/lucas-aguiar-nunes" target="_blank"><img title="Connect" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Profile"/></a>
      <a href="https://github.com/LucasAguiarN" target="_blank"><img title="Follow me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile"/></a>
    </td>
  </tr>
</table>

<h2 id="requirements">📦 Requirements</h2>

[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/) <img src="https://img.shields.io/badge/python-3.13.2-blue" alt="Python = 3.13.2"><br>

Make sure Docker is installed if you want to run the project in a container

In the project's root directory, build the container image
```bash
docker build -t school-manager .
```
Run the container
```bash
docker run --name school-manager-container -p 5000:5000 school-manager
```

To run locally without a container, make sure Python is installed, and in the project's root directory run the command to install the libraries<br>

```bash
pip install -r requirements.txt
```

<h2 id="architecture">🧩 System Architecture</h2>
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

<h2 id="how-it-works">⚙️ Features</h2>
🔹 Student CRUD (Create, List, Update, and Delete)
<br>🔹 Teacher CRUD (Create, List, Update, and Delete)
<br>🔹 Class CRUD (Create, List, Update, and Delete)

<h2 id="endpoints">🛠️ API Endpoints</h2>

Swagger Documentation
```bash
curl -X GET http://localhost:5000/apidocs
```
List Teachers
```bash
curl -X GET http://localhost:5000/professores
```
Create Teacher
```bash
curl -X POST http://localhost:5000/professores \
    -H "Content-Type: application/json" \
    -d '{
          "nome": "Carlos",
          "idade": 32, 
          "materia": "Microserviços",
          "observacoes":""
        }'
```
View Teacher
```bash
curl -X GET http://localhost:5000/professores/{professor_id}
```
Update Teacher
```bash
curl -X PUT http://localhost:5000/professores/{professor_id} \
    -H "Content-Type: application/json" \
    -d '{
          "nome": "Carlos",
          "idade": 32, 
          "materia": "Mobile",
          "observacoes":""
        }'
```
Delete Teacher
```bash
curl -X DELETE http://localhost:5000/professores/{professor_id}
```
List Classes
```bash
curl -X GET http://localhost:5000/turmas
```
Create Class
```bash
curl -X POST http://localhost:5000/turmas \
    -H "Content-Type: application/json" \
    -d '{
          "descricao": "ADS Periodo Manha", 
          "ativo": "True",
          "professor_id": 1
        }'
```
View Class
```bash
curl -X GET http://localhost:5000/turmas/{turma_id}
```
Update Class
```bash
curl -X PUT http://localhost:5000/turmas/{turma_id} \
    -H "Content-Type: application/json" \
    -d '{
          "descricao": "ADS Periodo Manha", 
          "ativo": "False",
          "professor_id": 1
        }'
```
Delete Class
```bash
curl -X DELETE http://localhost:5000/turmas/{turma_id}
```
List Students
```bash
curl -X GET http://localhost:5000/alunos
```
Create Student
```bash
curl -X POST http://localhost:5000/alunos \
    -H "Content-Type: application/json" \
    -d '{
          "nome": "Lucas",
          "idade": 27, 
          "data_nasc": "18/11/1998",
          "turma_id": 1
        }'
```
View Student
```bash
curl -X GET http://localhost:5000/alunos/{aluno_id}
```
Update Student
```bash
curl -X PUT http://localhost:5000/alunos/{aluno_id} \
    -H "Content-Type: application/json" \
    -d '{
          "nome": "Lucas",
          "idade": 27, 
          "data_nasc": "18/11/1998",
          "turma_id": 1
        }'
```
Delete Student
```bash
curl -X DELETE http://localhost:5000/alunos/{aluno_id}
```