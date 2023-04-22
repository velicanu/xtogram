import streamlit as st

from components import get_item, get_quantity, get_unit
from tables import DENSITIES, MASSES, VOLUMES
from utils import init, load_config, save_config


def get_grams(item, unit, quantity, masses, volumes, densities):
    if unit in masses:
        return quantity * masses[unit]
    return quantity * volumes[unit] * densities[item]


def main(config):
    init()
    col1, col2, col3 = st.columns(3)
    with col1:
        item = get_item(config, DENSITIES)
    with col2:
        unit = get_unit(config, VOLUMES, MASSES)
    with col3:
        quantity = get_quantity(config)

    grams = get_grams(item, unit, quantity, MASSES, VOLUMES, DENSITIES)

    st.title(f"{grams:.2f}")

    return {"item": item, "unit": unit, "quantity": quantity}


if __name__ == "__main__":
    config = load_config()
    new_config = main(config)
    save_config(new_config)
