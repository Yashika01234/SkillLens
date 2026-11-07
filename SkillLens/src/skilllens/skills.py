from pathlib import Path
import pandas as pd


def load_skill_catalog(path="data/skills.csv"):
    """Load the skill names and aliases used by the simple skill extractor."""
    data = pd.read_csv(path).fillna("")
    catalog = {}
    for _, row in data.iterrows():
        skill = str(row["skill"]).strip()
        aliases = [item.strip() for item in str(row["aliases"]).split("|") if item.strip()]
        catalog[skill] = aliases
    return catalog


def extract_skills(text, catalog):
    """Return canonical skill names found in text, using whole-word matching."""
    import re

    text = text.lower()
    found = []
    for skill, aliases in catalog.items():
        terms = [skill] + aliases
        for term in terms:
            pattern = r"(?<![a-z0-9+#])" + re.escape(term.lower()) + r"(?![a-z0-9+#])"
            if re.search(pattern, text):
                found.append(skill)
                break
    return sorted(found)
