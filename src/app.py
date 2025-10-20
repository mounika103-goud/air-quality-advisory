"""Streamlit application entrypoint for Air Quality Advisory."""
import sys
from pathlib import Path

# Make project root importable so `from src...` works when running with Streamlit.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from typing import Tuple, Dict, Any

from src.utils.constants import (
    AQILevel,
    POLLUTANT_SPECS,
    INDIAN_CITIES,
    AQI_LEVELS,
    SENSITIVE_GROUPS,
    get_aqi_level,
    predict_aqi,
    generate_daily_trend
)

st.set_page_config(
    page_title="Air Quality Health Advisory",
    layout="wide",
    initial_sidebar_state="expanded"
)

def create_city_comparison(base_aqi: float) -> go.Figure:
    cities = []
    aqi_values = []
    for city, factors in INDIAN_CITIES.items():
        city_aqi = base_aqi * factors.get('base_mult', 1.0)
        cities.append(city)
        aqi_values.append(city_aqi)
    fig = px.bar(
        x=cities,
        y=aqi_values,
        title="AQI Comparison Across Cities",
        labels={"x": "City", "y": "AQI Value"},
        color=aqi_values,
        color_continuous_scale="RdYlGn_r"
    )
    fig.add_hline(y=50, line_dash="dash", line_color="green", annotation_text="Good")
    fig.add_hline(y=100, line_dash="dash", line_color="yellow", annotation_text="Moderate")
    fig.add_hline(y=150, line_dash="dash", line_color="orange", annotation_text="Unhealthy")
    return fig

def normalize_name(name: str) -> str:
    # Lowercase and remove non-alphanumeric characters to compare keys robustly
    return "".join([c for c in name.lower() if c.isalnum()])

def find_spec(pollutant_label: str) -> Dict[str, Any]:
    # Try exact lookup then normalized matching against POLLUTANT_SPECS keys
    if pollutant_label in POLLUTANT_SPECS:
        return POLLUTANT_SPECS[pollutant_label]
    norm = normalize_name(pollutant_label)
    for key, spec in POLLUTANT_SPECS.items():
        if normalize_name(key) == norm:
            return spec
    # fallback minimal spec
    return {
        'unit': '',
        'min': 0.0,
        'max': 100000.0,
        'default': 0.0,
        'warning_threshold': 0.0,
        'severe_threshold': float('inf'),
        'description': '',
        'health_effects': ''
    }

def check_pollutant_levels(pollutant: str, value: float, specs: dict) -> Tuple[str, str, str]:
    if value >= specs.get('severe_threshold', float('inf')):
        return (
            "SEVERE ALERT",
            f"⚠️ {pollutant} level is {value:.1f} {specs.get('unit','')} - SEVERE!\n{specs.get('health_effects','')}\nRecommended Action: Immediate reduction needed!",
            "red"
        )
    elif value >= specs.get('warning_threshold', float('inf')):
        return (
            "WARNING",
            f"⚡ {pollutant} level is {value:.1f} {specs.get('unit','')} - HIGH!\n{specs.get('health_effects','')}\nRecommended Action: Consider reduction measures",
            "orange"
        )
    return ("NORMAL", f"✅ {pollutant} level is within acceptable range", "green")

def create_trend_chart(pollutant: str, current_value: float, specs: dict) -> go.Figure:
    hours = 24
    now = datetime.now()
    x = [now + timedelta(hours=i) for i in range(hours)]
    base = float(current_value)
    y = []
    current_hour = now.hour
    for hour in range(hours):
        h = (current_hour + hour) % 24
        if 6 <= h <= 9:
            factor = 1.2
        elif 17 <= h <= 20:
            factor = 1.3
        else:
            factor = 0.9
        value = base * factor * (1 + np.random.normal(0, 0.08))
        y.append(max(0.0, value))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name=f'{pollutant} Trend'))
    if specs.get('warning_threshold', None) is not None:
        fig.add_hline(y=specs['warning_threshold'], line_dash="dash", line_color="orange", annotation_text="Warning Threshold")
    if specs.get('severe_threshold', None) is not None and np.isfinite(specs['severe_threshold']):
        fig.add_hline(y=specs['severe_threshold'], line_dash="dash", line_color="red", annotation_text="Severe Threshold")
    fig.update_layout(title=f"{pollutant} 24-Hour Trend Prediction", xaxis_title="Time", yaxis_title=f"Level ({specs.get('unit','')})", hovermode='x unified')
    return fig

def main():
    st.title("🌫️ Advanced Air Quality Prediction & Health Advisory")
    st.markdown("Real-time air quality monitoring and health impact assessment system")
    st.sidebar.title("⚙️ Configuration")
    selected_city = st.sidebar.selectbox("Select City", list(INDIAN_CITIES.keys()), help="Choose a city to adjust predictions based on local patterns")
    st.subheader("📊 Pollutant Measurements")
    tab1, tab2 = st.tabs(["Primary Pollutants", "Secondary Pollutants"])
    input_values = {}
    with tab1:
        st.markdown("### Major Air Pollutants")
        col1, col2, col3 = st.columns(3)
        alerts = []
        # Display labels (pretty) and use robust lookup for specs
        display_pollutants = ['NO₂', 'SO₂', 'CO', 'O₃', 'PM₁₀', 'PM₂.₅']
        for idx, disp in enumerate(display_pollutants):
            specs = find_spec(disp)
            with [col1, col2, col3][idx % 3]:
                value = st.number_input(
                    f"{disp} ({specs.get('unit','')})",
                    min_value=float(specs.get('min', 0.0)),
                    max_value=float(specs.get('max', 100000.0)),
                    value=float(specs.get('default', 0.0)),
                    format="%.2f",
                    help=f"{specs.get('description','')}\n\nSafe Limit: {specs.get('warning_threshold',0)} {specs.get('unit','')}"
                )
                status, message, color = check_pollutant_levels(disp, value, specs)
                if status != "NORMAL":
                    if status == "SEVERE ALERT":
                        st.error(message)
                    else:
                        st.warning(message)
                    with st.expander(f"📈 {disp} Trend Analysis"):
                        cA, cB = st.columns([2,1])
                        with cA:
                            trend_fig = create_trend_chart(disp, value, specs)
                            st.plotly_chart(trend_fig, use_container_width=True)
                        with cB:
                            safe_thresh = specs.get('warning_threshold', 1.0)
                            exceed_pct = ((value / safe_thresh) - 1) * 100 if safe_thresh else 0.0
                            st.markdown(f"### Current Status\n- **Level**: {value:.1f} {specs.get('unit','')}\n- **Safe Limit**: {safe_thresh} {specs.get('unit','')}\n- **Exceedance**: {exceed_pct:.1f}%\n\n### Health Implications\n{specs.get('health_effects','')}\n\n### Recommended Actions\n1. Monitor levels closely\n2. Implement reduction measures\n3. Consider protective equipment")
                    alerts.append({'pollutant': disp, 'value': value, 'threshold': specs.get('warning_threshold', 1.0), 'status': status})
                else:
                    st.success(message)
                input_values[disp] = value
        if alerts:
            st.markdown("---")
            st.markdown("### ⚠️ Active Alerts")
            for alert in alerts:
                thresh = alert['threshold'] or 1.0
                exceedance = ((alert['value'] / thresh) - 1) * 100
                st.markdown(f"- **{alert['pollutant']}**: {alert['status']} — Current: {alert['value']:.1f} ({exceedance:.1f}% above limit)")
    with tab2:
        st.markdown("### Additional Air Components")
        col1, col2, col3 = st.columns(3)
        secondary_pollutants = ['NH₃', 'Pb', 'CO₂', 'CH₄']
        for idx, disp in enumerate(secondary_pollutants):
            specs = find_spec(disp)
            with [col1, col2, col3][idx % 3]:
                value = st.number_input(
                    f"{disp} ({specs.get('unit','')})",
                    min_value=float(specs.get('min', 0.0)),
                    max_value=float(specs.get('max', 100000.0)),
                    value=float(specs.get('default', 0.0)),
                    format="%.2f",
                    help=f"{specs.get('description','')}\n\nHealth Effects: {specs.get('health_effects','')}"
                )
                if value >= specs.get('severe_threshold', float('inf')):
                    st.error(f"⚠️ Severe {disp} level!\n{specs.get('health_effects','')}")
                elif value >= specs.get('warning_threshold', float('inf')):
                    st.warning(f"⚡ High {disp} level\n{specs.get('health_effects','')}")
                input_values[disp] = value
    with st.expander("ℹ️ View Healthy Ranges and Health Effects"):
        for pollutant_key, specs in POLLUTANT_SPECS.items():
            st.markdown(f"### {pollutant_key}\n- **Description**: {specs.get('description','')}\n- **Normal Range**: < {specs.get('warning_threshold',0)} {specs.get('unit','')}\n- **Warning Level**: {specs.get('warning_threshold',0)} - {specs.get('severe_threshold',0)} {specs.get('unit','')}\n- **Severe Level**: > {specs.get('severe_threshold',0)} {specs.get('unit','')}\n- **Health Effects**: {specs.get('health_effects','')}\n---")
    if st.button("Predict AQI"):
        # Build input vector - use normalized lookup
        input_vector = [
            input_values.get('NO₂', input_values.get('NO2', 0.0)),
            input_values.get('SO₂', input_values.get('SO2', 0.0)),
            input_values.get('CO', 0.0),
            input_values.get('O₃', input_values.get('O3', 0.0)),
            input_values.get('PM₁₀', input_values.get('PM10', 0.0)),
            input_values.get('NH₃', input_values.get('NH3', 0.0))
        ]
        base_aqi = float(predict_aqi(input_vector))
        city_factor = INDIAN_CITIES.get(selected_city, {}).get('base_mult', 1.0)
        final_aqi = base_aqi * city_factor
        aqi_level = get_aqi_level(final_aqi)
        tabA, tabB, tabC = st.tabs(["AQI Prediction", "City Comparison", "Pollutant Analysis"])
        with tabA:
            c1, c2 = st.columns(2)
            with c1:
                st.metric("Predicted AQI", f"{final_aqi:.1f}")
                if isinstance(aqi_level, AQILevel):
                    st.markdown(f"### Status: {aqi_level.emoji} {aqi_level.category}")
                    st.markdown(aqi_level.description)
            with c2:
                st.markdown("### Recommendations")
                recs = getattr(aqi_level, "recommendations", []) if aqi_level else []
                for rec in recs:
                    st.markdown(f"- {rec}")
        with tabB:
            st.markdown("### 🏙️ City-wise AQI Comparison")
            city_fig = create_city_comparison(base_aqi)
            st.info(f"City Factor: {city_factor:.2f}x  •  Base AQI: {base_aqi:.1f}  •  Final AQI: {final_aqi:.1f}  •  Context: {selected_city}")
            st.plotly_chart(city_fig, use_container_width=True)
        with tabC:
            st.markdown("### 🔍 Pollutant Analysis")
            poll_names = ['NO₂', 'SO₂', 'CO', 'O₃', 'PM₁₀', 'NH₃']
            pollutant_df = pd.DataFrame({
                'Pollutant': poll_names,
                'Value': [input_values.get(n, 0.0) for n in poll_names],
                'Unit': [find_spec(n).get('unit','') for n in poll_names]
            })
            fig = px.bar(pollutant_df, x='Pollutant', y='Value', title='Current Pollutant Levels', color='Value', color_continuous_scale='RdYlGn_r', text='Value')
            fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("### Pollutant Information")
            for _, row in pollutant_df.iterrows():
                st.markdown(f"**{row['Pollutant']}**: {row['Value']:.1f} {row['Unit']}")
if __name__ == "__main__":
    main()
# ...existing code...streamlit run src\app.py