import streamlit as st


def get_item(config, densities):
    _densities = list(densities)
    index = _densities.index(config["item"])
    return st.selectbox("x", _densities, index=index)


def get_unit(config, volumes, masses):
    units = list(volumes | masses)
    index = units.index(config["unit"])
    return st.selectbox("type", units, index=index)


def get_quantity(config):
    return st.number_input("quantity", min_value=0.0, value=config["quantity"])
