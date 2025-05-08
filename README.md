# HR Attrition Analysis

This project is focused on analyzing employee attrition within an organization using a combination of data science, business intelligence, and visualization tools. The objective is to understand the key reasons for employee turnover and provide actionable insights to HR stakeholders.

---

## Project Structure

```
HR_ATTRITION_ANALYSIS/
├── data/                  # Raw and processed data files
├── notebooks/             # Jupyter notebooks for EDA and modeling
├── powerbi_dashboard/     # Power BI dashboard files (.pbix)
├── reports/               # Reports and documentation
├── scripts/               # Python scripts for data processing
├── README.md              # Project README file
└── requirements.txt       # Project dependencies
```

---

## Objective

* Analyze HR data to detect patterns leading to employee attrition.
* Build predictive models to identify at-risk employees.
* Visualize findings through an interactive dashboard.

---

## Data Preprocessing

All preprocessing steps are handled in a dedicated script or Jupyter notebook. Cleaned data is stored in `data/processed_hr_data.csv`.

To preprocess the data, run:

```bash
cd scripts
python preprocess_data.py
```

---

## Exploratory Data Analysis (EDA)

Key highlights from the EDA:

* Attrition segmented by job role, gender, education level, and age group.
* Distance from home and business travel frequency analyzed.
* Gender-based attrition trends visualized.

The EDA notebook is located at: `notebooks/eda.ipynb`

---

## Model Building & SHAP Analysis

Implemented models:

* Logistic Regression
* Decision Tree

Performance is measured using metrics like accuracy, precision, recall.

SHAP values help explain feature importance.

Notebook path: `notebooks/modeling.ipynb`

---

## Power BI Dashboard

Features:

* Slicers for Gender and Department
* KPIs: Total Employees, Attrition Rate, Average Age
* Visuals: Donut charts, bar charts, waterfall chart

File: `powerbi_dashboard/hr_attrition.pbix`

---

## DAX Measures Used

```DAX
Attrition Rate = 
DIVIDE(
    CALCULATE(COUNTROWS(HR_data), HR_data[Attrition] = "Yes"),
    COUNTROWS(HR_data)
)

Age Group = 
SWITCH(TRUE(),
    HR_data[Age] <= 25, "18-25",
    HR_data[Age] <= 35, "26-35",
    HR_data[Age] <= 45, "36-45",
    HR_data[Age] <= 55, "46-55",
    "56 Plus"
)
```

---

## Requirements

Install required Python packages:

```bash
pip install -r requirements.txt
```

---

## Deliverables

* 📄 Word Report: `reports/hr_attrition_report.docx`
* 📊 Power BI Dashboard: `powerbi_dashboard/hr_attrition.pbix`
* 🧠 ML Models & SHAP: `notebooks/modeling.ipynb`
* 📈 EDA Summary: `notebooks/eda.ipynb`

---

## Future Enhancements

* Automate dashboard updates
* Integrate performance review data
* Deploy model via REST API

---

**Author:** *Shashank Mishra*

