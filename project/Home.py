import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(page_title="Research Portal", layout="wide")
navbar =  """
<style>
.navbar {
    background-color: #004080;
    overflow: hidden;
    padding: 0.75rem 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 0;
}
.navbar a {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    font-weight: 600;
}
.navbar a:hover {
    background-color: #0066cc;
    border-radius: 4px;
}
.navbar-logo {
    height: 40px;
}
.navbar-menu {
    display: flex;
    gap: 10px;
}
</style>

<div class="navbar">
    <div>
        <a href="/">
            <img src="https://cdn.prod.website-files.com/681bb5b264e600d25933af1b/685ea5fc390c7539720c32c2_VIT-copy-1-1.png" class="navbar-logo">
        </a>
    </div>
    <div class="navbar-menu">
        <a href="/">Home</a>
        <a href="/Faculty_Dashboard">Faculty Dashboard</a>
        <a href="#">Login</a>
    </div>
</div>
"""

st.markdown(navbar, unsafe_allow_html=True)


home_css = """
<style>
.container {
    display: grid;
    grid-template-columns: repeat(3, minmax(300px, 1fr));
    grid-gap: 20px;
    margin-top: 30px;
}
.card {
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px;
    background-color: #ffffff;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.card img {
    width: 80px;
    height: 80px;
    object-fit: cover;
    margin-bottom: 15px;
}
.card h3 {
    font-size: 20px;
    margin-bottom: 10px;
}
.card p {
    font-size: 14px;
    color: #555;
    margin-bottom: 20px;
}
.card a {
    text-decoration: none;
    color: #ffffff;
    background-color: #424593;
    padding: 10px 20px;
    border-radius: 5px;
    display: inline-block;
}
.card a:hover {
    background-color: #33356e;
}
</style>
"""

# Apply CSS
st.markdown(home_css, unsafe_allow_html=True)

# Page Title
st.title("🎓 Welcome to your Faculty Research Portal")

components.html(f"""
{home_css}
<div class="container">

    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" alt="Faculty">
        <h3>Faculty Profiles</h3>
        <p>Browse research profiles, citations and scholarly work.</p>
        <a href="/Faculty_Profiles">View Profiles</a>
    </div>

    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2920/2920209.png" alt="Resources">
        <h3>Scholarly Resources</h3>
        <p>Access research papers, patents and publications.</p>
        <a href="#">Explore Resources</a>
    </div>

    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png" alt="Impact">
        <h3>Impact Metrics</h3>
        <p>See the citation count, h-index and i10-index impact.</p>
        <a href="#">View Impact</a>
    </div>

    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3652/3652287.png" alt="Deparment">
        <h3>Department</h3>
        <p>Browse department-wise publications</p>
        <a href="#">View publications</a>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/5976/5976300.png" alt="Deparment">
        <h3>Top-publications</h3>
        <p>Browse research papers</p>
        <a href="#">View </a>
    </div>
    
</div>
""", height=900)

df = pd.read_excel("project/department_metrics.xlsx")

# Page Title


# Bar traces
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df['Department'],
    y=df['Publications'],
    name='Publications',
    marker_color='rgba(0, 123, 255, 0.8)'
))

fig.add_trace(go.Bar(
    x=df['Department'],
    y=df['Citations'],
    name='Citations',
    marker_color='rgba(156, 39, 176, 0.8)'
))

fig.add_trace(go.Bar(
    x=df['Department'],
    y=df['Crossref_Citations'],
    name='CROSSREF Citations',
    marker_color='rgba(76, 175, 80, 0.8)',
    
))

# Add h-index as a line trace with secondary y-axis
fig.add_trace(go.Scatter(
    x=df['Department'],
    y=df['h_index'],
    name='h-index',
    mode='lines+markers+text',
    text=df['h_index'],
    textposition='top center',
    marker=dict(color='orange'),
    yaxis='y2'
))

# Layout config
fig.update_layout(
    title='Research Metrics by Department',
    xaxis_title='Department',
    yaxis=dict(title='Counts (Publications, Citations, Crossref)'),
    yaxis2=dict(title='h-index', overlaying='y', side='right'),
    barmode='group',
    height=600,
    legend=dict(x=0.85, y=1),
    xaxis_tickangle=-35
)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("Developed by Vidyalankar institute of technology")
