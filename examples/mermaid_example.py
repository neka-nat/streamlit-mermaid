import streamlit as st
from streamlit_mermaid import st_mermaid

st.set_page_config(
    page_title="Streamlit Mermaid Example",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Streamlit Mermaid Example")

st.markdown(
    """
    ## Mermaid
    [Mermaid](https://mermaid-js.github.io/mermaid/#/) is a diagramming and charting tool that uses text-based descriptions to render diagrams.
    """
)

st.markdown(
    """
    ### Flowchart
    """
)

mermaid_code = """graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
"""

mermaid_code = st.text_area("Mermaid Code", mermaid_code)

st_mermaid(mermaid_code, height="500px")
