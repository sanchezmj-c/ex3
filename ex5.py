# Load Sample Data
df = sns.load_dataset('mpg')
corr = df.corr(numeric_only=True)
corr_text = np.round(corr, 2).astype(str)  # Redondear y convertir a texto

# Streamlit App Title
st.title("📊 Interactive Dashboard with Multiple Plots")

# Create a sidebar filter for selecting a year
#selected_year = st.sidebar.slider("Select Year:", int(df["model_year"].min()), int(df["model_year"].max()), int(df["model_year"].min()))

# Filter data based on the selected year
#filtered_df = df[df.model_year == selected_year]

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

fig2 = px.strip(
    df,  # DataFrame
    x='cylinders',  # Eje X: número de cilindros
    y='horsepower',  # Eje Y: caballos de fuerza
    color='cylinders',  # Colorear por número de cilindros
    color_discrete_sequence=px.colors.qualitative.Plotly,  # Usar la paleta Plotly
    title='Distribución de Potencia según Número de Cilindros',  # Título
    labels={'cylinders': 'Número de Cilindros', 'horsepower': 'Caballos de Fuerza (hp)'}  # Etiquetas
)

# Personalizar el diseño del gráfico
fig2.update_layout(
    width=800,  # Ancho del gráfico
    height=500,  # Alto del gráfico
    xaxis_title='Número de Cilindros',  # Título del eje X
    yaxis_title='Caballos de Fuerza (hp)',  # Título del eje Y
    showlegend=False  # Ocultar la leyenda
)

fig3 = px.scatter(filtered_df, x="weight", y="mpg", color_discrete_sequence=px.colors.qualitative.Set1,
                  size="horsepower", title="Relación entre Peso y MPG (Color por Origen)")


## Arrange the plots in a grid layout
col1, col2 = st.columns(2)  # Create 2 columns

with col1:
    st.plotly_chart(fig1, use_container_width=True)  # First plot in first column

with col2:
    st.plotly_chart(fig2, use_container_width=True)  # Second plot in second column

# Add the third plot in a full-width row below
st.plotly_chart(fig3, use_container_width=True)
