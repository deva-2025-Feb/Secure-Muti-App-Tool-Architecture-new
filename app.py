import streamlit as st
import json
from auth import authenticate
from access_control import check_access
from query_router import route_query
from tools import TOOL_REGISTRY
from logger import log_action

st.set_page_config(page_title="Analytics Platform", layout="wide")

# ================= GLOBAL STYLE =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400&family=Inter:wght@400;700&display=swap');

.stApp {
    background-color: #000000;
    font-family: 'Inter', sans-serif;
}

header, footer {visibility: hidden;}

/* Make normal text white */
.stMarkdown, .stText, label {
    color: #FFFFFF;
}

.image-panel {
    height: 580px;
    border-radius: 20px;
    background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.9)), 
                url("https://images.unsplash.com/photo-1551288049-bebda4e38f71");
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 40px;
    border: 1px solid #1A1C1E;
}

.image-title {
    font-size: 48px;
    font-weight: 700;
    color: white;
    margin-bottom: 10px;
}

.stTextInput > div > div > input {
    background-color: #0A0A0A !important;
    color: white !important;
    border: 1px solid #1A1C1E !important;
    border-radius: 8px !important;
    height: 45px;
}

div.stButton > button {
    background: linear-gradient(90deg, #00F5FF 0%, #7000FF 100%);
    border: none;
    color: white;
    width: 100%;
    padding: 15px;
    border-radius: 8px;
    font-weight: 700;
    font-size: 16px;
    letter-spacing: 2px;
    margin-top: 15px;
    transition: 0.3s;
}

div.stButton > button:hover {
    box-shadow: 0 0 30px rgba(0, 245, 255, 0.4);
    transform: scale(1.01);
}
</style>
""", unsafe_allow_html=True)

# ================= LOAD SCHEMA =================
with open("schema.json") as f:
    schema = json.load(f)

# ================= SESSION =================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ================= LOGIN PAGE =================
if not st.session_state.authenticated:

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="image-panel">
            <div class="image-title">Analytics Platform</div>
            <div>
                Enterprise Sales & Finance Intelligence Dashboard
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<h3>Secure Login</h3>", unsafe_allow_html=True)

        username = st.text_input("User ID")
        password = st.text_input("Password", type="password")

        if st.button("LOGIN"):
            role = authenticate(username, password)
            if role:
                st.session_state.authenticated = True
                st.session_state.user = username
                st.session_state.role = role
                st.rerun()
            else:
                st.error("Invalid Credentials")

# ================= DASHBOARD =================
else:

    st.markdown(f"### Welcome {st.session_state.user} | Role: {st.session_state.role}")
    st.write(f"Schema Version: {schema['version']}")

    # Dashboard Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div><h4>Revenue</h4><h2 style="color:#00F5FF;">1.2M</h2></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div><h4>Transactions</h4><h2 style="color:#FF00FF;">5,320</h2></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div><h4>Growth</h4><h2 style="color:#00FF94;">18%</h2></div>', unsafe_allow_html=True)

    st.markdown("### Data Query")
    query = st.text_input("Enter analytics query")

    if st.button("RUN ANALYSIS") and query:
        tool_name = route_query(query)

        if tool_name is None:
            st.warning("Invalid dataset query")
            st.stop()

        if check_access(st.session_state.role, tool_name):
            fig = TOOL_REGISTRY[tool_name]()

            # ===== FORCE DARK THEME FOR ALL CHARTS =====
            fig.update_layout(
                paper_bgcolor="#000000",
                plot_bgcolor="#000000",
                font=dict(color="white"),
                legend=dict(font=dict(color="white"))
            )

            st.plotly_chart(fig, width="stretch")
            log_action(st.session_state.user, st.session_state.role, query, tool_name, "Allowed")

        else:
            st.error("Access Restricted")
            log_action(st.session_state.user, st.session_state.role, query, tool_name, "Denied")

    # Admin logs
    if st.session_state.role == "Admin":
        if st.button("VIEW LOGS"):
            try:
                with open("audit_log.txt", "r") as f:
                    logs = f.read()
                st.text_area("System Logs", logs, height=300)
            except FileNotFoundError:
                st.warning("No logs available")

    # Logout
    if st.button("LOGOUT"):
        st.session_state.authenticated = False
        st.rerun()