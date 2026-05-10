import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# Header
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")

st.markdown("## Developed By")
st.markdown("### TAYYAB MUSTAFA")
st.markdown("### Roll Number: 25-ME-84")

st.write("---")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Select Option",
    ["Unit Converter", "Material Density Checker"]
)

# =========================
# UNIT CONVERTER
# =========================

if menu == "Unit Converter":

    st.header("📏 Unit Converter")

    conversion_type = st.selectbox(
        "Choose Conversion Type",
        ["Length", "Weight", "Temperature"]
    )

    # LENGTH
    if conversion_type == "Length":

        value = st.number_input("Enter Value", min_value=0.0)

        from_unit = st.selectbox(
            "From",
            ["Meter", "Kilometer", "Centimeter"]
        )

        to_unit = st.selectbox(
            "To",
            ["Meter", "Kilometer", "Centimeter"]
        )

        # Convert to meters first
        meter = value

        if from_unit == "Kilometer":
            meter = value * 1000

        elif from_unit == "Centimeter":
            meter = value / 100

        # Convert from meters
        result = meter

        if to_unit == "Kilometer":
            result = meter / 1000

        elif to_unit == "Centimeter":
            result = meter * 100

        st.success(f"Converted Value: {result}")

    # WEIGHT
    elif conversion_type == "Weight":

        value = st.number_input("Enter Weight", min_value=0.0)

        from_unit = st.selectbox(
            "From",
            ["Kilogram", "Gram"]
        )

        to_unit = st.selectbox(
            "To",
            ["Kilogram", "Gram"]
        )

        kg = value

        if from_unit == "Gram":
            kg = value / 1000

        result = kg

        if to_unit == "Gram":
            result = kg * 1000

        st.success(f"Converted Weight: {result}")

    # TEMPERATURE
    elif conversion_type == "Temperature":

        value = st.number_input("Enter Temperature")

        from_unit = st.selectbox(
            "From",
            ["Celsius", "Fahrenheit"]
        )

        to_unit = st.selectbox(
            "To",
            ["Celsius", "Fahrenheit"]
        )

        result = value

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32

        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9

        st.success(f"Converted Temperature: {result}")

# =========================
# MATERIAL DENSITY CHECKER
# =========================

elif menu == "Material Density Checker":

    st.header("🧱 Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Cast Iron": 7200
    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density = materials[material]

    st.info(f"Density of {material} = {density} kg/m³")

st.write("---")
st.caption("Mechanical Engineering Web App using Streamlit")
