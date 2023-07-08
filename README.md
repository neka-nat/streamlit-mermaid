# streamlit-mermaid

Streamlit Component, for Mermaid.

## Installation

```bash
pip install streamlit-mermaid
```

## Quick start

```py
import streamlit_mermaid as stmd
import streamlit as st

code = """
graph TD
    A --> B
"""

mermaid = stmd.st_mermaid(code)
st.write(mermaid)
```

```bash
streamlit run example.py
```
