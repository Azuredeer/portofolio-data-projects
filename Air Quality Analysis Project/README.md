## How to Run the Dashboard

To run the Air Quality Analysis Dashboard, follow these steps:

### Setup Environment

1. **Create and Activate a Python Environment**:
   - If using Conda (ensure [Conda](https://docs.conda.io/en/latest/) is installed):
     ```
     conda create --name air_quality python=3.9
     conda activate air_quality
     ```
   - If using venv (standard Python environment tool):
     ```
     python -m venv air_quality
     source air_quality/bin/activate  # On Windows use `air_quality\Scripts\activate`
     ```

2. **Install Required Packages**:
   - The following packages are necessary for running the analysis and the dashboard:
     ```
     pip install pandas numpy matplotlib seaborn streamlit
     ```

     or you can do
     ```
     pip install -r requirements.txt
     ```
### Run the Streamlit App

1. **Navigate to the Project Directory** where `dashboard.py` is located.

2. **Run the Streamlit App**:
    ```
    streamlit run dashboard/dashboard.py
    ```

### Additional Files

- The dataset used for this analysis is included in the project repository.
- A detailed Python notebook (`analysis_air.ipynb`) containing the data analysis and visualizations is also provided.
---
### P.S.

Since Dicoding recommended creating the good and tidy folder structures, as `dashboard.py` in `dashboard` folder, then the deployment for Streamlit App affected.

That was why I put the `requirements.txt` in the `dashboard` folder as well.  

---

## About Me
- **Name**: Yoan Rifqi Candra
- **Email Address**: yoanrifqicandra@gmail.com
- **Dicoding ID**: [yoanrifqi](https://www.dicoding.com/users/yoanrifqi/)