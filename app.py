from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parent
SUB = ROOT / "reports" / "submission"
AUC = ROOT / "reports" / "auction_2027"

st.set_page_config(
    page_title="SuperRR Selector",
    page_icon="🏏",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --bg: #080d18;
    --panel: #111a2b;
    --panel2: #162238;
    --line: rgba(148,163,184,.16);
    --muted: #91a1b8;
    --white: #f4f7fb;
    --lime: #f04b9b;
    --cyan: #f7a6cc;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background:
      radial-gradient(ellipse at 80% 0%, rgba(44,91,130,.20), transparent 35%),
      radial-gradient(ellipse at 0% 35%, rgba(120,160,70,.08), transparent 30%),
      var(--bg);
    color: var(--white);
}
.block-container {
    max-width: 1500px;
    padding: 2.2rem 3rem 3rem;
}
h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: -.6px;
    color: var(--white);
}
h1 {font-size: 2.35rem !important; font-weight: 700 !important;}
h2 {font-size: 1.55rem !important; margin-top: 1.4rem !important;}
h3 {font-size: 1.12rem !important;}
p, label, .stMarkdown {color: #d3dceb;}
small, [data-testid="stCaptionContainer"] {color: var(--muted) !important;}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #101a2b 0%, #0b1220 100%);
    border-right: 1px solid var(--line);
}
[data-testid="stSidebar"] > div:first-child {padding-top: 1.5rem;}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {
    color: var(--lime) !important;
    font-size: 1.5rem !important;
}
[data-testid="stSidebar"] [role="radiogroup"] label {
    background: transparent;
    border: 1px solid transparent;
    border-radius: 10px;
    padding: 9px 12px;
    margin: 3px 0;
    transition: .2s ease;
}
[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: rgba(199,243,107,.08);
    border-color: rgba(199,243,107,.18);
}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
    background: rgba(199,243,107,.12);
    border-color: rgba(199,243,107,.35);
}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {
    color: var(--lime) !important;
    font-weight: 700;
}

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #17243a, #111b2d);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 18px 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,.16);
}
[data-testid="stMetricLabel"] {
    color: #9eafc5 !important;
    font-size: .82rem !important;
    font-weight: 600;
}
[data-testid="stMetricValue"] {
    color: var(--lime) !important;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.9rem !important;
    font-weight: 700;
}
[data-testid="stMetricDelta"] {font-size: .8rem;}

[data-testid="stDataFrame"], [data-testid="stTable"] {
    border: 1px solid var(--line);
    border-radius: 13px;
    overflow: hidden;
}
[data-testid="stPlotlyChart"] {
    background: rgba(17,26,43,.72);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 12px 10px 2px;
}
.stButton button, .stDownloadButton button {
    border-radius: 10px;
    border: 1px solid rgba(199,243,107,.35);
    background: rgba(199,243,107,.10);
    color: var(--lime);
    font-weight: 700;
    padding: .55rem 1rem;
    transition: .2s ease;
}
.stButton button:hover, .stDownloadButton button:hover {
    background: var(--lime);
    color: #101827;
    border-color: var(--lime);
}
.stTextInput input, .stSelectbox [data-baseweb="select"],
.stMultiSelect [data-baseweb="select"] {
    background: #121e31;
    border-color: var(--line);
    border-radius: 10px;
}
.stTextInput input:focus {
    border-color: var(--lime);
    box-shadow: 0 0 0 1px var(--lime);
}
[data-testid="stAlert"] {
    border-radius: 12px;
    border: 1px solid var(--line);
}
hr {border-color: var(--line) !important;}
[data-testid="stHeader"] {background: transparent;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}

/* SUPERRR ROYAL PINK + MOBILE RESPONSIVE */
:root {
    --royal-pink: #f04b9b;
    --royal-light: #ff9dca;
}

[data-testid="stMetricValue"] {
    color: #ff8fc5 !important;
}

[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
    background: rgba(240,75,155,.14) !important;
    border-color: rgba(240,75,155,.55) !important;
}

[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {
    color: #ff8fc5 !important;
}

[data-testid="stAlert"] {
    background: rgba(240,75,155,.12) !important;
    border: 1px solid rgba(240,75,155,.35) !important;
    color: #ffe5f1 !important;
}

@media (max-width: 768px) {
    .block-container {
        padding: 1rem .85rem 2rem !important;
    }

    h1 {
        font-size: 1.65rem !important;
    }

    h2 {
        font-size: 1.3rem !important;
    }

    [data-testid="stMetric"] {
        padding: 11px !important;
        border-radius: 12px !important;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.35rem !important;
    }

    [data-testid="stImage"] img {
        max-width: 100% !important;
        height: auto !important;
        object-fit: contain !important;
    }

    /* Keep logo and title side by side on phones */
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) {
        flex-wrap: nowrap !important;
        gap: 10px !important;
        align-items: center !important;
    }

    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) > [data-testid="column"]:first-child {
        flex: 0 0 29% !important;
        min-width: 0 !important;
    }

    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) > [data-testid="column"]:last-child {
        flex: 1 1 71% !important;
        min-width: 0 !important;
    }

    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) h1 {
        font-size: 1.45rem !important;
    }
}

</style>
""", unsafe_allow_html=True)



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



# SUPERRR LIGHT ROYAL PINK OVERRIDE
st.markdown("""
<style>
:root {
    --rr-pink: #e82e88;
    --rr-hot: #ff69ad;
    --rr-plum: #542044;
    --rr-ink: #382238;
    --rr-muted: #765e72;
    --rr-border: #f3b5d3;
}

/* Main canvas */
.stApp {
    background:
      radial-gradient(ellipse at 90% 0%, #ffe0ef 0%, transparent 42%),
      linear-gradient(135deg, #fff7fb 0%, #fce8f2 55%, #fff2f8 100%) !important;
    color: var(--rr-ink) !important;
}
[data-testid="stMain"] {
    background: transparent !important;
}
.block-container {
    max-width: 1500px !important;
}

/* Default readable text */
[data-testid="stMain"] p,
[data-testid="stMain"] label,
[data-testid="stMain"] li,
[data-testid="stMain"] [data-testid="stMarkdownContainer"] {
    color: var(--rr-ink);
}
[data-testid="stCaptionContainer"] p {
    color: var(--rr-muted) !important;
}
h1, h2, h3, h4 {
    color: #572044 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffe4f0 0%, #f9d6e8 100%) !important;
    border-right: 1px solid #efb0d0 !important;
}
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: #542044 !important;
}
[data-testid="stSidebar"] [role="radiogroup"] label {
    border-radius: 12px !important;
    margin: 4px 0 !important;
}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
    background: #f8c1dc !important;
    border: 1px solid #e82e88 !important;
}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {
    color: #a4145c !important;
    font-weight: 800 !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #ffffff, #fff0f7) !important;
    border: 1px solid #f0b5d2 !important;
    border-radius: 16px !important;
    box-shadow: 0 5px 18px rgba(130, 35, 85, .07) !important;
}
[data-testid="stMetricLabel"] {
    color: #76516c !important;
}
[data-testid="stMetricValue"] {
    color: #d51e79 !important;
}

/* Alerts - fix pale/invisible text */
[data-testid="stAlert"] {
    background: #fff0d8 !important;
    border: 1px solid #f0c58e !important;
    border-radius: 14px !important;
}
[data-testid="stAlert"] *,
[data-testid="stAlert"] p,
[data-testid="stAlert"] span {
    color: #56351d !important;
    opacity: 1 !important;
}

/* Tables and charts */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    border: 1px solid #efb5d2 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}
[data-testid="stPlotlyChart"] {
    background: #fffafd !important;
    border: 1px solid #f0bfd8 !important;
    border-radius: 15px !important;
}

/* Inputs */
input, textarea, [data-baseweb="select"] {
    border-color: #e9a3c7 !important;
}
.stButton > button, .stDownloadButton > button {
    background: linear-gradient(100deg, #e82e88, #bd176a) !important;
    color: white !important;
    border: 1px solid #d9277d !important;
    border-radius: 11px !important;
    font-weight: 700 !important;
}

/* Credits card: keep text dark and readable */
div[style*="grid-template-columns:1.3fr 1.4fr 1fr 1fr"] {
    background: linear-gradient(120deg, #ffe2ef, #fff4fa) !important;
    border-color: #efa4c9 !important;
}
div[style*="grid-template-columns:1.3fr 1.4fr 1fr 1fr"] * {
    color: #542044 !important;
}

/* Mobile */
@media screen and (max-width: 768px) {
    .block-container {
        padding: 1rem .8rem 2.5rem !important;
        width: 100% !important;
    }
    h1 { font-size: 1.55rem !important; line-height: 1.25 !important; }
    h2 { font-size: 1.25rem !important; }

    /* Hero logo and heading stack vertically */
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) {
        display: flex !important;
        flex-direction: column !important;
        gap: 8px !important;
        width: 100% !important;
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
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) img {
        max-width: 135px !important;
        max-height: 150px !important;
        object-fit: contain !important;
    }
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) h1,
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) h2,
    [data-testid="stHorizontalBlock"]:has([data-testid="stImage"]) p {
        text-align: center !important;
    }

    /* Stack columns on phones */
    [data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
    }
    [data-testid="stHorizontalBlock"] > [data-testid="column"] {
        min-width: min(100%, 240px) !important;
    }

    [data-testid="stMetric"] {
        padding: 12px !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 1.3rem !important;
    }

    /* Credits become two readable columns */
    div[style*="grid-template-columns:1.3fr 1.4fr 1fr 1fr"] {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 15px 10px !important;
    }

    [data-testid="stDataFrame"] {
        max-width: 100% !important;
        overflow-x: auto !important;
    }
}
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_csv(path):
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()


batters = load_csv(SUB / "all_batter_rankings.csv")
bowlers = load_csv(SUB / "all_bowler_rankings.csv")
profiles = load_csv(AUC / "released_89_ipl_profiles_v2.csv")
mapping = load_csv(AUC / "released_89_historical_mapping.csv")
bat_screen = load_csv(AUC / "released_batting_screen.csv")
bowl_screen = load_csv(AUC / "released_bowling_screen.csv")

# User-supplied provisional hypotheses. Not model-generated rankings.
predictions = pd.DataFrame([
    ["Nehal Wadhera", 1, "Indian middle-order finisher", False, 420, "Hypothesis: left-hand middle-order option"],
    ["Nitish Rana", 2, "Indian middle-order batter", False, 420, "Hypothesis: experienced middle order, part-time spin"],
    ["Mustafizur Rahman", 3, "Overseas death-overs pace", True, 920, "Hypothesis: slower-ball death option; expensive previous salary"],
    ["Matt Henry", 4, "Overseas powerplay pace", True, 200, "Hypothesis: new-ball option"],
    ["Akash Deep", 5, "Indian fast bowler", False, 100, "Hypothesis: Indian pace option"],
    ["Wanindu Hasaranga", 6, "Overseas spin all-rounder", True, 200, "Hypothesis: middle-over wicket-taker; fitness unverified"],
    ["Shahrukh Khan", 7, "Indian finisher", False, 400, "Hypothesis: power-hitter; historical ID mapping unavailable"],
    ["Tushar Deshpande", 8, "Indian death-overs pace", False, 650, "Hypothesis: Indian pace option"],
    ["Rachin Ravindra", 9, "Overseas batting all-rounder", True, 200, "Hypothesis: backup top-order and spin option"],
    ["Avesh Khan", 10, "Indian fast bowler", False, 975, "Hypothesis: Indian pace depth"],
], columns=[
    "player_name", "hypothesis_rank", "hypothesis_role",
    "overseas", "previous_salary_lakh", "hypothesis_note"
])

def money_lakh(x):
    try:
        return f"₹{float(x)/100:.2f} cr"
    except Exception:
        return "Not available"

def safe_num(row, col):
    try:
        v = row[col]
        return float(v) if pd.notna(v) else None
    except Exception:
        return None

st.title("🏏 SuperRR Selector")
st.caption("Historical pressure research | IPL 2027 RR auction workspace")

st.warning(
    "Research and prediction are separate. User-supplied player hypotheses "
    "are not model conclusions. Previous salary is not auction price."
)

pages = [
    "Overview",
    "RR Current Squad",
    "Historical Batter Rankings",
    "Historical Bowler Rankings",
    "RR Released Pool",
    "RR Predictions",
    "Player Profile",
    "RR Squad Builder",
]
page = st.sidebar.radio("Navigate", pages)


# SUPERRR_TOP_LEADERBOARD_LAYOUT
import html

def render_top10(title, df, name_col, score_col, accent, subtitle):
    st.markdown(f"""
    <div style="background:linear-gradient(120deg,#17263c,#101a2b);
                border:1px solid rgba(148,163,184,.18);
                border-radius:16px;padding:17px 18px 10px;">
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div>
          <div style="font-size:17px;font-weight:800;color:#f4f7fc;">{title}</div>
          <div style="font-size:11px;color:#91a2b9;margin-top:3px;">{subtitle}</div>
        </div>
        <div style="font-size:11px;font-weight:800;color:{accent};
                    background:{accent}18;padding:6px 10px;border-radius:20px;">
          TOP 10
        </div>
      </div>
    """, unsafe_allow_html=True)

    if df.empty:
        st.info("Ranking data not found.")
    else:
        top = df.sort_values("rank").head(10)
        for _, r in top.iterrows():
            rank = int(r["rank"])
            name = html.escape(str(r[name_col]))
            score = r[score_col]
            score_text = f"{float(score):.2f}" if pd.notna(score) else "N/A"
            formats = html.escape(str(r.get("formats", "")))
            color = "#c9f36a" if rank == 1 else "#dce5f2"
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:11px;
                        padding:8px 2px;border-bottom:1px solid rgba(148,163,184,.10);">
              <div style="width:25px;height:25px;display:flex;align-items:center;
                          justify-content:center;border-radius:8px;
                          background:{accent}18;color:{accent};
                          font-size:11px;font-weight:800;">{rank}</div>
              <div style="flex:1;min-width:0;">
                <div style="font-size:12px;font-weight:700;color:{color};
                            overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">{name}</div>
                <div style="font-size:10px;color:#8495ad;">{formats}</div>
              </div>
              <div style="font-size:13px;font-weight:800;color:#f4f7fc;">{score_text}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)



# RR BRANDED HOME DASHBOARD — OVERVIEW ONLY
if page == "Overview":
    logo_path = ROOT / "website" / "assets" / "rr_logo.png"
    logo_col, title_col = st.columns([1, 4], gap="large")

    with logo_col:
        if logo_path.exists():
            st.image(str(logo_path), width=115)
        else:
            st.markdown("# 🏏 RR")

    with title_col:
        st.markdown("""
        <div style="padding:8px 0 12px;">
          <div style="font-size:10px;letter-spacing:3px;font-weight:900;color:#f04b9b;">
            IPL 2027 · AUCTION INTELLIGENCE
          </div>
          <div style="font-family:Space Grotesk,sans-serif;font-size:38px;
                      font-weight:800;letter-spacing:-1.5px;color:#f7f8fc;margin-top:5px;">
            RAJASTHAN ROYALS
          </div>
          <div style="font-size:18px;font-weight:800;color:#f04b9b;margin-top:3px;">
            SUPERRR SELECTOR
          </div>
          <div style="font-size:12px;color:#a6b4c8;margin-top:9px;">
            Historical pressure-performance research · Player intelligence · IPL 2027 squad planning
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="height:1px;background:linear-gradient(90deg,#f04b9b,#68d9e8,transparent);
                margin:12px 0 18px;"></div>
    <div style="background:linear-gradient(110deg,#25172b,#151d30 65%,#102437);
                border:1px solid rgba(240,75,155,.27);border-radius:16px;
                padding:17px 19px;margin-bottom:20px;">
      <div style="font-size:10px;letter-spacing:2px;color:#f04b9b;font-weight:900;margin-bottom:14px;">
        PROJECT CREDITS
      </div>
      <div style="display:grid;grid-template-columns:1.3fr 1.4fr 1fr 1fr;gap:14px;">
        <div><div style="font-size:9px;color:#9aaac0;letter-spacing:1px;">PREPARED BY</div>
          <div style="font-size:15px;color:#fff;font-weight:800;margin-top:5px;">Bulesh Choudhary</div></div>
        <div><div style="font-size:9px;color:#9aaac0;letter-spacing:1px;">PROJECT ROLE</div>
          <div style="font-size:13px;color:#fff;font-weight:700;margin-top:5px;">Founder & Research Lead</div></div>
        <div><div style="font-size:9px;color:#9aaac0;letter-spacing:1px;">REPORT DATE</div>
          <div style="font-size:13px;color:#fff;font-weight:700;margin-top:5px;">18 November 2026</div></div>
        <div><div style="font-size:9px;color:#9aaac0;letter-spacing:1px;">RESEARCH PERIOD</div>
          <div style="font-size:13px;color:#fff;font-weight:700;margin-top:5px;">2022–2026</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div style="margin:20px 0 22px;padding:22px 24px;
                background:linear-gradient(110deg,#28152d,#171e34,#10283a);
                border:1px solid rgba(240,75,155,.38);
                border-radius:16px;text-align:center;">
      <div style="font-size:10px;letter-spacing:3px;
                  color:#ff78b8;font-weight:900;">
        A MESSAGE FOR THE ROYALS
      </div>
      <div style="font-size:25px;font-weight:900;
                  color:#ffffff;margin:10px 0;">
        BEST WISHES, RAJASTHAN ROYALS! 👑
      </div>
      <div style="font-size:15px;font-weight:700;
                  color:#ff78b8;">
        Play bold. Play fearless. Make every moment count.
      </div>
      <div style="font-size:12px;color:#cbd5e1;margin-top:12px;">
        Wishing the Royals a season filled with fearless cricket,
        unforgettable performances and the spirit of champions.
      </div>
      <div style="font-size:16px;font-weight:900;
                  color:#ff78b8;margin-top:14px;letter-spacing:3px;">
        HALLA BOL! 💗
      </div>
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("BATTER RANKINGS", len(batters))
    m2.metric("BOWLER RANKINGS", len(bowlers))
    m3.metric("RELEASED PLAYERS", len(profiles))
    m4.metric("RR HYPOTHESES", len(predictions))

    st.markdown("## Historical Top Performers")
    st.caption("ALL PLAYERS · DATA-BASED HISTORICAL RANKINGS")

    left_top, right_top = st.columns(2, gap="large")
    with left_top:
        render_top10("🏏 Top 10 Batters", batters, "player_name",
                     "final_score", "#f04b9b", "Pressure performance · Historical ranking")
    with right_top:
        render_top10("🎯 Top 10 Bowlers", bowlers, "player_name",
                     "final_score", "#68d9e8", "Pressure performance · Historical ranking")

    st.markdown("""
    <div style="margin:20px 0;padding:14px 16px;background:rgba(240,75,155,.07);
                border:1px solid rgba(240,75,155,.20);border-radius:12px;color:#d3dceb;font-size:12px;">
      <b style="color:#ff8fc5;">RESEARCH ≠ PREDICTION</b>
      &nbsp; Historical rankings are data-based. RR predictions remain separate and provisional.
      Previous salary is not auction price.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Rajasthan Royals · Auction Snapshot")
    a, b, c, d = st.columns(4)
    a.metric("REMAINING PURSE", "₹27.05 Cr")
    b.metric("AVAILABLE SLOTS", "6")
    c.metric("OVERSEAS SLOTS", "3")
    d.metric("RETAINED SQUAD", "19")

    st.caption("Scroll down for research coverage and verification notes.")

# ---------------- OVERVIEW ----------------
if page == "Overview":
    st.header("Project Overview")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Historical batters", len(batters))
    c2.metric("Historical bowlers", len(bowlers))
    c3.metric("RR released pool", len(profiles))
    c4.metric("RR provisional hypotheses", len(predictions))

    st.subheader("Two independent workstreams")
    left, right = st.columns(2)
    with left:
        st.markdown("### 📊 Data Research")
        st.write("All-player historical rankings. Retained/released status does not affect competition rankings.")
        if not batters.empty:
            st.write("Top batter:", batters.iloc[0]["player_name"])
        if not bowlers.empty:
            st.write("Top bowler:", bowlers.iloc[0]["player_name"])
    with right:
        st.markdown("### 🟠 RR Prediction")
        st.write("User-provided hypotheses, released-player profiles, squad needs and budget.")
        st.write("89 released players:", len(profiles))
        st.write("Pressure-model rerun for all 89: **Pending**")

    st.subheader("Data coverage")
    if not profiles.empty:
        matched = (profiles["mapping_status"] == "HISTORICAL ID MATCHED").sum()
        no_id = (profiles["mapping_status"] == "NO HISTORICAL ID MATCH").sum()
        a, b, c = st.columns(3)
        a.metric("Historical IDs matched", int(matched))
        b.metric("No historical ID", int(no_id))
        c.metric("Total released pool", len(profiles))

    st.info(
        "Current released-player IPL profiles are aggregate statistics. "
        "They are not pressure-model scores. Insufficient data is not treated as zero performance."
    )

# ---------------- BATTER RANKINGS ----------------
elif page == "Historical Batter Rankings":
    st.header("Historical Top 10 — Batters")
    st.caption("All-player research ranking. Not restricted to the RR released pool.")
    if batters.empty:
        st.error("Batter ranking CSV not found.")
    else:
        df = batters.sort_values("rank").copy()
        st.dataframe(df, use_container_width=True, hide_index=True)
        fig = px.bar(
            df.sort_values("final_score"),
            x="final_score", y="player_name", orientation="h",
            color="final_score", title="Historical Batter Final Scores",
            hover_data=["rank", "formats", "pressure_balls", "pressure_matches"]
        )
        st.plotly_chart(fig, use_container_width=True)
        st.download_button(
            "Download batter rankings CSV",
            df.to_csv(index=False).encode("utf-8"),
            "historical_batter_rankings.csv", "text/csv"
        )

# ---------------- BOWLER RANKINGS ----------------
elif page == "Historical Bowler Rankings":
    st.header("Historical Top 10 — Bowlers")
    st.caption("All-player research ranking. Not restricted to the RR released pool.")
    if bowlers.empty:
        st.error("Bowler ranking CSV not found.")
    else:
        df = bowlers.sort_values("rank").head(10).copy()
        st.dataframe(df, use_container_width=True, hide_index=True)
        fig = px.bar(
            df.sort_values("final_score"),
            x="final_score", y="player_name", orientation="h",
            color="final_score", title="Historical Bowler Top 10 Scores",
            hover_data=["rank", "formats", "pressure_balls", "pressure_matches"]
        )
        st.plotly_chart(fig, use_container_width=True)
        st.download_button(
            "Download bowler rankings CSV",
            df.to_csv(index=False).encode("utf-8"),
            "historical_bowler_rankings.csv", "text/csv"
        )

# ---------------- RELEASED POOL ----------------
elif page == "RR Released Pool":
    st.header("IPL 2027 — Released Player Pool")
    st.caption("Official released pool mapping and historical IPL 2022–2026 aggregate profiles.")

    if profiles.empty:
        st.error("Released profile CSV not found.")
    else:
        df = profiles.copy()
        search = st.text_input("Search player")
        if search:
            df = df[df["released_player_name"].str.contains(search, case=False, na=False)]

        overseas_filter = st.selectbox("Player category", ["All", "Indian", "Overseas"])
        if overseas_filter == "Indian":
            df = df[df["overseas_marked"] == False]
        elif overseas_filter == "Overseas":
            df = df[df["overseas_marked"] == True]

        status_filter = st.selectbox(
            "Historical mapping",
            ["All", "HISTORICAL ID MATCHED", "NO HISTORICAL ID MATCH"]
        )
        if status_filter != "All":
            df = df[df["mapping_status"] == status_filter]

        st.metric("Players shown", len(df))
        if "mapping_status" in df.columns:
            no_id_count = int((df["mapping_status"] == "NO HISTORICAL ID MATCH").sum())
            if no_id_count:
                st.info(
                    f"{no_id_count} displayed player(s) have no historical ID match. "
                    "Their zero placeholders must not be interpreted as zero performance."
                )
        cols = [
            "released_player_name", "overseas_marked", "listed_salary_lakh",
            "mapping_status", "batting_runs", "batting_balls", "strike_rate",
            "wickets", "legal_balls", "economy", "batting_status", "bowling_status"
        ]
        cols = [x for x in cols if x in df.columns]
        st.dataframe(df[cols], use_container_width=True, hide_index=True)

        st.download_button(
            "Download filtered released pool",
            df.to_csv(index=False).encode("utf-8"),
            "rr_released_pool.csv", "text/csv"
        )

# ---------------- PREDICTIONS ----------------
elif page == "RR Predictions":
    st.header("RR Provisional Predictions")
    st.error(
        "HYPOTHESIS ONLY — These names and role priorities were supplied by the user. "
        "They are not the output of the pressure model."
    )

    df = predictions.copy()
    if not profiles.empty:
        df = df.merge(
            profiles[[
                "released_player_name", "player_id", "mapping_status",
                "batting_runs", "batting_balls", "strike_rate",
                "wickets", "legal_balls", "economy",
                "batting_status", "bowling_status"
            ]],
            left_on="player_name", right_on="released_player_name",
            how="left"
        )

    df["previous_salary"] = df["previous_salary_lakh"].apply(money_lakh)
    display_cols = [
        "hypothesis_rank", "player_name", "hypothesis_role", "overseas",
        "previous_salary", "mapping_status", "batting_runs",
        "strike_rate", "wickets", "economy", "hypothesis_note"
    ]
    display_cols = [x for x in display_cols if x in df.columns]
    st.dataframe(df[display_cols], use_container_width=True, hide_index=True)

    st.markdown("### Budget illustration — previous salary only")
    st.write("This is not an auction-price forecast.")
    selected = st.multiselect(
        "Select hypothesis players for illustrative budget calculation",
        predictions["player_name"].tolist(),
        default=["Nehal Wadhera", "Matt Henry", "Akash Deep", "Wanindu Hasaranga", "Rachin Ravindra"]
    )
    chosen = predictions[predictions["player_name"].isin(selected)]
    total = chosen["previous_salary_lakh"].sum() / 100
    overseas_count = int(chosen["overseas"].sum())
    x, y, z = st.columns(3)
    x.metric("Previous salary total", f"₹{total:.2f} cr")
    y.metric("Overseas selected", f"{overseas_count}/3")
    z.metric("Illustrative remaining purse", f"₹{27.05-total:.2f} cr")
    if len(chosen) > 6 or overseas_count > 3 or total > 27.05:
        st.error("This illustrative combination exceeds at least one squad constraint.")
    else:
        st.success("Illustrative combination is within the stated 6-slot / 3-overseas / ₹27.05 cr limits, using previous salaries only.")

    st.download_button(
        "Download separate RR hypothesis list",
        predictions.to_csv(index=False).encode("utf-8"),
        "rr_user_hypotheses_NOT_FINAL.csv", "text/csv"
    )

# ---------------- PLAYER PROFILE ----------------
elif page == "Player Profile":
    st.header("Player Profile Explorer")
    st.write("Select a player to inspect available records across research and RR pool data.")

    names = set()
    if not profiles.empty:
        names.update(profiles["released_player_name"].dropna().astype(str))
    if not batters.empty:
        names.update(batters["player_name"].dropna().astype(str))
    if not bowlers.empty:
        names.update(bowlers["player_name"].dropna().astype(str))
    names.update(predictions["player_name"].tolist())

    selected_name = st.selectbox("Choose player", sorted(names))
    st.title(selected_name)

    p = profiles[profiles["released_player_name"].str.lower() == selected_name.lower()] if not profiles.empty else pd.DataFrame()
    br = batters[batters["player_name"].str.lower() == selected_name.lower()] if not batters.empty else pd.DataFrame()
    bw = bowlers[bowlers["player_name"].str.lower() == selected_name.lower()] if not bowlers.empty else pd.DataFrame()
    pr = predictions[predictions["player_name"].str.lower() == selected_name.lower()]

    if not p.empty:
        r = p.iloc[0]
        st.subheader("Released-pool record")
        a, b, c, d = st.columns(4)
        a.metric("Previous listed salary", money_lakh(r.get("listed_salary_lakh")))
        b.metric("Overseas", "Yes" if bool(r.get("overseas_marked")) else "No")
        c.metric("Historical mapping", str(r.get("mapping_status", "Unknown")))
        d.metric("Player ID", str(r.get("player_id", "Not mapped")))

        st.subheader("Batting — IPL aggregate")
        x, y, z, q = st.columns(4)
        x.metric("Runs", int(r["batting_runs"]) if pd.notna(r.get("batting_runs")) else "N/A")
        y.metric("Balls", int(r["batting_balls"]) if pd.notna(r.get("batting_balls")) else "N/A")
        z.metric("Strike rate", round(r["strike_rate"], 2) if pd.notna(r.get("strike_rate")) else "N/A")
        q.metric("Matches", int(r["batting_matches"]) if pd.notna(r.get("batting_matches")) else "N/A")
        st.write("Batting seasons:", r.get("batting_seasons", "Not available"))
        st.write("Batting status:", r.get("batting_status", "Not available"))

        st.subheader("Bowling — IPL aggregate")
        x, y, z, q = st.columns(4)
        x.metric("Wickets", int(r["wickets"]) if pd.notna(r.get("wickets")) else "N/A")
        y.metric("Legal balls", int(r["legal_balls"]) if pd.notna(r.get("legal_balls")) else "N/A")
        z.metric("Economy", round(r["economy"], 2) if pd.notna(r.get("economy")) else "N/A")
        q.metric("Bowling matches", int(r["bowling_matches"]) if pd.notna(r.get("bowling_matches")) else "N/A")
        st.write("Bowling seasons:", r.get("bowling_seasons", "Not available"))
        st.write("Bowling status:", r.get("bowling_status", "Not available"))
        st.write("Extras caveat:", r.get("extras_flag", "Not available"))
    else:
        st.info("No released-pool aggregate profile available for this player.")

    if not br.empty:
        st.subheader("Historical pressure research — Batter")
        st.dataframe(br, use_container_width=True, hide_index=True)
    if not bw.empty:
        st.subheader("Historical pressure research — Bowler")
        st.dataframe(bw, use_container_width=True, hide_index=True)

    if not pr.empty:
        st.subheader("RR user hypothesis — separate from model")
        st.dataframe(pr, use_container_width=True, hide_index=True)

    if p.empty and br.empty and bw.empty:
        st.warning("INSUFFICIENT DATA: No historical profile or ranking row found. This is not a zero-performance score.")

    st.info(
        "Pressure-model rerun for the complete 89-player released pool is pending. "
        "Do not interpret aggregate IPL stats as pressure scores."
    )


# ---------------- RR CURRENT SQUAD ----------------
elif page == "RR Current Squad":
    st.header("Rajasthan Royals | Current Retained Squad")
    st.markdown(
        "**19 players. One vision. A stronger Royals.**\n\n"
        "Built around explosive young Indian talent, experienced "
        "international match-winners and a varied bowling unit — "
        "the Royals have a strong foundation for the next auction."
    )
    st.caption("SQUAD SNAPSHOT | 18 NOVEMBER 2026 | USER-PROVIDED RETAINED LIST")

    retained = [
        ("Yashasvi Jaiswal", "Opener", "Indian"),
        ("Vaibhav Sooryavanshi", "Opener", "Indian"),
        ("Lhuan-dre Pretorius", "Wicketkeeper-batter", "Overseas"),
        ("Riyan Parag (C)", "Middle order / part-time spin", "Indian"),
        ("Dhruv Jurel", "Wicketkeeper-batter", "Indian"),
        ("Donovan Ferreira", "Middle-order batter", "Overseas"),
        ("Dasun Shanaka", "All-rounder", "Overseas"),
        ("Ravindra Jadeja", "Spin all-rounder", "Indian"),
        ("Shubham Dubey", "Finisher batter", "Indian"),
        ("Aman Rao Perala", "Batter", "Indian"),
        ("Jofra Archer", "Fast bowler", "Overseas"),
        ("Nandre Burger", "Left-arm pace", "Overseas"),
        ("Mohammed Shami (T)", "Fast bowler", "Indian"),
        ("Sandeep Sharma", "Pace bowler", "Indian"),
        ("Sushant Mishra", "Left-arm pace", "Indian"),
        ("Ravi Bishnoi", "Leg-spinner", "Indian"),
        ("Manimaran Siddharth (T)", "Spinner", "Indian"),
        ("Brijesh Sharma", "Spinner", "Indian"),
        ("Yash Raj Punja", "Bowler", "Indian"),
    ]

    squad = pd.DataFrame(retained, columns=["Player", "Role", "Category"])
    indian_count = int((squad["Category"] == "Indian").sum())
    overseas_count = int((squad["Category"] == "Overseas").sum())

    a, b, c, d = st.columns(4)
    a.metric("Retained players", len(squad))
    b.metric("Indian players", indian_count)
    c.metric("Overseas players", overseas_count)
    d.metric("Remaining purse", "₹27.05 Cr")

    st.markdown("### Retained Squad")
    filter_role = st.selectbox(
        "Filter squad",
        ["All players", "Indian", "Overseas"]
    )
    view = squad.copy()
    if filter_role != "All players":
        view = view[view["Category"] == filter_role]

    st.dataframe(
        view,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### Squad composition")
    role_groups = [
        ("Batting & Wicketkeeping", [
            "Opener", "Wicketkeeper-batter", "Middle order / part-time spin",
            "Middle-order batter", "Finisher batter", "Batter"
        ]),
        ("All-rounders", ["All-rounder", "Spin all-rounder"]),
        ("Bowling", [
            "Fast bowler", "Left-arm pace", "Pace bowler",
            "Leg-spinner", "Spinner"
        ]),
        ("Role to be confirmed", ["Role not confirmed"])
    ]

    for group_name, roles in role_groups:
        group = squad[squad["Role"].isin(roles)]
        with st.expander(f"{group_name} ({len(group)})", expanded=True):
            for _, player in group.iterrows():
                tag = "🌍 Overseas" if player["Category"] == "Overseas" else "🇮🇳 Indian"
                st.write(f"**{player['Player']}** — {player['Role']} · {tag}")

    st.markdown("### Auction position")
    x, y, z = st.columns(3)
    x.metric("Available slots", "6")
    y.metric("Overseas slots available", "3")
    z.metric("Remaining purse", "₹27.05 Cr")

    st.info(
        "This page displays the retained list supplied for this project. "
        "Player roles and retention details have not been independently re-verified here."
    )

# ---------------- SQUAD BUILDER ----------------
elif page == "RR Squad Builder":
    st.header("RR Squad Builder | Auction Planning")
    st.caption("Retained: 19 | Auction slots: 6 | Overseas additions: 3 | Purse: ₹27.05 Cr")
    st.warning(
        "Budget illustration uses previous listed salaries only. "
        "These are NOT predicted auction prices."
    )

    options = sorted(set(predictions["player_name"].dropna().tolist()))
    if not profiles.empty:
        options = sorted(
            set(options) |
            set(profiles["released_player_name"].dropna().astype(str).tolist())
        )

    chosen_names = st.multiselect(
        "Select released players for your proposed RR combination",
        options,
        max_selections=6
    )

    chosen = (
        profiles[profiles["released_player_name"].isin(chosen_names)].copy()
        if not profiles.empty else pd.DataFrame()
    )
    chosen = chosen.drop_duplicates("released_player_name")

    if chosen_names:
        missing_profiles = sorted(set(chosen_names) - set(chosen["released_player_name"]))
        if missing_profiles:
            st.warning(
                "No released-pool salary/profile record found for: "
                + ", ".join(missing_profiles)
            )

    if not chosen.empty:
        chosen["salary_cr_previous"] = pd.to_numeric(
            chosen["listed_salary_lakh"], errors="coerce"
        ).fillna(0) / 100

        total = float(chosen["salary_cr_previous"].sum())
        overseas = int(chosen["overseas_marked"].fillna(False).astype(bool).sum())
        slots = len(chosen)

        a, b, c, d = st.columns(4)
        a.metric("Slots used", f"{slots}/6")
        b.metric("Overseas used", f"{overseas}/3")
        c.metric("Previous salary total", f"₹{total:.2f} Cr")
        d.metric("Illustrative purse left", f"₹{27.05-total:.2f} Cr")

        display_cols = [
            "released_player_name", "overseas_marked",
            "listed_salary_lakh", "batting_runs", "strike_rate",
            "wickets", "economy", "batting_status", "bowling_status"
        ]
        display_cols = [c for c in display_cols if c in chosen.columns]
        st.dataframe(
            chosen[display_cols],
            use_container_width=True,
            hide_index=True
        )

        if overseas > 3 or total > 27.05:
            st.error("This combination exceeds the overseas limit or illustrative purse.")
        else:
            st.success("Combination is within the stated limits, based on previous salaries.")
    else:
        st.info("Select players above to build an illustrative auction combination.")

    st.markdown("### Squad constraints")
    st.write("- Maximum 6 auction additions")
    st.write("- Maximum 3 overseas additions")
    st.write("- Remaining purse: ₹27.05 crore")
    st.write("- Retained squad: 19 players")
    st.caption("Final auction prices, registration and availability are not verified.")


st.sidebar.divider()
st.sidebar.markdown("""
<div style="
    background:linear-gradient(145deg,#fff0f7,#fbd5e8);
    border:1px solid #e995bf;
    border-radius:16px;
    padding:15px 13px;
    margin-top:8px;
">
    <div style="font-size:10px;letter-spacing:2px;color:#c21d70;font-weight:900;">
        PROJECT CREATOR
    </div>
    <div style="font-size:19px;font-weight:900;color:#542044;margin-top:8px;">
        Bulesh Choudhary
    </div>
    <div style="font-size:11px;color:#76516c;margin:4px 0 15px;">
        Founder &amp; Research Lead
    </div>

    <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
      <a href="https://www.instagram.com/buleshdhayal/"
         target="_blank" rel="noopener"
         aria-label="Open Instagram"
         style="display:flex;align-items:center;justify-content:center;
         width:43px;height:43px;border-radius:12px;
         background:linear-gradient(135deg,#833ab4,#fd1d1d,#fcb045);">
        <svg viewBox="0 0 24 24" width="25" height="25" fill="none"
             stroke="white" stroke-width="2">
          <rect x="3" y="3" width="18" height="18" rx="5"/>
          <circle cx="12" cy="12" r="4"/>
          <circle cx="17.5" cy="6.5" r="1" fill="white" stroke="none"/>
        </svg>
      </a>

      <a href="https://www.linkedin.com/in/bulesh-choudhary96/"
         target="_blank" rel="noopener"
         aria-label="Open LinkedIn"
         style="display:flex;align-items:center;justify-content:center;
         width:43px;height:43px;border-radius:12px;background:#0a66c2;">
        <svg viewBox="0 0 24 24" width="25" height="25" fill="white">
          <path d="M5.2 3.5a2.2 2.2 0 1 0 0 4.4 2.2 2.2 0 0 0 0-4.4zM3.4 9.5h3.6V21H3.4zM9.1 9.5h3.4v1.6h.1a3.8 3.8 0 0 1 3.4-1.9c3.6 0 4.3 2.3 4.3 5.3V21h-3.6v-5.8c0-1.4 0-3.2-2-3.2s-2.3 1.5-2.3 3.1V21H9.1z"/>
        </svg>
      </a>
    </div>
    <div style="font-size:11px;color:#76516c;margin-top:12px;">
        Tap an icon to visit my profile
    </div>
</div>
<div style="font-size:10px;color:#76516c;margin-top:12px;line-height:1.6;">
    SuperRR Selector · Research and prediction kept separate<br>
    Registration / fitness status: NOT VERIFIED unless independently confirmed.
</div>
""", unsafe_allow_html=True)
