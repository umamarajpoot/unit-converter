import streamlit as st
from pint import UnitRegistry

# Initialize Pint UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

# Define a function to perform the conversion
def convert_units(value, from_unit, to_unit):
    try:
        quantity = Q_(value, from_unit)
        converted_quantity = quantity.to(to_unit)
        return converted_quantity.magnitude
    except:
        return None

# Streamlit App
st.set_page_config(page_title="✨ Ultimate Unit Converter", layout="centered")

# Custom CSS for styling and animations
st.markdown("""
    <style>
    /* General Styling */
    body {
        font-family: 'Helvetica', sans-serif;
        background: #f5f5f5;
    }
    .stButton>button {
        background-color: #28a745;
        color: white;
        font-size: 18px;
        padding: 12px 28px;
        border-radius: 12px;
        border: none;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #218838;
        transform: scale(1.1);
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        border: 2px solid #28a745;
        border-radius: 12px;
        padding: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: border-color 0.3s ease;
    }
    .stTextInput>div>div>input:focus, .stSelectbox>div>div>div:focus {
        border-color: #218838;
    }
    .stMarkdown h1 {
        color: #28a745;
        text-align: center;
        animation: fadeIn 2s;
    }
    .stMarkdown h2, .stMarkdown h3 {
        color: #28a745;
    }
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #c3e6cb;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        animation: slideIn 0.5s ease;
    }
    .stError {
        background-color: #f8d7da;
        color: #721c24;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #f5c6cb;
        animation: shake 0.5s;
    }
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-10px); }
        50% { transform: translateX(10px); }
        75% { transform: translateX(-10px); }
        100% { transform: translateX(0); }
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #28a745;
        color: white;
        text-align: center;
        padding: 12px;
        font-size: 18px;
        font-family: 'Helvetica', sans-serif;
        animation: fadeIn 2s;
    }
    .footer a {
        color: white;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        color: #f5f5f5;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("✨ Ultimate Unit Converter")
st.markdown("""
Convert any unit to another in real-time! Supports various unit categories like length, mass, temperature, volume, speed, energy, and more. Experience fast and accurate conversions with a clean interface.
""")

# Define supported units
unit_categories = {
    "Length": ["meter", "foot", "inch", "mile", "kilometer", "light_year"],
    "Mass": ["kilogram", "gram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "gallon", "cubic_meter", "cubic_inch"],
    "Speed": ["meter_per_second", "kilometer_per_hour", "mile_per_hour"],
    "Energy": ["joule", "calorie", "btu", "electron_volt"],
}

# Input fields
st.subheader("Enter Your Conversion")

col1, col2, col3 = st.columns(3)

with col1:
    value = st.number_input("Enter value:", value=1.0, step=0.1)

with col2:
    category = st.selectbox("Select unit category:", list(unit_categories.keys()))

with col3:
    from_unit = st.selectbox("Select from unit:", unit_categories[category])

# Target unit
target_unit = st.selectbox("Select target unit:", unit_categories[category])

# Convert button
if st.button("Convert"):
    with st.spinner("Converting..."):  # Add a loading spinner
        result = convert_units(value, from_unit, target_unit)
        if result is not None:
            st.success(f"✅ **{value} {from_unit} = {result:.4f} {target_unit}**")
        else:
            st.error("❌ Invalid conversion. Please check your units.")

# Add examples and references
with st.expander("📚 Supported Units and Examples"):
    st.markdown("""
    ### Length
    - **meter (m)**, **foot (ft)**, **inch (in)**, **mile (mi)**, **kilometer (km)**, **light_year (ly)**
    - Example: `5 feet to meters`, `10 kilometers to miles`

    ### Mass
    - **kilogram (kg)**, **gram (g)**, **pound (lb)**, **ounce (oz)**, **ton (ton)**
    - Example: `10 kg to pounds`, `150 grams to ounces`

    ### Temperature
    - **celsius (°C)**, **fahrenheit (°F)**, **kelvin (K)**
    - Example: `32 celsius to fahrenheit`, `100 kelvin to celsius`

    ### Volume
    - **liter (L)**, **gallon (gal)**, **cubic_meter (m³)**, **cubic_inch (in³)**
    - Example: `1 gallon to liters`, `5 cubic meters to gallons`

    ### Speed
    - **meter_per_second (m/s)**, **kilometer_per_hour (km/h)**, **mile_per_hour (mph)**
    - Example: `60 mph to km/h`, `10 m/s to km/h`

    ### Energy
    - **joule (J)**, **calorie (cal)**, **btu (BTU)**, **electron_volt (eV)**
    - Example: `1000 joules to calories`, `500 BTU to joules`

    ### How It Works
    1. Enter a value.
    2. Select the unit category (e.g., Length, Mass).
    3. Select the source unit (e.g., `feet`).
    4. Select the target unit (e.g., `meters`).
    5. Click **Convert** to see the result.
    """)
st.markdown("""
    <div class="footer">
        Developed with ❤️ by <a href="https://linkedin.com/in/umama-rajput-79603b301" target="_blank">Umama Rajput</a>
    </div>
    """, unsafe_allow_html=True)
