"""Run this app with: streamlit run itables_app.py"""

import string

import numpy as np
import pandas as pd
import streamlit as st
from itables import to_html_datatable
from itables.sample_dfs import get_countries
from streamlit.components.v1 import html

df = get_countries(html=False)
# Add columns for the searchPanes demo
df["climate_zone"] = np.where(
    df["latitude"].abs() < 23.43615,
    "Tropical",
    np.where(
        df["latitude"].abs() < 35,
        "Sub-tropical",
        # Artic circle is 66.563861 but there is no capital there => using 64
        np.where(df["latitude"].abs() < 64, "Temperate", "Frigid"),
    ),
)
df["hemisphere"] = np.where(df["latitude"] > 0, "North", "South")
wide_df = pd.DataFrame(
    {
        letter: np.random.normal(size=100)
        for letter in string.ascii_lowercase + string.ascii_uppercase
    }
)

st.logo(
    "https://raw.githubusercontent.com/mwouts/itables/main/src/itables/logo/logo.svg",
    link="https://mwouts.github.io/itables/streamlit.html",
)
st.sidebar.markdown(
    """
# ITables in Streamlit
![Stars](https://img.shields.io/github/stars/mwouts/itables)

The recommended way to use ITables in a Streamlit application is by calling
```python
from itables.streamlit import interactive_table

interactive_table(df, ...)
```

Yet in case you have specific needs like using custom JavaScript callbacks, you can
also use `to_html_datatable` in combination with `html` like in this example.
    """
)

st.markdown(
    """
```python
from itables import to_html_datatable
from streamlit.components.v1 import html


html(
    to_html_datatable(
        df,
        layout={"top1": "searchPanes"},
        searchPanes={"layout": "columns-3", "cascadePanes": True},
    ),
    height=960,  # adjust manually
)
```
"""
)

html(
    to_html_datatable(
        df,
        layout={"top1": "searchPanes"},
        searchPanes={"layout": "columns-3", "cascadePanes": True},
    ),
    height=960,  # adjust manually
)
