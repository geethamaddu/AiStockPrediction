import streamlit as st
import requests

st.set_page_config(page_title="Multi Agent stock prediction system", layout="wide")
st.title("Multi Agent stock prediction system")
st.caption("Dynamic multi-agent stock intelligence with MCP-based tools")

symbol = st.text_input("Enter stock symbol", value="AAPL")
api_base = st.text_input("API URL", value="http://localhost:8000")

if st.button("Analyze"):
    response = requests.get(f"{api_base}/predict/{symbol.upper()}", timeout=60)
    data = response.json()

    st.subheader(f"{data['symbol']} — {data['outlook'].upper()}")
    st.write(f"**Confidence:** {data['confidence']}")
    st.write(data["summary"])

    st.write("### Supporting Signals")
    for item in data["supporting_signals"]:
        st.write(f"- {item}")

    st.write("### Risk Factors")
    for item in data["risk_factors"]:
        st.write(f"- {item}")

    st.write("### Agent Outputs")
    st.json(data["agent_outputs"])