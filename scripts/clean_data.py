"""
Nettoyage des donnees Insee (enquete TIC entreprises, adoption de l'IA) :
fichier Excel brut a 11 onglets -> format tidy exploitable dans un outil BI.

Usage : python3 scripts/clean_data.py
"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
RAW_FILE = DATA_DIR / "IP2120.xlsx"
TIDY_FILE = DATA_DIR / "insee_ia_pour_powerbi.csv"


def clean_to_tidy() -> pd.DataFrame:
    df = pd.read_excel(RAW_FILE, sheet_name="Figure 1", skiprows=3)
    df = df.rename(columns={"Unnamed: 0": "categorie"})

    taille = df.iloc[1:4].copy()
    taille["type"] = "Taille de l'entreprise"
    secteur = df.iloc[5:15].copy()
    secteur["type"] = "Secteur d'activité"

    df_clean = pd.concat([taille, secteur], ignore_index=True)
    df_clean = df_clean.rename(columns={
        2023: "France_2023", 2024: "France_2024", 2025: "France_2025",
        "2023.1": "UE_2023", "2024.1": "UE_2024", "2025.1": "UE_2025",
    })

    df_tidy = df_clean.melt(
        id_vars=["categorie", "type"],
        value_vars=["France_2023", "France_2024", "France_2025", "UE_2023", "UE_2024", "UE_2025"],
        var_name="zone_annee",
        value_name="part_entreprises_ia_pct",
    )
    df_tidy[["zone", "annee"]] = df_tidy["zone_annee"].str.split("_", expand=True)
    df_tidy = df_tidy.drop(columns=["zone_annee"])
    df_tidy["annee"] = df_tidy["annee"].astype(int)

    expected_rows = 13 * 6
    if len(df_tidy) != expected_rows:
        raise ValueError(f"Nombre de lignes inattendu apres nettoyage : {len(df_tidy)} (attendu {expected_rows})")

    df_tidy.to_csv(TIDY_FILE, index=False, encoding="utf-8-sig")
    print(f"OK — {len(df_tidy)} lignes ecrites dans {TIDY_FILE}")
    return df_tidy


if __name__ == "__main__":
    clean_to_tidy()
