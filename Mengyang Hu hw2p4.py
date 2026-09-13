"""HW2P4 — Tuple unpacking and dictionary methods.

DSE I1020, Fall 2026. Fill in every section marked TODO.
Running `python hw2p4.py` must print output for all five tasks without error.
"""

import time

# Shared data for Tasks 1, 2, and 5. Do not change these values.
PAIRS = [
    ("Ada", 91),
    ("Grace", 97),
    ("Katherine", 95),
    ("Dorothy", 88),
    ("Mary", 97),
]


def task1_top_scorer(pairs):
    """Return the (name, score) tuple with the highest score.

    Use tuple unpacking in a for loop. Do NOT call max().
    If two people tie for the highest score, return the one that appears first.
    """
    # TODO: unpack each tuple as `for name, score in pairs:` and track the best so far.
    max_name, max_score = pairs[0]
    for name, score in pairs[1:]:
        if score > max_score:
            max_name, max_score = name, score
    return (max_name, max_score)

    raise NotImplementedError


def task2_safe_lookup(pairs, missing_key):
    """Build a dict from `pairs` and return `.get(missing_key, <default>)`.

    Pick a sensible default and say in a comment why you chose it.
    """
    # TODO: build the dict, then use .get() with a default.
    score_dict = dict(pairs)
    return score_dict.get(missing_key, 'Student not exist!') #to show user that the student is not exist in the PAIRS list
    
    raise NotImplementedError


def task3_merge(a, b):
    """Merge dicts `a` and `b` and return the result.

    Use dict unpacking ({**a, **b}) or .update().
    """
    # TODO: merge the two dicts.
    # TODO (comment): on a key present in BOTH dicts, whose value survives, and why?
    merged_dict = a.copy()
    merged_dict.update(b)

    return merged_dict 
    #the value in b suvives because .update() will take every key lookup in a:
    #if it is not exist in a ,it will create a new key-value pair;
    #if it is exist in a ,the value in b will replace the value in a.

    raise NotImplementedError


def task4_unhashable_key():
    """Demonstrate that a list cannot be used as a dict key.

    Trigger the error inside a try/except, and return the exception message as a string.
    """
    # TODO: try `{[1, 2]: "value"}` (or d[[1, 2]] = "value") inside try/except TypeError.
    # TODO (comment): what does "hashable" mean, and why is `list` not hashable?
    try:
        {[1, 2]: "value"} 
    except TypeError as error:
        return str(error)
    # 'hash' is a value that computed from content by hash algorithm. For specific content, hash is ALMOST unique.So hash can be used to lookup data.
    # 'hashable' means it is unchangeable. List is changeable so not 'hashable'.

    raise NotImplementedError


def task5_timing(pairs, repeats=100000):
    """Time the Task 1 unpacking loop against a manual index-based loop.

    Return (unpacking_seconds, index_seconds, ratio) where
    ratio = index_seconds / unpacking_seconds.
    """
    # TODO: time `for name, score in pairs:` over `repeats` iterations with time.time().
    # TODO: time `for i in range(len(pairs)):` with pairs[i][0], pairs[i][1] over `repeats`.
    # TODO: compute and return the ratio.
    start_time = time.time()
    for i in range(repeats):
        max_name, max_score = pairs[0]
        for name, score in pairs[1:]:
            if score > max_score:
                max_name, max_score = name, score 
    unpacking_seconds = time.time() - start_time

    start_time = time.time()
    for i in range(repeats):
        max_name = None
        max_score = -1
        for j in range(len(pairs)):
            if pairs[j][1] > max_score:
                max_name = pairs[j][0]
                max_score = pairs[j][1]
    
    index_seconds = time.time() - start_time

    ratio = index_seconds / unpacking_seconds
    return (unpacking_seconds, index_seconds, ratio)
    raise NotImplementedError


def main():
    print("Task 1 — top scorer:", task1_top_scorer(PAIRS))

    print("Task 2 — safe lookup:", task2_safe_lookup(PAIRS, "Alan"))

    scores_a = {"Ada": 91, "Grace": 97}
    scores_b = {"Grace": 99, "Katherine": 95}
    print("Task 3 — merged:", task3_merge(scores_a, scores_b))

    print("Task 4 — unhashable key error:", task4_unhashable_key())

    unpacking_s, index_s, ratio = task5_timing(PAIRS)
    print(f"Task 5 — unpacking: {unpacking_s:.4f}s  index: {index_s:.4f}s  ratio: {ratio:.2f}")


if __name__ == "__main__":
    main()
