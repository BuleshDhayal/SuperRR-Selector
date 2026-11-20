from pathlib import Path

path = Path("app.py")
source = path.read_text(encoding="utf-8")

# 1. Add final Royal Pink + responsive CSS before data loading.
marker = "@st.cache_data"
if marker not in source:
    raise SystemExit("ERROR: @st.cache_data marker not found. No changes made.")

css = r'''
# ================= SUPERRR FINAL ROYAL PINK DESIGN =================
st.markdown("""
<style>
:root {
    --rr-pink: #f04498;
    --rr-light: #ff9bc9;
    --rr-deep: #a81760;
    --rr-navy: #090d19;
    --rr-panel: #171b30;
    --rr-border: rgba(255, 105, 180, .28);
}

/* Premium pink + navy background */
.stApp {
    background:
      radial-gradient(ellipse at 85% 0%, rgba(240,68,152,.17), transparent 38%),
      radial-gradient(ellipse at 0% 45%, rgba(168,23,96,.12), transparent 35%),
      #090d19 !important;
    color: #fff !important;
}

h1, h2, h3 {
    color: #fff !important;
}

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #25172f, #151d31) !important;
    border: 1px solid var(--rr-border) !important;
    border-radius: 15px !important;
}

[data-testid="stMetricValue"] {
    color: var(--rr-light) !important;
}

[data-testid="stMetricLabel"] {
    color: #c7b5c5 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #171326 0%, #0b1020 100%) !important;
    border-right: 1px solid var(--rr-border) !important;
}

[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: rgba(240,68,152,.10) !important;
    border-color: rgba(240,68,152,.35) !important;
}

[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
    background: rgba(240,68,152,.17) !important;
    border: 1px solid rgba(240,68,152,.65) !important;
}

[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {
    color: #ff9bc9 !important;
}

/* Alerts: readable text */
[data-testid="stAlert"] {
    background: linear-gradient(110deg, #32172d, #21192c) !important;
    border: 1px solid rgba(255,105,180,.42) !important;
    border-radius: 13px !important;
}
[data-testid="stAlert"] p,
[data-testid="stAlert"] div {
    color: #fff0f7 !important;
}

/* Project credits card */
div[style*="grid-template-columns:1.3fr 1.4fr 1fr 1fr"] {
    background: transparent;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    border: 1px solid #f04498 !important;
    border-radius: 10px !important;
}
.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #a81760 !important;
    color: white !important;
    border-color: #ff9bc9 !important;
}

/* Avoid content escaping viewport */
html, body, .stApp {
    max-width: 100%;
    overflow-x: hidden !important;
}
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.block-container {
    max-width: 100% !important;
    min-width: 0 !important;
}

/* Phone layout */
@media screen and (max-width: 768px) {
    .block-container {
        padding: 1rem .8rem 2.5rem !important;
        max-width: 100% !important;
    }

    h1 {
        font-size: 1.65rem !important;
        line-height: 1.2 !important;
    }
    h2 {
        font-size: 1.3rem !important;
    }

    /* Hero: logo above title, never side-by-side */
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) {
        display: flex !important;
        flex-direction: column !important;
        flex-wrap: nowrap !important;
        width: 100% !important;
        gap: 8px !important;
        align-items: stretch !important;
    }
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) > [data-testid="column"] {
        width: 100% !important;
        min-width: 0 !important;
        flex: 1 1 100% !important;
    }
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) [data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
    }
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) [data-testid="stImage"] img {
        width: auto !important;
        max-width: 155px !important;
        max-height: 175px !important;
        object-fit: contain !important;
    }
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) h1,
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) h2,
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) p {
        text-align: center !important;
    }

    /* Credits: 2 columns instead of 4 */
    div[style*="grid-template-columns:1.3fr 1.4fr 1fr 1fr"] {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 17px 12px !important;
    }

    [data-testid="stMetric"] {
        padding: 11px !important;
        min-width: 0 !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 1.25rem !important;
        overflow-wrap: anywhere !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: .72rem !important;
    }

    [data-testid="stDataFrame"],
    [data-testid="stTable"] {
        max-width: 100% !important;
    }
}
</style>
""", unsafe_allow_html=True)

'''

if "SUPERRR FINAL ROYAL PINK DESIGN" not in source:
    source = source.replace(marker, css + "\n" + marker, 1)

# 2. Replace sidebar footer with name and social links.
old_footer = '''st.sidebar.divider()
st.sidebar.caption("SuperRR Selector | Research and prediction kept separate")
st.sidebar.caption("Registration / fitness status: NOT VERIFIED unless independently confirmed.")'''

new_footer = r'''st.sidebar.divider()
st.sidebar.markdown("""
<div style="
    background:linear-gradient(145deg,#30152d,#171b30);
    border:1px solid rgba(240,68,152,.48);
    border-radius:15px;
    padding:15px 13px;
    margin-top:8px;
">
    <div style="font-size:10px;letter-spacing:2px;color:#ff91c4;font-weight:900;">
        PROJECT CREATOR
    </div>
    <div style="font-size:19px;font-weight:900;color:#ffffff;margin-top:7px;">
        Bulesh Choudhary
    </div>
    <div style="font-size:11px;color:#cbb8ca;margin:4px 0 12px;">
        Founder &amp; Research Lead
    </div>
    <a href="https://www.instagram.com/buleshdhayal/"
       target="_blank"
       style="display:block;color:#ff9bc9;text-decoration:none;font-weight:700;padding:5px 0;">
       ◎ Instagram · @buleshdhayal
    </a>
    <a href="https://www.linkedin.com/in/bulesh-choudhary96/"
       target="_blank"
       style="display:block;color:#ff9bc9;text-decoration:none;font-weight:700;padding:5px 0;">
       in LinkedIn · Bulesh Choudhary
    </a>
</div>
<div style="font-size:10px;color:#9aa3b5;margin-top:12px;line-height:1.6;">
    SuperRR Selector · Research and prediction kept separate<br>
    Registration / fitness status: NOT VERIFIED unless independently confirmed.
</div>
""", unsafe_allow_html=True)'''

if old_footer in source:
    source = source.replace(old_footer, new_footer, 1)
elif "instagram.com/buleshdhayal" not in source:
    raise SystemExit("ERROR: Sidebar footer marker not found. CSS was not saved.")

# 3. Save.
path.write_text(source, encoding="utf-8")
print("Royal Pink theme + mobile hero + social sidebar updated.")
