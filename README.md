# PySpark CI with GitHub Actions

[![PySpark CI](https://github.com/SayedELMASRY2/Deployment/actions/workflows/ci.yml/badge.svg)](https://github.com/SayedELMASRY2/Deployment/actions/workflows/ci.yml)
![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.13-blue.svg)
![PySpark](https://img.shields.io/badge/pyspark-3.5.6-orange.svg)
![PyTest](https://img.shields.io/badge/pytest-8.4.2-brightgreen.svg)
![Java](https://img.shields.io/badge/JDK-17%20(Temurin)-red.svg)

This repository contains an automated data processing pipeline implemented using **Apache PySpark**, equipped with unit testing via **pytest** and a Continuous Integration (CI) workflow configured with **GitHub Actions**.

---

## 📌 Project Overview

The objective of this project is to implement a robust data cleaning pipeline in PySpark and establish an automated CI pipeline that tests all incoming changes on every **Pull Request** before merging into the `main` branch.

### Key Features
- **Data Cleansing Logic (`pyspark_job.py`):**
  - Filters out records where `amount <= 0`.
  - Filters out records where `name` is `NULL`.
  - Adds a new column `amount_with_tax` calculated as `amount * 1.20`.
- **Unit Testing Suite (`test_pyspark_job.py`):**
  - PySpark unit tests using `pytest` verifying boundary and edge cases.
  - Deterministic assertions utilizing `.orderBy("id")` to prevent multi-partition shuffle non-determinism.
- **Continuous Integration (`.github/workflows/ci.yml`):**
  - Triggers automatically whenever a Pull Request is opened, synchronized, or reopened.
  - Provisions a complete runner environment including **Python 3.10** and **Java JDK 17 (Temurin)** (required by the Spark JVM engine).
  - Executes unit tests automatically and gates PR merging.

---

## 📁 Repository Structure

```text
spark-project/
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI workflow configuration
├── pyspark_job.py               # PySpark data processing & clean_data function
├── test_pyspark_job.py          # PyTest unit tests for clean_data
├── requirements.txt             # Pinned dependencies (pyspark==3.5.6, pytest==8.4.2)
└── README.md                    # Project documentation
```

---

## 🚀 Quick Start (Local Setup)

### 1. Prerequisites
- **Python 3.10+**
- **Java (JDK 8, 11, or 17)**: Required by Apache Spark. Ensure `JAVA_HOME` environment variable is set.

### 2. Clone the Repository
```bash
git clone https://github.com/SayedELMASRY2/Deployment.git
cd Deployment
```

### 3. Create a Virtual Environment & Install Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Linux / macOS:
source venv/bin/activate

# Install exact pinned requirements
pip install -r requirements.txt
```

### 4. Run Unit Tests Locally
```bash
pytest -v
```

Expected output:
```text
test_pyspark_job.py::test_clean_data PASSED                      [100%]
============================== 1 passed in ... ==============================
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

The workflow defined in `.github/workflows/ci.yml` executes on every Pull Request targeting `main`:

```text
[ Pull Request Opened / Updated ]
                │
                ▼
      [ 1. Checkout Code ]
                │
                ▼
     [ 2. Set up Python 3.10 ]
                │
                ▼
     [ 3. Set up Java JDK 17 ]
                │
                ▼
  [ 4. Install requirements.txt ]
                │
                ▼
       [ 5. Run pytest -v ]
                │
        ┌───────┴───────┐
        ▼               ▼
 [ Tests Passed ✅ ] [ Tests Failed ❌ ]
        │               │
        ▼               ▼
 [ Merge Allowed ]  [ Merge Blocked ]
```

---

## 📊 Verification & Test Results

| Requirement | Implementation Detail | Status |
| :--- | :--- | :---: |
| **Remove `amount <= 0`** | `df.filter(F.col("amount") > 0)` | ✅ Verified |
| **Remove NULL names** | `df.filter(F.col("name").isNotNull())` | ✅ Verified |
| **Calculate `amount_with_tax`** | `.withColumn("amount_with_tax", F.col("amount") * 1.20)` | ✅ Verified |
| **PySpark Unit Tests** | Automated test fixtures covering all boundary cases | ✅ Passed |
| **GitHub Actions CI on PR** | Auto-triggered workflow with Python 3.10 and Java 17 | ✅ Passed (27s) |


