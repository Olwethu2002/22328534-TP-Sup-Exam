
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Women Safety Hotspot Analysis",
    page_icon="📍",
    layout="wide"
)

st.title("📍 Women Safety Hotspot Analysis")
st.write("Crime pattern analysis for Ekurhuleni and Kempton Park")

st.warning(
    "This dashboard displays recorded crime data. "
    "It does not confirm that every recorded crime involved a woman."
)

uploaded_file = st.file_uploader(
    "Upload your crime dataset (CSV)",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Dataset Information")
    col1, col2 = st.columns(2)
    col1.metric("Total records", len(df))
    col2.metric("Total columns", len(df.columns))

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        category = st.selectbox("Select a crime category", numeric_cols)

        st.subheader("Recorded Crime Counts")
        st.bar_chart(df[category].fillna(0))

        year_cols = [c for c in df.columns if "year" in c.lower()]

        if year_cols:
            year_col = st.selectbox("Select year column", year_cols)
            trend = df.groupby(year_col)[category].sum()
            st.subheader("Crime Trend Over Time")
            st.line_chart(trend)

else:
    st.info("Upload your SAPS crime dataset to view the dashboard.")
