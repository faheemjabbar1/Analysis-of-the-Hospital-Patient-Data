🧠 Stroke Risk Analytics System

A modular Python-based analytics system designed to analyze and evaluate stroke risk factors using anonymized patient health records.
This project was developed as part of Programming Concepts and Practice (55-706555) coursework, focusing on data preprocessing, risk factor analysis, modular design, and ethical considerations in healthcare analytics.

📌 Table of Contents

Overview

Features

System Architecture

Tech Stack

Installation

Usage

Example Queries

Exporting Results

Challenges & Limitations

Ethics & Interpretability

Future Work

References

📖 Overview

Stroke is a leading global health threat, responsible for millions of deaths and disabilities each year.
This project develops a Python-based, modular, command-line analytics system to identify and evaluate behavioural and clinical risk factors of stroke, such as:

Hypertension

Smoking

Sleep patterns

Cardiovascular comorbidities

The system is designed to be scalable, interpretable, and user-friendly, targeting both academic and clinical use cases

Assessment Draft

.

✨ Features

Modular Design → dataset_module, query_module, bimodule for flexibility and scalability.

Data Preprocessing → Handles missing values, inconsistent labels, and categorical encoding.

Descriptive & Advanced Analytics → Supports subgroup analysis, cross-tab queries, and statistical summaries.

Sleep/Stroke Analysis → Evaluates the relationship between sleep hours and stroke risk.

User Interface → Interactive Command Line Interface (CLI) with color-coded outputs for accessibility.

CSV Export → Query results can be exported for reuse, replication, and audits.

🏗️ System Architecture
+------------------+
| dataset_module   | --> Data ingestion, cleaning, encoding
+------------------+
| query_module     | --> Analytical queries & subgroup comparisons
+------------------+
| bimodule         | --> Core logic & integration
+------------------+
| UI/CLI           | --> User interaction & navigation
+------------------+
| Export Engine    | --> Save results to CSV for reuse

🛠️ Tech Stack

Language: Python 3.10+

Libraries:

pandas, numpy → Data preprocessing & analysis

matplotlib, seaborn → Data visualization

colorama → CLI color-coded menus

Environment: CLI-based for wide compatibility in healthcare settings

🚀 Installation

Clone this repo:

git clone https://github.com/your-username/stroke-risk-analytics.git
cd stroke-risk-analytics


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt

🎯 Usage

Run the CLI application:

python main.py


Follow the menu to:

Load dataset

Run descriptive statistics

Query risk factors (e.g., hypertension + smoking overlap)

Compare stroke incidence by sleep duration

Export results to CSV

🔍 Example Queries

Stroke prevalence among smokers with hypertension

Cross-tabulation of residence type vs. stroke incidence

Average sleep duration comparison (stroke-positive vs stroke-negative patients)

📤 Exporting Results

Results can be saved to CSV for reuse:

results/export_query_results.csv


These files are:

Standardized (readable by Excel/SPSS/clinical tools)

Useful for peer validation & clinical audits

⚠️ Challenges & Limitations

Missing & inconsistent values (esp. sleep and smoking data).

No direct integration with electronic health records yet.

CLI interface may limit adoption compared to GUI.

🧩 Ethics & Interpretability

Transparency first: Modular, traceable queries instead of black-box AI.

Data anonymization applied.

Export & auditability ensures replicability in clinical research.

🔮 Future Work

Integration with machine learning risk prediction models.

Expansion to longitudinal data tracking.

GUI-based interface for wider accessibility.
