"""
===================================================================
PERSONAL PORTFOLIO WEBSITE - UPPARA KAVYA CHARITHA
===================================================================
Built exclusively using Python and Streamlit.
NO HTML, CSS, JavaScript, or external frontend languages used.
Clean, modular, responsive, and beginner-friendly architecture.
===================================================================
"""

import streamlit as st

# Configure page settings (must be the first Streamlit command)
st.set_page_config(
    page_title="Uppara Kavya Charitha | AI & Software Developer Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Import data and modular sections
from portfolio_data import PROFILE, CONTACT_INFO, RESUME_TEXT
from sections import (
    render_home,
    render_about,
    render_skills,
    render_projects,
    render_certifications,
    render_education,
    render_contact,
)

# Navigation Configuration
PAGE_DISPLAY_NAMES = [
    "🏠 Home",
    "👤 About Me",
    "⚡ Technical Skills",
    "🚀 Projects",
    "📜 Certifications",
    "🎓 Education",
    "📬 Contact",
]

PAGE_KEY_MAP = {
    "Home": "🏠 Home",
    "About Me": "👤 About Me",
    "Technical Skills": "⚡ Technical Skills",
    "Projects": "🚀 Projects",
    "Certifications": "📜 Certifications",
    "Education": "🎓 Education",
    "Contact": "📬 Contact",
}

REV_PAGE_KEY_MAP = {v: k for k, v in PAGE_KEY_MAP.items()}

# Initialize navigation session state
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"


def navigate_to(page_name: str):
    """Callback function to change active section from within any page."""
    if page_name in PAGE_KEY_MAP:
        st.session_state.current_page = page_name
        st.rerun()


# =========================================================================
# SIDEBAR NAVIGATION & PROFILE SUMMARY
# =========================================================================
with st.sidebar:
    # Sidebar Header Card
    with st.container(border=True):
        st.markdown(f"### 👩‍💻 {PROFILE['name']}")
        st.caption(f"{PROFILE['headline']}")
        st.write(f"🎓 **{PROFILE['role']}**")
        st.write(f"🏛️ *ALITS (2024–2028)*")
        st.info("🟢 Open for Internships")

    st.write("")  # Spacing

    # Sidebar Navigation Radio
    st.markdown("### 🧭 Navigation")
    current_display = PAGE_KEY_MAP.get(st.session_state.current_page, "🏠 Home")
    current_index = PAGE_DISPLAY_NAMES.index(current_display)

    chosen_display = st.radio(
        label="Select Portfolio Section:",
        options=PAGE_DISPLAY_NAMES,
        index=current_index,
        label_visibility="collapsed",
    )

    chosen_key = REV_PAGE_KEY_MAP[chosen_display]
    if chosen_key != st.session_state.current_page:
        st.session_state.current_page = chosen_key
        st.rerun()

    st.divider()

    # Sidebar Quick Contact & Social Links
    st.markdown("### 🔗 Quick Connect")
    st.link_button(
        label="💼 LinkedIn Profile",
        url=CONTACT_INFO["linkedin"],
        use_container_width=True,
    )
    st.link_button(
        label="🐙 GitHub Profile",
        url=CONTACT_INFO["github"],
        use_container_width=True,
    )
    st.link_button(
        label="✉️ Send Direct Email",
        url=f"mailto:{CONTACT_INFO['email']}",
        use_container_width=True,
    )

    st.write("")

    # Resume Download in Sidebar
    st.download_button(
        label="📄 Download Resume",
        data=RESUME_TEXT,
        file_name="Uppara_Kavya_Charitha_Resume.txt",
        mime="text/plain",
        use_container_width=True,
        type="primary",
    )

    st.divider()

    # Tech Stack & Credits in Sidebar
    with st.container(border=True):
        st.caption("⚡ **100% Python Architecture**")
        st.caption("Framework: Streamlit")
        st.caption("Design: Dark & Purple Theme")
        st.caption(f"© 2024–2028 {PROFILE['name']}")


# =========================================================================
# MAIN CONTENT ROUTER
# =========================================================================
current = st.session_state.current_page

if current == "Home":
    render_home(navigate_to)
elif current == "About Me":
    render_about(navigate_to)
elif current == "Technical Skills":
    render_skills(navigate_to)
elif current == "Projects":
    render_projects(navigate_to)
elif current == "Certifications":
    render_certifications(navigate_to)
elif current == "Education":
    render_education(navigate_to)
elif current == "Contact":
    render_contact(navigate_to)
else:
    render_home(navigate_to)


# =========================================================================
# FOOTER
# =========================================================================
st.write("")  # Spacing
st.divider()

with st.container():
    f_col1, f_col2, f_col3 = st.columns([2, 1, 1])
    with f_col1:
        st.write(
            f"**{PROFILE['name']}** — B.Tech Computer Science Engineering Student at "
            f"Anantha Lakshmi Institute of Technology and Sciences."
        )
        st.caption("Aspiring AI & Software Developer | Passionate about Python, AI & Computer Vision")
    with f_col2:
        st.write("**Navigation:**")
        st.caption("Use the sidebar or on-page buttons to explore sections smoothly.")
    with f_col3:
        st.write("**Built With:**")
        st.caption("🐍 100% Pure Python & Streamlit | Zero HTML/CSS/JS")

