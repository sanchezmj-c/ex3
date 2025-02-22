# Load Sample Data
df = sns.load_dataset('mpg')
corr = df.corr(numeric_only=True)
corr_text = np.round(corr, 2).astype(str)  # Redondear y convertir a texto

# Streamlit App Title
st.title("📊 Interactive Dashboard with Multiple Plots")

# Create a sidebar filter for selecting a year
selected_year = st.sidebar.slider("Select Year:", int(df["model_year"].min()), int(df["model_year"].max()), int(df["model_year"].min()))

# Filter data based on the selected year
filtered_df = df[df.model_year == selected_year]

# Create three different plots
# Crear el mapa de calor interactivo con Plotly
fig1 = px.imshow(
    corr,  # Matriz de correlación
    text_auto=False,  # Desactivar el formateo automático
    color_continuous_scale='RdBu',  # Escala de colores divergente
    labels=dict(x="Variable", y="Variable", color="Correlación"),  # Etiquetas
    x=corr.columns,  # Eje X: nombres de las columnas
    y=corr.columns,  # Eje Y: nombres de las columnas
    title="Mapa de Calor de Correlaciones (Dataset MPG)"
)

# Agregar los valores formateados como texto en las celdas
fig1.update_traces(
    text=corr_text.values,  # Usar los valores formateados
    texttemplate="%{text}",  # Mostrar el texto en las celdas
    hovertemplate="<b>Variable X:</b> %{x}<br><b>Variable Y:</b> %{y}<br><b>Correlación:</b> %{z:.2f}<extra></extra>"
)

fig2 = px.bar(filtered_df, x="origin", y="mpg", color="origin", title="Consumo Promedio de Combustible por Región de Origen")

fig3= px.scatter(filtered_df, x="horsepower", y="mpg", color="origin", title="Relación entre Caballos de Fuerza y Millas por Galón")

# Layout - Using Tabs to Display Multiple Plots
tab1, tab2, tab3 = st.tabs(["📌 HeatMap", "📊 Bar Chart", "📈 Line Chart"])

with tab1:
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.plotly_chart(fig3, use_container_width=True)
