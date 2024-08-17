# Using `to_html_datatable` in a Streamlit application

This repository contains a Streamlit app that display DataFrames using [ITables](https://mwouts.github.io/itables/streamlit.html)' `to_html_datatable` function.

Access the demo at https://to-html-datatable.streamlit.app.

You should use `to_html_datatable` only in specific cases. Please note that the recommended way to use ITables in a Streamlit application is:
```
from itables.streamlit import interactive_table
```
