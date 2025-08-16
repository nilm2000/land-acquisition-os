"""
Utility functions for deduplicating datasets.
"""

def remove_duplicates(items: list, key: str):
    """
    Removes duplicate dicts from a list based on a specific key.
    """
    seen = set()
    unique_items = []
    for item in items:
        val = item.get(key)
        if val not in seen:
            seen.add(val)
            unique_items.append(item)
    return unique_items
