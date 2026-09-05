"""
Tech Stack Recommender
-----------------------
DecodeLabs - Artificial Intelligence Track - Project 3 (AI Recommendation Logic)

This script builds a content-based recommendation engine that maps a user's
skills to the most relevant job roles, using TF-IDF feature weighting and
Cosine Similarity scoring.

Pipeline (Input -> Process -> Output):
    1. Ingestion  -> capture the user's skills (minimum 3)
    2. Scoring    -> vectorize skills with TF-IDF, score every role with
                     Cosine Similarity against the user profile
    3. Sorting    -> rank roles by descending similarity score
    4. Filtering  -> return only the Top-N (default 3) matches

Run with:
    python tech_stack_recommender.py
"""

import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_FILE = "raw skills.csv"
TOP_N = 3
MIN_SKILLS = 3


# ---------------------------------------------------------------------------
# STEP 1: INGESTION
# ---------------------------------------------------------------------------
def load_dataset(path: str) -> pd.DataFrame:
    """Load the job-role dataset (the 'items' in the recommendation engine)."""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        sys.exit(f"Could not find '{path}'. Make sure it's in the same folder as this script.")

    required_cols = {"Role", "Required_Skills"}
    if not required_cols.issubset(df.columns):
        sys.exit(f"'{path}' must contain columns: {required_cols}")

    return df


def get_user_skills(min_skills: int = MIN_SKILLS) -> list[str]:
    """
    Prompt the user for their skills.
    Accepts either comma-separated input on one line, or one skill per line.
    Enforces a minimum number of inputs for sufficient data density.
    """
    print("=" * 60)
    print(" TECH STACK RECOMMENDER — DecodeLabs Project 3")
    print("=" * 60)
    print(f"\nEnter at least {min_skills} skills, separated by commas.")
    print("Example: Python, Cloud Computing, Automation\n")

    raw = input("Your skills: ").strip()
    skills = [s.strip() for s in raw.split(",") if s.strip()]

    while len(skills) < min_skills:
        print(f"\nPlease enter at least {min_skills} skills for accurate matching.")
        raw = input("Your skills: ").strip()
        skills = [s.strip() for s in raw.split(",") if s.strip()]

    return skills


# ---------------------------------------------------------------------------
# STEP 2: SCORING
# ---------------------------------------------------------------------------
def score_roles(df: pd.DataFrame, user_skills: list[str]):
    """
    Build a shared TF-IDF vocabulary from the item corpus (role skill sets),
    transform the user profile into the same vector space, and compute
    Cosine Similarity between the user vector and every role vector.
    """
    corpus = df["Required_Skills"].tolist()
    user_profile = " ".join(user_skills)

    # Fit the vectorizer on the item corpus so item and user features
    # map to the exact same vocabulary space.
    vectorizer = TfidfVectorizer()
    item_vectors = vectorizer.fit_transform(corpus)
    user_vector = vectorizer.transform([user_profile])

    scores = cosine_similarity(user_vector, item_vectors).flatten()
    df = df.copy()
    df["match_score"] = scores
    return df


# ---------------------------------------------------------------------------
# STEP 3 & 4: SORTING + FILTERING
# ---------------------------------------------------------------------------
def rank_and_filter(df: pd.DataFrame, top_n: int = TOP_N) -> pd.DataFrame:
    """Sort roles by descending match_score and keep only the Top-N results."""
    ranked = df.sort_values(by="match_score", ascending=False)
    return ranked.head(top_n)


# ---------------------------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------------------------
def display_results(results: pd.DataFrame, user_skills: list[str]):
    print("\n" + "-" * 60)
    print(f" Based on your skills: {', '.join(user_skills)}")
    print(" Top career-path matches:")
    print("-" * 60)

    if results["match_score"].max() == 0:
        print("\nNo overlap found with the current dataset.")
        print("Falling back to trending roles for new users (cold start):\n")

    for rank, (_, row) in enumerate(results.iterrows(), start=1):
        pct = round(row["match_score"] * 100, 1)
        print(f"{rank}. {row['Role']:<25} match: {pct:>5}%")
        print(f"   skills: {row['Required_Skills']}\n")


def main():
    df = load_dataset(DATA_FILE)
    user_skills = get_user_skills()
    scored = score_roles(df, user_skills)
    top_matches = rank_and_filter(scored, TOP_N)
    display_results(top_matches, user_skills)


if __name__ == "__main__":
    main()