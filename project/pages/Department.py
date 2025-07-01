import streamlit as st
from scholarly import scholarly
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Department Research Publications", layout="wide")

# Load faculty data
df = pd.read_excel("faculty_metrics.xlsx")

# Get unique departments
departments = df['Department'].unique()

# Page Title
st.title("📚 Department-wise Latest Publications - Vidyalankar Institute of Technology")

# Sidebar for department selection
selected_dept = st.sidebar.selectbox("Select Department", departments)

# Filter faculties for selected department
dept_faculties = df[df['Department'] == selected_dept]

st.header(f"Department: {selected_dept}")
st.write(f"Total Faculty: {len(dept_faculties)}")

# Iterate through faculties in the department
for _, row in dept_faculties.iterrows():
    name = row['Name']
    scholar_id = row['Scholar ID']

    if scholar_id == "Not Found":
        st.warning(f"🔍 {name} — Google Scholar ID not available.")
        continue

    try:
        author = scholarly.search_author_id(scholar_id)
        detailed_author = scholarly.fill(author)

        st.subheader(f"👤 {name}")
        st.write(f"**Total Citations:** {detailed_author.get('citedby', 'N/A')}")
        st.write(f"**h-index:** {detailed_author.get('hindex', 'N/A')}")
        st.write(f"**i10-index:** {detailed_author.get('i10index', 'N/A')}")

        # Fetch latest 5 publications
        pubs = detailed_author.get('publications', [])[:5]
        papers = []
        for pub in pubs:
            pub_filled = scholarly.fill(pub)
            title = pub['bib']['title']
            year = pub['bib'].get('pub_year', 'N/A')
            venue = pub['bib'].get('venue', 'Unknown')
            url = pub_filled.get('pub_url', None)

            title_md = f"[{title}]({url})" if url else title
            papers.append({'Title': title_md, 'Year': year, 'Journal': venue})

        # Convert to dataframe
        pubs_df = pd.DataFrame(papers)

        if not pubs_df.empty:
            st.markdown(f"**📄 Latest Publications:**")
            for _, paper in pubs_df.iterrows():
                st.markdown(f"- {paper['Title']} ({paper['Year']}, *{paper['Journal']}*)")

            st.markdown("---")

        else:
            st.info("No publications found.")

    except Exception as e:
        st.error(f"Error retrieving data for {name}: {e}")

st.markdown("---")
st.markdown("Developed by Vidyalankar Institute of Technology")
