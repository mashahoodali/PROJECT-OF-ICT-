import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mechanical Converter", page_icon="⚙️")

# --- STUDENT CREDENTIALS SECTION ---
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")
st.markdown(f"""
### Student Information
*   **Full Name:** Tayyab Mustafa
*   **Roll Number:** 25-ME-84
""")
st.divider()

# --- APP LOGIC ---
tab1, tab2 = st.tabs(["Unit Converter", "Material Density Checker"])

with tab1:
    st.header("Mechanical Unit Converter")
    category = st.selectbox("Select Category", ["Length", "Pressure", "Force", "Energy"])
    
    col1, col2 = st.columns(2)
    
    if category == "Length":
        with col1:
            val = st.number_input("Input Value", value=1.0, key="len_in")
            u_from = st.selectbox("From", ["Meters (m)", "Millimeters (mm)", "Inches (in)", "Feet (ft)"])
        with col2:
            conversions = {"Meters (m)": 1.0, "Millimeters (mm)": 1000.0, "Inches (in)": 39.3701, "Feet (ft)": 3.28084}
            u_to = st.selectbox("To", ["Meters (m)", "Millimeters (mm)", "Inches (in)", "Feet (ft)"])
            res = val * (conversions[u_to] / conversions[u_from])
            st.metric("Result", f"{res:.4f} {u_to.split()[1]}")

    elif category == "Pressure":
        with col1:
            val = st.number_input("Input Value", value=1.0, key="pres_in")
            u_from = st.selectbox("From", ["Pascal (Pa)", "Bar", "PSI", "Atmosphere (atm)"])
        with col2:
            conversions = {"Pascal (Pa)": 1.0, "Bar": 1e-5, "PSI": 0.000145038, "Atmosphere (atm)": 9.8692e-6}
            u_to = st.selectbox("To", ["Pascal (Pa)", "Bar", "PSI", "Atmosphere (atm)"])
            res = val * (conversions[u_to] / conversions[u_from])
            st.metric("Result", f"{res:.4f} {u_to}")

with tab2:
    st.header("Material Density Checker")
    # Data for common engineering materials (kg/m^3)
    mat_data = {
        "Steel (Mild)": 7850,
        "Aluminum 6061": 2700,
        "Copper": 8960,
        "Titanium (Grade 5)": 4430,
        "Cast Iron": 7200,
        "Water": 1000
    }
    
    selected_mat = st.selectbox("Select Engineering Material", list(mat_data.keys()))
    density = mat_data[selected_mat]
    
    st.info(f"The standard density of **{selected_mat}** is **{density:,} kg/m³**.")
    
    st.subheader("Mass Calculator")
    vol = st.number_input("Enter Volume of Component (m³)", min_value=0.0, value=0.1, step=0.01)
    mass = density * vol
    st.success(f"Estimated Mass: **{mass:.2f} kg**")
