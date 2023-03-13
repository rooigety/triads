# Copyright 2023 ROOIGETY, all rights reserved.
#
# Written by rooigety <flanker_sheen.Of@icloud.com> and originally
# created on 2023-03-13.

import os
import sys

import streamlit as st
from streamlit.web import cli


def get_apps():
    app_files = os.listdir("./src/triads/apps")

    results = dict()
    for file in app_files:
        if not file.endswith(".py"):
            continue
        elif file.startswith("_"):
            continue
        else:
            name = file.rstrip(".py").split("_")
            results[" ".join(name)] = file[:-3]

    return results


def main():
    st.set_page_config(page_title="Triads", page_icon="🃏")
    st.sidebar.title("Triads")
    st.sidebar.markdown("A collection of apps for triads.")

    apps = get_apps()
    app = st.sidebar.selectbox("Select an app", list(apps.keys()))

    if app:
        module = __import__(f"triads.apps.{apps[app]}", fromlist=["main"])
        module.main()


def run() -> None:
    """Run the Streamlit server."""
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", "src/triads/server.py"]
        sys.exit(cli.main())


if __name__ == "__main__":
    main()
