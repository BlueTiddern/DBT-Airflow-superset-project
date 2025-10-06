
# DBT-Airflow-Superset Project

This project is an orchestration of an end-to-end data pipeline, starting from collecting weather data using the Weather Stack API, parsing and processing with Python, staging the data into PostgreSQL, transforming and managing it with DBT, visualizing results in Apache Superset, and orchestrating the workflow using Apache Airflow.

---

## 🚀 Project Overview

- **Data Source:** Weather Stack API
- **Processing:** Python scripts
- **Staging:** PostgreSQL database
- **Transformation:** DBT (Data Build Tool)
- **Visualization:** Apache Superset dashboards
- **Orchestration:** Apache Airflow DAGs

---

## 🏗️ Architecture

graph LR
    A[Weather Stack API] --> B[Python Parser]
    
    B --> C[PostgreSQL]
    
    C --> D[DBT Transformations]
    
    D --> E[PostgreSQL (Transformed)]
    
    E --> F[Apache Superset]
    
    A & B & C & D & E & F --> G[Apache Airflow]

---

## 📂 Main Technologies

- **Python** (93.7%)
- **HTML** (5.2%)
- **C++** (0.8%)
- **C** (0.2%)
- **Cython** (0.1%)
- **Shell**

---

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/BlueTiddern/DBT-Airflow-superset-project.git
   cd DBT-Airflow-superset-project
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup PostgreSQL**
   - Ensure PostgreSQL is running.
   - Configure your database credentials in the project’s configuration files.

4. **Configure DBT**
   - Update your `profiles.yml` with the correct connection details.

5. **Setup Apache Airflow**
   - Initialize the Airflow database:
     ```bash
     airflow db init
     ```
   - Add your DAGs from the repository.
   - Start Airflow webserver and scheduler.

6. **Setup Apache Superset**
   - Follow [Superset’s official installation guide](https://superset.apache.org/docs/installation/installing-superset-from-scratch).

7. **Run the Pipeline**
   - Use Airflow to trigger the end-to-end workflow.

---

## ✨ Features

- Automated weather data collection and ingestion.
- Robust data transformations with DBT models.
- Powerful data visualizations in Superset dashboards.
- Fully orchestrated workflows with Airflow.
- Modular and extensible pipeline design.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

- [BlueTiddern](https://github.com/BlueTiddern)

---

> Feel free to contribute, suggest improvements, or open issues!
