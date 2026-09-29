import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Daily Births Forecasting",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #F4F8FB;
    color: #000000;
}

[data-testid="stSidebar"] {
    background-color: #123B5D;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #000000 !important;
}

p, label, span, div {
    color: #000000;
}

.stButton > button {
    background-color: #159A9C;
    color: white !important;
    border-radius: 8px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #117C7E;
    color: white !important;
}

.stDownloadButton > button {
    background-color: #123B5D;
    color: white !important;
    border-radius: 8px;
    border: none;
    font-weight: bold;
}

.stDownloadButton > button:hover {
    background-color: #0D2D46;
    color: white !important;
}

.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #159A9C;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    text-align: center;
}

.metric-title {
    color: #000000 !important;
    font-size: 15px;
    font-weight: bold;
}

.metric-value {
    color: #000000 !important;
    font-size: 28px;
    font-weight: bold;
}

.login-box {
    background-color: white;
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
}

.info-box {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #159A9C;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOGIN SYSTEM
# --------------------------------------------------

USERS = {
    "admin": {
        "password": "admin123",
        "role": "Administrator"
    },
    "user": {
        "password": "user123",
        "role": "User"
    }
}


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


def login():

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col2:

        st.markdown(
            """
            <div class="login-box">
            <h1 style="text-align:center;color:#123B5D;">
            📊 Daily Births Forecasting
            </h1>

            <p style="text-align:center;color:black;">
            Secure Forecasting Dashboard
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        username = st.text_input(
            "Username",
            placeholder="Enter username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        if st.button("Login", use_container_width=True):

            if username in USERS and USERS[username]["password"] == password:

                st.session_state.logged_in = True
                st.session_state.username = username

                st.rerun()

            else:
                st.error("Invalid username or password")


if not st.session_state.logged_in:

    login()
    st.stop()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("📊 Birth Forecast")

st.sidebar.markdown("---")

st.sidebar.write(
    f"👤 User: {st.session_state.username}"
)

st.sidebar.write(
    f"🔐 Role: {USERS[st.session_state.username]['role']}"
)

st.sidebar.markdown("---")

if st.sidebar.button("Logout", use_container_width=True):

    st.session_state.logged_in = False
    st.session_state.username = ""

    st.rerun()


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

try:

    df = pd.read_csv("daily-total-female-births.csv")

except FileNotFoundError:

    st.error(
        "Dataset not found. Please place "
        "'daily-total-female-births.csv' in the same folder as app.py."
    )

    st.stop()


# --------------------------------------------------
# PREPARE DATA
# --------------------------------------------------

if len(df.columns) >= 2:

    df = df.iloc[:, :2]

    df.columns = ["ds", "y"]


df["ds"] = pd.to_datetime(
    df["ds"],
    errors="coerce"
)

df["y"] = pd.to_numeric(
    df["y"],
    errors="coerce"
)

df = df.dropna()

df = df.sort_values("ds")


# --------------------------------------------------
# MAIN TITLE
# --------------------------------------------------

st.title("📊 Daily Births Forecasting Dashboard")

st.markdown(
    """
    **Machine Learning based forecasting of daily female births**

    This dashboard analyzes historical daily birth data and predicts
    future birth values using the Prophet forecasting model.
    """
)


# --------------------------------------------------
# METRICS
# --------------------------------------------------

total_records = len(df)

average_births = df["y"].mean()

maximum_births = df["y"].max()

minimum_births = df["y"].min()


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        f"""
        <div class="metric-card">
        <div class="metric-title">Total Records</div>
        <div class="metric-value">{total_records}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="metric-card">
        <div class="metric-title">Average Births</div>
        <div class="metric-value">{average_births:.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="metric-card">
        <div class="metric-title">Maximum Births</div>
        <div class="metric-value">{maximum_births}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="metric-card">
        <div class="metric-title">Minimum Births</div>
        <div class="metric-value">{minimum_births}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("<br>", unsafe_allow_html=True)


# --------------------------------------------------
# BLACK CHART THEME
# --------------------------------------------------

def black_chart_theme(fig):

    fig.update_layout(

        paper_bgcolor="white",

        plot_bgcolor="white",

        font=dict(
            color="black",
            family="Arial"
        ),

        title=dict(
            font=dict(
                color="black",
                size=22
            )
        ),

        xaxis=dict(

            title_font=dict(
                color="black",
                size=15
            ),

            tickfont=dict(
                color="black",
                size=12
            ),

            showline=True,

            linecolor="black",

            mirror=True

        ),

        yaxis=dict(

            title_font=dict(
                color="black",
                size=15
            ),

            tickfont=dict(
                color="black",
                size=12
            ),

            showline=True,

            linecolor="black",

            mirror=True

        ),

        legend=dict(

            font=dict(
                color="black",
                size=13
            )

        ),

        hoverlabel=dict(

            bgcolor="white",

            font=dict(
                color="black",
                size=13
            )

        )

    )

    return fig


# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📁 Dataset",
        "📈 Analysis",
        "🔮 Forecast",
        "⚙️ Model"
    ]
)


# ==================================================
# DATASET TAB
# ==================================================

with tab1:

    st.header("📁 Dataset")

    st.write(
        "Historical daily female birth records used for forecasting."
    )

    display_df = df.copy()

    display_df["ds"] = display_df["ds"].dt.strftime("%Y-%m-%d")

    display_df.columns = [
        "Date",
        "Births"
    ]

    st.dataframe(
        display_df,
        use_container_width=True,
        height=450
    )


    csv_data = display_df.to_csv(
        index=False
    ).encode("utf-8")


    st.download_button(

        label="⬇️ Download Dataset",

        data=csv_data,

        file_name="daily_births_dataset.csv",

        mime="text/csv"

    )


# ==================================================
# ANALYSIS TAB
# ==================================================

with tab2:

    st.header("📈 Historical Data Analysis")


    # ----------------------------------------------
    # DAILY BIRTHS
    # ----------------------------------------------

    fig_daily = px.line(

        df,

        x="ds",

        y="y",

        title="Daily Female Births",

        labels={
            "ds": "Date",
            "y": "Number of Births"
        }

    )


    fig_daily.update_traces(
        line=dict(width=2)
    )


    fig_daily = black_chart_theme(
        fig_daily
    )


    st.plotly_chart(
        fig_daily,
        use_container_width=True
    )


    # ----------------------------------------------
    # MONTHLY AVERAGE
    # ----------------------------------------------

    monthly = (

        df.set_index("ds")

        .resample("ME")["y"]

        .mean()

        .reset_index()

    )


    fig_monthly = px.bar(

        monthly,

        x="ds",

        y="y",

        title="Monthly Average Births",

        labels={
            "ds": "Month",
            "y": "Average Births"
        }

    )


    fig_monthly = black_chart_theme(
        fig_monthly
    )


    st.plotly_chart(

        fig_monthly,

        use_container_width=True

    )


# ==================================================
# FORECAST TAB
# ==================================================

with tab3:

    st.header("🔮 Birth Forecast")


    st.write(
        "Use the slider to select how many future days should be predicted."
    )


    periods = st.slider(

        "Forecast Period",

        min_value=7,

        max_value=365,

        value=30,

        step=1

    )


    if st.button(
        "🚀 Generate Forecast",
        use_container_width=True
    ):

        with st.spinner(
            "Training forecasting model..."
        ):

            model = Prophet(

                yearly_seasonality=True,

                weekly_seasonality=True,

                daily_seasonality=False

            )


            model.fit(df)


            future = model.make_future_dataframe(

                periods=periods,

                freq="D"

            )


            forecast = model.predict(
                future
            )


        st.success(
            "Forecast generated successfully!"
        )


        # ------------------------------------------
        # FORECAST TABLE
        # ------------------------------------------

        future_forecast = forecast[
            forecast["ds"] > df["ds"].max()
        ].copy()


        forecast_table = pd.DataFrame({

            "Date": future_forecast["ds"],

            "Predicted Births":
                future_forecast["yhat"],

            "Lower Limit":
                future_forecast["yhat_lower"],

            "Upper Limit":
                future_forecast["yhat_upper"]

        })


        forecast_table["Date"] = (
            forecast_table["Date"]
            .dt.strftime("%Y-%m-%d")
        )


        forecast_table[
            [
                "Predicted Births",
                "Lower Limit",
                "Upper Limit"
            ]
        ] = forecast_table[
            [
                "Predicted Births",
                "Lower Limit",
                "Upper Limit"
            ]
        ].round(0).astype(int)


        st.subheader(
            "Future Birth Predictions"
        )


        st.dataframe(

            forecast_table,

            use_container_width=True,

            height=400

        )


        # ------------------------------------------
        # FORECAST CHART
        # ------------------------------------------

        chart_df = forecast[
            [
                "ds",
                "yhat",
                "yhat_lower",
                "yhat_upper"
            ]
        ].copy()


        fig_forecast = px.line(

            chart_df,

            x="ds",

            y=[
                "yhat",
                "yhat_lower",
                "yhat_upper"
            ],

            title="Birth Forecast",

            labels={
                "ds": "Date",
                "value": "Births",
                "variable": "Forecast"
            }

        )


        fig_forecast = black_chart_theme(
            fig_forecast
        )


        st.plotly_chart(

            fig_forecast,

            use_container_width=True

        )


        # ------------------------------------------
        # DOWNLOAD FORECAST
        # ------------------------------------------

        forecast_csv = forecast_table.to_csv(
            index=False
        ).encode("utf-8")


        st.download_button(

            label="⬇️ Download Forecast",

            data=forecast_csv,

            file_name="birth_forecast.csv",

            mime="text/csv"

        )


# ==================================================
# MODEL TAB
# ==================================================

with tab4:

    st.header("⚙️ Machine Learning Model")


    st.markdown(
        """
        <div class="info-box">

        <h3>Prophet Forecasting Model</h3>

        <p>
        This application uses the Facebook Prophet forecasting model
        to predict future daily birth values.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.subheader("Model Configuration")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            """
            **Yearly Seasonality**

            Enabled
            """
        )


    with col2:

        st.markdown(
            """
            **Weekly Seasonality**

            Enabled
            """
        )


    with col3:

        st.markdown(
            """
            **Daily Seasonality**

            Disabled
            """
        )


    st.markdown("---")


    st.subheader(
        "Dataset Information"
    )


    st.write(
        f"Number of records: **{len(df)}**"
    )

    st.write(
        f"Start date: **{df['ds'].min().strftime('%Y-%m-%d')}**"
    )

    st.write(
        f"End date: **{df['ds'].max().strftime('%Y-%m-%d')}**"
    )


    # ----------------------------------------------
    # ADMIN CONTROLS
    # ----------------------------------------------

    if USERS[st.session_state.username]["role"] == "Administrator":

        st.markdown("---")

        st.subheader(
            "🔐 Administrator Controls"
        )

        uploaded_file = st.file_uploader(

            "Upload New Dataset",

            type=["csv"]

        )


        if uploaded_file is not None:

            new_df = pd.read_csv(
                uploaded_file
            )

            st.success(
                "Dataset uploaded successfully."
            )

            st.dataframe(
                new_df,
                use_container_width=True
            )


    else:

        st.info(
            "Administrator access is required for dataset upload and model controls."
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:black;">

    <b>Daily Births Forecasting System</b><br>

    Machine Learning • Time Series Forecasting • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)