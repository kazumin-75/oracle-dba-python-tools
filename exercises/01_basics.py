"""Python の基礎練習 / Basic Python exercises."""


def count_words(text: str) -> dict[str, int]:
    """文章の単語ごとの出現回数を数える / Count how many times each word appears."""
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    print(count_words("ORA-00600 ora-00600 ORA-04031"))
