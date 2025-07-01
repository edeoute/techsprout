import streamlit as st
from scholarly import scholarly
import pandas as pd
import plotly.express as px
from PIL import Image
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Faculty Research Profile", layout="wide")
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
st.title("🎓 Faculty Research Profile Dashboard")

home_css = """
<style>
.container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    grid-gap: 20px;
    margin-top: 30px;
    margin-bottom: 50px;
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


components.html(f"""
{home_css}
<div class="container">

    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" alt="Faculty">
        <h3>Director</h3>
        <p>Browse research profiles, citations and scholarly work.</p>
        <a href="#">View Profile</a>
    </div>
    
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" alt="Faculty">
        <h3>Dean</h3>
        <p>Browse research profiles, citations and scholarly work.</p>
        <a href="#">View Profile</a>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" alt="Faculty">
        <h3>Professor</h3>
        <p>Browse research profiles, citations and scholarly work.</p>
        <a href="#">View Profile</a>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" alt="Faculty">
        <h3>Assistant Professor</h3>
        <p>Browse research profiles, citations and scholarly work.</p>
        <a href="#">View Profile</a>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" alt="Faculty">
        <h3>Senior Professor</h3>
        <p>Browse research profiles, citations and scholarly work.</p>
        <a href="#">View Profile</a>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" alt="Faculty">
        <h3>Physical Director</h3>
        <p>Browse research profiles, citations and scholarly work.</p>
        <a href="#">View Profile</a>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" alt="Faculty">
        <h3>Faculty</h3>
        <p>Browse research profiles, citations and scholarly work.</p>
        <a href="#">View Profile</a>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" alt="Faculty">
        <h3>Scientist</h3>
        <p>Browse research profiles, citations and scholarly work.</p>
        <a href="#">View Profile</a>
    </div>
  
    
    
</div>
""", height=800)


