# 📊 NGO Education Analytics Dashboard

## 🚀 Overview

This project is an end-to-end data analytics solution built to monitor and evaluate student performance across NGO learning centers. It processes raw student data, generates insights, and visualizes key metrics using interactive dashboards.

---

## 🎯 Objectives

* Analyze student attendance and performance
* Identify learning trends across centers
* Provide actionable insights for NGOs

---

## 🛠️ Tech Stack

* **Python** (Data Processing)
* **SQL (SQLite)** (Data Storage)
* **Power BI** (Data Visualization)

---

## ⚙️ Project Workflow

1. **Data Collection**

   * Raw student data stored in CSV format

2. **Data Processing (Python)**

   * Cleaned and transformed data
   * Added performance classification

3. **Data Storage (SQL)**

   * Stored processed data in SQLite database

4. **Data Visualization (Power BI)**

   * Created interactive dashboards

---

## ▶️ How to Run the Project

### Step 1: Run Python Script

```bash
cd scripts
python data_processing.py
```

### Step 2: Check Output

* `processed_data.csv` will be generated inside `data/`

### Step 3: Open Dashboard

* Open Power BI Desktop
* Load `processed_data.csv`
* View dashboard

---

## 📊 Key Features

* Attendance analysis by center
* Student performance classification
* Score distribution insights
* Interactive filters and KPIs

---

## 📁 Project Structure

```
ngo_dashboard_project/
│
├── data/
│   ├── sample_data.csv
│   ├── processed_data.csv
│   └── ngo.db
│
├── scripts/
│   └── data_processing.py
│
├── dashboard/
│   └── app.py
│
├── sql/
│   └── schema.sql
│
└── README.md
```

---

## 📈 Sample Insights

* Average attendance across centers
* Performance distribution (Good / Needs Improvement)
* Center-wise student performance

---

## 💡 Future Improvements

* Add AI-based student performance prediction
* Build real-time dashboard
* Deploy as web application

---

## 👤 Author

* Your Name

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
