
# 🐟 Clarias Fish Growth Prediction App

## Overview

This project provides an interactive Streamlit web app and a Jupyter notebook for predicting the **final mean weight** of *Clarias gariepinus* (African catfish) juveniles and fingerlings. The prediction is based on feed composition and growth parameters, leveraging a machine learning model trained on real experimental data.

---

## Features

- **User-friendly Streamlit app** for quick predictions
- Predicts final mean weight based on 10 key growth and feed parameters
- Interactive sliders, radio buttons, and real-time feedback
- Model trained using a robust scikit-learn pipeline
- Transparent code and reproducible workflow

---

## Dataset Source

The dataset used in this project was obtained from the **Unilorin Zoology Department Library** and is based on two undergraduate projects:

- **Adenusi Morenike Hannah (18/55EK036):**  
  *Growth performances of Clarias gariepinus juveniles fed with varying levels of Citrus sinesis peel and pulp single cell protein.*
- **Yusuf Habibat (17/55EK225):**  
  *Growth performance of Clarias fingerlings fed on single cell protein from Dioscorea rotundata peel.*

---

## Files

- `streamlit_app.py`  
  The Streamlit web application for interactive predictions.

- `Predicting_Final_Mean_Weight_of_Clarias_Fish_Based_on_Feed_Composition_and_Growth_Parameters.ipynb`  
  The Jupyter notebook containing data analysis, model training, and evaluation.

- `model.joblib`  
  The trained machine learning model pipeline (must be in the same directory as the app).

- `Clarias growth perfomance.xlsx`  
  The original dataset ( see above for source).

---

## How to Run the App

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/clarias-gariepinus-growth-prediction-app.git
   cd clarias-gariepinus-growth-prediction-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure `model.joblib` is present in the project directory.**

4. **Start the app:**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Interact with the app in your browser!**
https://clarias-gariepinus-growth-prediction-app-elogqw8ngb8upfpcj5gtq.streamlit.app/
---

## Model Details

- **Algorithm:** Linear Regression (scikit-learn)
- **Pipeline:** Includes numeric imputation, scaling, and one-hot encoding for categorical features
- **Features:**  
  - Initial Mean Weight (g)
  - Mean Weight Gained (g)
  - Specific Growth Rate (SGR)
  - Feed Conversion Rate (FCR)
  - Percentage Mortality (%PM)
  - Percentage Survival (%PS)
  - Single Cell Protein (Yes/No)
  - Single Cell Protein Type (SPT)
  - SPT Percentage
  - Commercial Feed Percentage

---

## Citation & Acknowledgments

- **Dataset:**  
  Unilorin Zoology Department Library  
  Projects by Adenusi Morenike Hannah (18/55EK036) and Yusuf Habibat (17/55EK225)

- **Developed by:**  
  Yusuf Abdulsobur Olayiwola, 2025

---

## License

This project is for educational and research purposes. Please cite the original student projects and the Unilorin Zoology Department if you use this work.

---

## Screenshots

!
![Screenshot 2025-05-16 200120](https://github.com/user-attachments/assets/90da6dd5-6e1d-44b1-9ca3-c1402e8f081a)


For questions or collaboration, please open an issue or contact [princeolayiwola8@gmail.com].

---

**Enjoy exploring Clarias fish growth predictions! 🐟**

---

> **Note:**  
>  Please contact the Unilorin Zoology Department Library or the original project authors for access.

