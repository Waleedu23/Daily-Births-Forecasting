📊 Daily Births Forecasting Using Machine Learning

A web-based Daily Births Forecasting System built using Python, Streamlit, Pandas, Plotly, and Prophet.

The application analyzes historical daily female birth data and forecasts future births using time-series forecasting.

🚀 Features

- 📁 View historical birth data
- 📊 Analyze daily and monthly birth trends
- 🔮 Forecast future births from 7 to 365 days
- 📈 Interactive Plotly charts
- 📋 View prediction intervals
- ⬇️ Download dataset and forecast results
- 🔐 User and administrator login
- ☁️ Streamlit Cloud deployment

🛠️ Technologies Used

Technology| Purpose
Python| Programming
Streamlit| Web application
Pandas| Data processing
NumPy| Numerical operations
Plotly| Interactive visualization
Prophet| Time-series forecasting

📂 Project Structure

Daily-Births-Forecasting/
│
├── app.py
├── daily-total-female-births.csv
├── requirements.txt
├── README.md
├── DATASET_SOURCE.txt
├── .gitignore
│
└── .streamlit/
    ├── config.toml
    └── secrets.toml.example

📊 Dataset

The project uses the Daily Total Female Births dataset containing daily female birth records from California for 1959.

The dataset contains:

- 365 daily observations
- "Date" – Date of observation
- "Births" – Number of births

For Prophet, the data is converted to:

ds → Date
y  → Births

🤖 Forecasting Model

The application uses Prophet for time-series forecasting.

Model Configuration

- Weekly seasonality: Enabled
- Yearly seasonality: Enabled
- Daily seasonality: Disabled

The user can select a forecast period between 7 and 365 days.

The forecast provides:

- Predicted births
- Lower prediction limit
- Upper prediction limit

🔄 Project Workflow

Historical Data
       ↓
Data Processing
       ↓
Data Analysis
       ↓
Prophet Model
       ↓
Future Forecast
       ↓
Interactive Dashboard

🔐 Authentication

The application provides two access levels:

Role| Access
User| Dataset, analysis and forecasting
Administrator| User features + administrative controls

Passwords should be stored using Streamlit Secrets and should not be uploaded to GitHub.

⚙️ Installation

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/Daily-Births-Forecasting.git

2. Open the project

cd Daily-Births-Forecasting

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run app.py

☁️ Deployment

The application can be deployed using Streamlit Community Cloud.

Select:

Repository: Daily-Births-Forecasting
Branch: main
Main file: app.py

Add your passwords through the Streamlit Secrets settings.

Do not upload:

.streamlit/secrets.toml

📥 Forecast Download

Forecast results can be downloaded as:

birth_forecast.csv

The forecast contains:

Field| Description
Date| Future prediction date
Predicted Births| Forecasted birth count
Lower Limit| Lower prediction boundary
Upper Limit| Upper prediction boundary

🎯 Project Objective

The objective of this project is to demonstrate the practical use of machine learning, time-series forecasting, data analysis, and interactive web applications using Python.

👨‍💻 Author

Mohammed Waleed V

M.Sc. Data Science
VIT Vellore

📄 License

No license has been specified for this project.

---

⭐ If you find this project useful for learning or academic purposes, you can star the repository.
