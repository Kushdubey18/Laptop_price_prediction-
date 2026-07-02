# 💻 Laptop Price Prediction System

A Machine Learning-based web application that predicts the price of a laptop based on its specifications. This project uses data preprocessing, feature engineering, and regression models to provide accurate laptop price predictions through an easy-to-use Flask web interface.

---

## 📌 Features

- Predict laptop prices instantly
- User-friendly web interface built with Flask
- Data preprocessing and feature engineering
- Multiple Machine Learning models tested
- Best-performing model selected for deployment
- Responsive and modern UI

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- HTML
- CSS
- Bootstrap
- Joblib

---

## 📂 Project Structure

```
Laptop_Price_Prediction/
│
├── model/
│   ├── best_model.pkl
│   ├── encoder.pkl
│   └── scaler.pkl
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── result.html
│
├── dataset/
│   └── laptop_price.csv
│
├── app.py
├── requirements.txt
├── model_training.ipynb
└── README.md
```

---

## 📊 Dataset

The dataset contains laptop specifications such as:

- Company
- TypeName
- RAM
- Weight
- Operating System
- CPU
- GPU
- Screen Size
- Resolution
- IPS Display
- Touchscreen
- Memory
- SSD
- HDD
- Price

---

## ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Handling Missing Values
4. Feature Engineering
5. Encoding Categorical Features
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Saving
10. Flask Deployment

---

## 🤖 Models Used

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost (Optional)

The best-performing model was selected based on evaluation metrics.

---

## 📈 Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Laptop_Price_Prediction.git
```

### Move into Project Directory

```bash
cd Laptop_Price_Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask App

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 💡 How It Works

1. Enter laptop specifications.
2. Click the **Predict** button.
3. The trained machine learning model processes the inputs.
4. Predicted laptop price is displayed instantly.

---

## 📷 Screenshots

### Home Page

<img src="static/images/home.png" width="800">

### Prediction Result

<img src="static/images/result.png" width="800">

---

## 🔮 Future Improvements

- Deploy on Render or Railway
- Add user authentication
- Price trend visualization
- Compare multiple laptops
- API integration
- Dark mode UI
- Mobile-friendly interface

---

## 👨‍💻 Author

**Kush Kumar Dubey**

📧 Email: kushd142@gmail.com

📍 Jaipur, Rajasthan, India

🔗 LinkedIn:
https://www.linkedin.com/in/kush-dubey-96796a275/

💻 GitHub:
https://github.com/Kushdubey18

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal purposes.
