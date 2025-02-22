# Example 3
import streamlit as st
import plotly.express as px
import pandas as pd

# Load Sample Data
df = px.data.gapminder()

# Streamlit App Title
st.title("📊 Interactive Dashboard with Multiple Plots")

# Create a sidebar filter for selecting a year
selected_year = st.sidebar.slider("Select Year:", int(df["year"].min()), int(df["year"].max()), int(df["year"].min()),step=5)

# Filter data based on the selected year
filtered_df = df[df.year == selected_year]

# Create three different plots
fig1 = px.scatter(filtered_df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                  hover_name="country", log_x=True, size_max=60, title="Life Expectancy vs GDP")

fig2 = px.bar(filtered_df, x="continent", y="pop", color="continent", title="Population per Continent")

fig3 = px.line(filtered_df, x="country", y="gdpPercap", color="continent", title="GDP Per Capita by Country")

# Arrange the plots in a grid layout
col1, col2 = st.columns(2)  # Create 2 columns

with col1:
    st.plotly_chart(fig1, use_container_width=True)  # First plot in first column

with col2:
    st.plotly_chart(fig2, use_container_width=True)  # Second plot in second column

# Add the third plot in a full-width row below
st.plotly_chart(fig3, use_container_width=True)
