def boyer_moore(transcript:str, search:str):
    T = len(transcript)
    S = len(search)
    bad_match_table = dict()
    occurence_indices = []
    
    #* create bad match table - O(S)
    for idx, char in enumerate(search):
        #? if last character, assign it S
        if idx == S - 1: bad_match_table[char] = S
        else: bad_match_table[char] = S - 1 - idx

    #* run the algorithm
    t_idx = S - 1
    while t_idx < T:
        print(f"t_idx is now {t_idx}")

        match_found = True
        for idx in range(0, S):
            print(f"on chars {transcript[t_idx - idx]} and {search[S - 1 - idx]}")

            #? if char not in bad match table, skip S spaces!
            if transcript[t_idx - idx] not in bad_match_table:
                t_idx += S
                match_found = False
                print(f"\tnot in bad_match_table. skipping {S} steps!")
                break

            #? if char doesn't match with our current character,
            #? but IS in bad match table, skip that many spaces
            elif transcript[t_idx - idx] != search[S - 1 - idx]:
                print(f"\tskipping {bad_match_table[transcript[t_idx - idx]]} steps!")
                t_idx += bad_match_table[transcript[t_idx - idx]]
                match_found = False
                break
            
            #? else we have a match here! lets keep trying the rest
            else: continue

        #? check if we broke out of loop only becuase we found a match!
        if match_found: 
            occurence_indices.append(t_idx - S + 1)
            t_idx += S

    print(bad_match_table)
    print(occurence_indices)

boyer_moore('macgmaseehburtonmaseeh', 'maseeh')