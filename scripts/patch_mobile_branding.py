from pathlib import Path

p = Path("app.py")
s = p.read_text(encoding="utf-8")

# Royal pink theme
s = s.replace("--lime: #c7f36b;", "--lime: #f04b9b;")
s = s.replace("--cyan: #63d9e8;", "--cyan: #f7a6cc;")

# Smaller logo
s = s.replace(
    'st.image(str(logo_path), width=155)',
    'st.image(str(logo_path), width=115)'
)

# Responsive styling
mobile_css = """
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
"""

if "SUPERRR ROYAL PINK + MOBILE RESPONSIVE" not in s:
    s = s.replace("</style>", mobile_css + "\n</style>", 1)

p.write_text(s, encoding="utf-8")
print("Updated: Royal Pink theme + mobile responsive layout")
