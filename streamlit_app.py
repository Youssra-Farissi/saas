import streamlit as st
st.set_page_config(
    page_title = "Hello",
    page_icon= ""
)

expander = st.expander("Domain knowledge of Oil & Gas")

expander.write("""
The oil and gas industry is a multifaceted sector encompassing exploration,
 extraction, refining, and distribution of hydrocarbon resources. 
 It plays a pivotal role in global energy supply, powering industries,
transportation, and households worldwide.
From drilling rigs in remote offshore locations to sprawling refineries and intricate pipelines,
the industry's operations are complex and technologically advanced. Geopolitical dynamics,
environmental concerns, and market fluctuations significantly impact its trajectory, 
driving innovation in sustainable practices and alternative energy sources.
Despite these challenges, the oil and gas sector remains integral to meeting the world's energy demands, 
 shaping economies, and driving global development.""")