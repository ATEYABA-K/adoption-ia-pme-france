# Adoption de l'IA par les entreprises françaises : l'angle mort des PME

Analyse de l'adoption de l'intelligence artificielle par les entreprises en France entre 2023 et 2025, à partir des données officielles Insee. L'angle retenu : comment cette adoption varie selon la taille de l'entreprise, et ce que ça dit d'un enjeu business concret pour toute équipe Digital/Data/IA qui cible le marché PME/Pro (B2B).

## Contexte

Ce projet simule le type d'analyse qu'un·e Chargé·e de Projet Digital/Data/IA pourrait produire pour justifier ou orienter une stratégie IA différenciée selon la taille des clients B2B — un exercice personnel pour mettre en pratique la chaîne complète : sourcing de données publiques, nettoyage Python, calcul d'indicateurs, dashboard.

## Résultats clés

![Adoption de l'IA par taille d'entreprise en 2025](chart_ia_par_taille_2025.png)

**L'écart d'adoption de l'IA entre grandes entreprises et PME s'est creusé entre 2023 et 2025, pas comblé.**

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| 10 à 49 salariés | 5 % | 9 % | 15 % |
| 50 à 249 salariés | 10 % | 15 % | 31 % |
| 250 salariés ou plus | 21 % | 33 % | 58 % |
| **Écart (250+ vs 10-49)** | **16 pts** | **24 pts** | **43 pts** |

Toutes les tailles d'entreprise progressent, mais les grandes entreprises accélèrent nettement plus vite que les petites. Une PME de 2025 utilise l'IA à peu près autant qu'une grande entreprise en... 2022-2023. Ce n'est pas un problème qui se résout tout seul avec le temps : l'écart relatif s'élargit chaque année.

Ce constat est cohérent avec ce qu'on observe généralement sur la diffusion des technologies en entreprise : les grandes structures ont plus facilement les ressources (budget, compétences internes, capacité à absorber le risque d'un déploiement raté) pour adopter tôt une technologie encore mouvante. Sans accompagnement spécifique, l'écart tend à se creuser avant de se refermer.

![Évolution de l'adoption de l'IA par taille d'entreprise, 2023-2025](chart_evolution_ia_2023_2025.png)

## Source des données

[Insee Première n° 2120](https://www.insee.fr/fr/statistiques/9025878) — *Les technologies de l'information et de la communication dans les entreprises en 2025*, issu de l'enquête TIC entreprises (Insee, 2023-2025). Champ : entreprises de 10 salariés ou plus, France, secteurs principalement marchands hors agricole/financier/assurance.

## Méthodologie

1. Téléchargement du fichier Insee brut (`data/IP2120.xlsx`)
2. Repérage de l'onglet pertinent ("Figure 1") parmi les 11 onglets du classeur, via l'onglet "Sommaire"
3. Nettoyage en Python/pandas : suppression des lignes de titre/notes, séparation des deux blocs "taille d'entreprise" / "secteur d'activité", passage en format tidy (une ligne = une observation)
4. Export vers `data/insee_ia_pour_powerbi.csv`
5. Dashboard interactif construit sur Looker Studio (2 graphiques : comparaison par taille en 2025, évolution 2023-2025 par taille), graphiques exportés en image pour ce README

## Limites à connaître

- Les chiffres mesurent la part d'**entreprises déclarant utiliser au moins une techno d'IA** — pas l'intensité d'usage ni la maturité du déploiement. Une entreprise qui teste un seul outil d'IA générative compte autant qu'une entreprise avec plusieurs cas d'usage industrialisés.
- L'enquête ne couvre que les entreprises de 10 salariés ou plus : les TPE (moins de 10 salariés), qui composent l'essentiel du tissu PME/Pro en France, ne sont pas dans le champ.
- La causalité n'est pas établie ici : l'écart par taille peut refléter des facteurs autres que la taille elle-même (secteur d'activité, maturité numérique préalable, structure des coûts). Le tableau complémentaire 6 du fichier Insee ("Modélisation de la probabilité d'utiliser au moins une technologie d'IA") va plus loin sur ce point mais n'a pas été exploité ici.

## Pistes pour aller plus loin

- Croiser avec le tableau "en % des effectifs" (poids des salariés concernés, pas seulement des entreprises) pour évaluer l'ampleur réelle de l'écart.
- Ajouter la dimension sectorielle (déjà présente dans les données brutes, pas encore dans le dashboard).
- Comparer à la France par rapport à l'Union européenne (donnée disponible dans le fichier source).

## Fichiers

- `data/IP2120.xlsx` — fichier source Insee brut
- `data/insee_ia_pour_powerbi.csv` — données nettoyées, format tidy, prêtes pour un outil BI
- `chart_ia_par_taille_2025.png`, `chart_evolution_ia_2023_2025.png` — graphiques exportés

## Auteur

Alvin Kouadio
