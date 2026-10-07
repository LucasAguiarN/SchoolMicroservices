<h1 align="center"; style="font-weight: bold;">School Reservation API</h1>

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
<br><br>The project consists of a RESTful API built with Flask to manage Reservations at an educational institution.
<br>

<h2 id="requirements">📦 Requirements</h2>

[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/) <img src="https://img.shields.io/badge/python-3.13.2-blue" alt="Python = 3.13.2"><br>

Make sure Docker is installed if you want to run the project in a container

In the project's root directory, build the container image
```bash
docker build -t school-reservation .
```
Run the container
```bash
docker run --name school-reservation-container -p 5002:5002 school-reservation
```

To run locally without a container, make sure Python is installed, and in the project's root directory run the command to install the libraries<br>

```bash
pip install -r requirements.txt
```

<h2 id="architecture">🧩 System Architecture</h2>
📦SchoolReservationAPI<br>
 ┣ 📂controllers<br>
 ┃ ┗ 📜reserva_controller.py<br>
 ┣ 📂models<br>
 ┃ ┣ 📜__init__.py<br>
 ┃ ┗ 📜reserva.py<br>
 ┣ 🚀app.py<br>
 ┣ ⚙️config.py<br>
 ┣ 🐳Dockerfile<br>
 ┣ 📖README.md<br>
 ┣ 🧩requirements.txt<br>
 ┗ 📑swagger.yml<br>

<h2 id="how-it-works">⚙️ Features</h2>
🔹 Reservation CRUD (Create, List, Update, and Delete)

<h2 id="endpoints">🛠️ API Endpoints</h2>

Swagger Documentation
```bash
curl -X GET http://localhost:5002/apidocs
```
List Reservations
```bash
curl -X GET http://localhost:5002/reservas
```
Create Reservation
```bash
curl -X POST http://localhost:5002/reservas \
    -H "Content-Type: application/json" \
    -d '{
            "num_sala": 101,
            "lab": "True",
            "data": "10/10/2025",
            "turma_id": 1
        }'
```
View Reservation
```bash
curl -X GET http://localhost:5002/reservas/{reserva_id}
```
Update Reservation
```bash
curl -X PUT http://localhost:5002/reservas/{reserva_id} \
    -H "Content-Type: application/json" \
    -d '{
            "num_sala": 202,
            "lab": "False",
            "data": "10/10/2025",
            "turma_id": 1
        }'
```
Delete Reservation
```bash
curl -X DELETE http://localhost:5002/reservas/{reserva_id}
```