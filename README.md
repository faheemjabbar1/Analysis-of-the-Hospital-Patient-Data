# Stroke-Risk-Analytics  

---

## 📌 Introduction
This project develops a **modular Python-based analytics system** to study the risk factors of **stroke incidence** using anonymized patient health records.  
The system focuses on **behavioural and clinical predictors** such as **hypertension, smoking status, and sleep patterns**, aiming to support **public health insights, clinical audits, and educational applications**.  

The motivation is to design a framework that is **interpretable, auditable, and ethically aligned** with healthcare data practices, while enabling **scalable analysis** for both descriptive and comparative studies.  

---

## 📊 Dataset
- **Source:** Anonymized patient health records  
- **Features:**  
  - Stroke outcome (Yes/No)  
  - Hypertension (binary)  
  - Smoking status (categorical)  
  - Sleep hours (numeric)  
  - Diabetes, residence type, and comorbidities  
- **Data Challenges:**  
  - Missing and inconsistent values (esp. sleep & smoking)  
  - Non-standardized categorical labels  
  - Required preprocessing for cleaning and encoding  

Preprocessing ensured uniformity and validity of the dataset for epidemiological analysis.  

---

## ⚙️ Methodology
The methodology follows a **modular, CLI-based analytical approach** implemented in Python.  

### 1. System Architecture
- **dataset_module:** Data ingestion, validation, and cleaning  
- **query_module:** Analytical queries for risk factor relationships  
- **bimodule:** Core logic combining results and extensions  
- **UI (CLI):** User-friendly menu-driven interface  
- **Export Engine:** Saves query outputs into CSV files  

### 2. Analytical Queries
- Stroke prevalence among **hypertensive smokers**  
- Cross-tabulation of **residence type vs. stroke incidence**  
- Average **sleep hours** comparison between stroke-positive and negative groups  
- Descriptive statistics (distribution, central tendency, subgroup breakdowns)  

### 3. User Interface
- Command-Line Interface (CLI) with **color-coded menus** (via `colorama`)  
- Designed for accessibility in **low-resource environments**  
- Supports exporting results to CSV for audits and reproducibility  

---

## 📈 Results
Key analytical findings:  

- **Hypertension + Smoking:** Patients with both risk factors showed significantly higher stroke prevalence, consistent with medical literature.  
- **Sleep Patterns:** Stroke-positive patients displayed slightly reduced sleep hours on average, aligning with recent clinical studies on sleep irregularity and vascular health.  
- **Descriptive Insights:** Stratification by comorbidities and demographics revealed subgroup-specific trends valuable for targeted interventions.  

These results demonstrate the potential of modular, transparent analytics in identifying actionable patterns in health datasets.  

---

## ⚠️ Challenges & Limitations
- **Data Quality Issues:** Missing and inconsistent entries required extensive cleaning.  
- **Scope:** Current design limited to descriptive and rule-based queries (no ML yet).  
- **Interface:** CLI-only, may not appeal to all users compared to GUI dashboards.  

---

## 🔮 Future Work
- Integration of **machine learning models** (logistic regression, random forest) for predictive risk scoring.  
- **Longitudinal analysis** to track patients over time.  
- Development of a **GUI-based interface** for broader adoption in clinical settings.  

---

## 📚 References
- Feigin et al. (2025). *World Stroke Organization Global Stroke Fact Sheet 2025.*  
- Zhou et al. (2025). *The Stroke Burden in China and Its Long-Term Trends.*  
- Saeed et al. (2025). *Machine learning-based stroke prediction.*  
- Jung et al. (2025). *User-Centered Explanation Interfaces for AI in Healthcare.*  
- NIH StrokeNet (2025). *Sleep Duration and Stroke Risk.*  

---
