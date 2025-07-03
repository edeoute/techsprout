import streamlit as st
import requests
import os
from scholarly import scholarly
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Faculty Research Profile", layout="wide")

# Navbar
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

# Faculty metrics table
metrics_df = pd.read_excel("project/faculty_metrics.xlsx")
st.title("🎓 Faculty Research Profiles")

# Load faculty data
metrics_df = pd.read_excel("project/faculty_metrics.xlsx")

# Preprocess for case-insensitive search
metrics_df["Name_Lower"] = metrics_df["Name"].str.lower()

# Input box for name search
name_query = st.text_input("Enter Faculty Name").strip().lower()

# Filter names that match the query
matched_faculty = metrics_df[metrics_df["Name_Lower"].str.contains(name_query, na=False)] if name_query else pd.DataFrame()

# Let user pick from matched names (if multiple)
faculty_id = ""
department = ""

if not matched_faculty.empty:
    # Display name and department for clarity
    matched_faculty = matched_faculty.copy()  # Ensure it's a real copy
    matched_faculty["Display"] = matched_faculty["Name"] + " (" + matched_faculty["Department"] + ")"
    selected_display = st.selectbox("Select Matching Faculty", matched_faculty["Display"])

    # Get selected row
    selected_row = matched_faculty[matched_faculty["Display"] == selected_display].iloc[0]
    faculty_id = selected_row["Scholar ID"]
    department = selected_row["Department"]
    faculty_name = selected_row["Name"]

    if faculty_id == "Not Found":
        st.warning("⚠️ Google Scholar ID not available for this faculty member.")
        st.stop()

    st.markdown(f"### 👤 {faculty_name}")
    st.markdown(f"🏢 **Department:** {department}")


# Cloudinary Base URL
cloudinary_base_url = "https://res.cloudinary.com/dwuhswk2w/image/upload/v1751302313/"

# Function to generate image URL

def get_profile_image_url(faculty_id):
    remote_url = f"{cloudinary_base_url}{faculty_id}.jpg"
    try:
        response = requests.head(remote_url)
        if response.status_code == 200:
            return remote_url
        else:
            raise Exception("Image not found on Cloudinary")
    except:
        # Fall back to local default image
        return os.path.join("..", "profile_photos", "default.jpg")


# Show metrics table if no ID
if not faculty_id:
    st.subheader("📊 Faculty Research Metrics Summary")
    st.dataframe(metrics_df, use_container_width=True)

# Fetch profile on input
if faculty_id:
    try:
        author = scholarly.search_author_id(faculty_id)
        detailed_author = scholarly.fill(author)

        col1, col2 = st.columns([1, 3])

        with col1:
            image_url = get_profile_image_url(faculty_id)
            st.image(image_url, width=200, caption=author['name'])

        with col2:
            st.subheader(f"👤 {author['name']}")
            st.write(f"**Affiliation:** {author.get('affiliation', 'N/A')}")
            st.write(f"**Interests:** {', '.join(author.get('interests', []))}")

            st.markdown("<hr style='border: 1px solid #bbb;'>", unsafe_allow_html=True)
            st.metric("📈 Total Citations", detailed_author.get('citedby', 'N/A'))
            st.metric("📊 h-index", detailed_author.get('hindex', 'N/A'))
            st.metric("🔢 i10-index", detailed_author.get('i10index', 'N/A'))

        # Publications Table
        st.markdown("### 📄 Publications")
        st.markdown("*loading publications might take some time please be patient*")

        pubs = detailed_author.get('publications', [])
        papers = []

        for pub in pubs:
            title = pub['bib']['title']
            year = pub['bib'].get('pub_year', 'N/A')
            venue = pub['bib'].get('venue', 'Unknown Journal')
            pub_filled = scholarly.fill(pub)
            url = pub_filled.get('pub_url', None)
            title_md = f"[{title}]({url})" if url else title
            papers.append({'Title': title_md, 'Year': year, 'Journal': venue})

        df = pd.DataFrame(papers)

        table_html = """
        <style>
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; text-align: left; color: black; }
        </style>
        <table><tr><th>Title</th><th>Year</th><th>Journal</th></tr>
        """

        for _, row in df.iterrows():
            title_text = row['Title']
            if title_text.startswith("[") and "](" in title_text:
                title, link = title_text[1:].split("](")
                link = link.rstrip(")")
                title_html = f'<a href="{link}" target="_blank">{title}</a>'
            else:
                title_html = title_text
            table_html += f"<tr><td>{title_html}</td><td>{row['Year']}</td><td>{row['Journal']}</td></tr>"

        table_html += "</table>"
        st.markdown(table_html, unsafe_allow_html=True)

        # Publications per year graph
        pub_count = df[df['Year'] != 'N/A'].groupby('Year').size().reset_index(name='Publications')
        if not pub_count.empty:
            fig = px.bar(pub_count, x='Year', y='Publications',
                         title='📊 Publications Per Year',
                         labels={'Publications': 'Number of Papers'})
            st.plotly_chart(fig, use_container_width=True)

    except StopIteration:
        st.error("❌ Author not found. Please check the Google Scholar ID.")

# Footer
st.markdown("---")
st.markdown("Developed by Vidyalankar Institute of Technology")
