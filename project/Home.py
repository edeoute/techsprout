import streamlit as st
import streamlit.components.v1 as components

# ----------- CONFIG & PAGE SETTINGS -----------
st.set_page_config(
    page_title="Research Portal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------- NAVBAR -----------
navbar = """
<style>
.navbar {
    background-color: #004080;
    overflow: hidden;
    padding: 0.75rem 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
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

# ----------- TITLE -----------
st.title("🎓 Welcome to your Faculty Research Portal")

# ----------- CARD STYLE (Streamlit + CSS) -----------
box_style = """
<style>
.card-box {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
    text-align: center;
    height: 100%;
}
.card-box:hover {
    transform: translateY(-6px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
}
.card-box img {
    width: 80px;
    height: 80px;
    object-fit: contain;
    margin-bottom: 15px;
}
.card-box h3 {
    margin: 10px 0;
}
.card-box p {
    font-size: 14px;
    color: #444;
    margin-bottom: 0;
}
.card-box .stButton {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}
.card-box .stButton>button {
    background-color: #424593;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 6px;
    font-weight: bold;
    cursor: pointer;
}
.card-box .stButton>button:hover {
    background-color: #33356e;
}
</style>
"""
st.markdown(box_style, unsafe_allow_html=True)

# ----------- CARDS DATA -----------
cards = [
    {
        "title": "Faculty Profiles",
        "desc": "Browse research profiles, citations, and scholarly work.",
        "img": "https://cdn-icons-png.flaticon.com/512/3135/3135789.png",
        "button": "View Profiles",
        "page": "pages/Faculty_Profiles.py"
    },
    {
        "title": "Impact Metrics",
        "desc": "See the citation count, h-index, and i10-index impact.",
        "img": "https://cdn-icons-png.flaticon.com/512/1828/1828884.png",
        "button": "View Metrics",
        "page": "pages/Impact_Metrics.py"
    },
    {
        "title": "Department",
        "desc": "Browse department-wise publications.",
        "img": "https://cdn-icons-png.flaticon.com/512/3652/3652287.png",
        "button": "View Department",
        "page": "pages/Department.py"
    }
]

# ----------- RENDER CARDS IN ROWS OF 3 -----------
cols_per_row = 3
for i in range(0, len(cards), cols_per_row):
    row = st.columns(cols_per_row)
    for j, card in enumerate(cards[i:i+cols_per_row]):
        with row[j]:
            st.markdown(f"""
                <div class="card-box">
                    <img src="{card['img']}">
                    <h3>{card['title']}</h3>
                    <p>{card['desc']}</p>
            """, unsafe_allow_html=True)
            if st.button(card["button"], key=f"btn_{i}_{j}"):
                st.switch_page(card["page"])
            st.markdown("</div>", unsafe_allow_html=True)

# ----------- FOOTER -----------
st.markdown("---")
st.markdown("Developed by Vidyalankar Institute of Technology")
