import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Impact Metrics",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("📊 Impact Metrics by Department")

df = pd.read_excel("project/department_metrics.xlsx")

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
    marker_color='rgba(76, 175, 80, 0.8)'
))

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

st.plotly_chart(fig, use_container_width=True)
