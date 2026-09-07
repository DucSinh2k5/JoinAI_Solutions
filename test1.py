






from itertools import combinations
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def most_similar_pair(lines):
    """Return the indexes of the two most similar lines."""
    if len(lines) < 2:
        raise ValueError("At least two lines are required")

    vectors = TfidfVectorizer().fit_transform(lines)
    best_pair = None
    best_similarity = float("-inf")

    for first, second in combinations(range(len(lines)), 2):
        similarity = cosine_similarity(vectors[first], vectors[second])[0, 0]
        if similarity > best_similarity:
            best_similarity = similarity
            best_pair = (first, second)

    return best_pair


def main():
    # Read one text line per document from standard input.
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        raise ValueError("Input must contain at least two lines")

    first, second = most_similar_pair(lines)
    print(first, second)


if __name__ == "__main__":
    main()