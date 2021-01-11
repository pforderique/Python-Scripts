# TRIES (Prefix Trees)
# Piero Orderique
# 11 January 2021

# Trie (aka prefix trees) 
    # variant of the n-ary tree where nodes hold characters
    # null nodes indicate complete words
    # node in a trie could have 1 to ALPHABET_SIZE + 1 children

    # Use cases:
        # store the entire english language for quick prefix lookups
            # trie can check if string is valid prefix in O(k) time