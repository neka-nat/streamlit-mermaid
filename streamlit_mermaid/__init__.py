import os
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
_RELEASE = True

if not _RELEASE:
    _streamlit_mermaid = components.declare_component(
        "streamlit_mermaid",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _streamlit_mermaid = components.declare_component("streamlit_mermaid", path=build_dir)


def st_mermaid(code: str, width: str="auto", height: str="auto", pan: bool=True, zoom: bool=True, show_controls: bool=True, key: Optional[str]=None):
    return _streamlit_mermaid(code=code, width=width, height=height, pan=pan, zoom=zoom, show_controls=show_controls, key=key)


# Test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run st_mermaid/__init__.py`
if not _RELEASE:
    code = """
    graph TD
        A --> B
        B --> C
        C --> D
        D --> E
        D --> F
    """

    st_mermaid(code, height="auto", pan=True, zoom=True, show_controls=True)
