def search(input, pattern):
    def create_frag(input, pattern):
        frag = [{}] * len(pattern)
        chars = set(input + pattern)
        frag[0] = {char: 0 for char in chars}
        frag[0][pattern[0]] = 1
        sim = 0
        for i in range(1, len(pattern)):
            frag[i] = {char: frag[sim][char] for char in chars}
            frag[i][pattern[i]] = i + 1
            simulation_state = frag[sim][pattern[i]]
        return frag
    if pattern == "":
        return 0
    frag = create_frag(input, pattern)
    i, state = 0, 0


    while i < len(input) and state < len(pattern):
        state = frag[state][input[i]]
        i += 1
    if state == len(input):
        return i - len(pattern)
    else:
        return - 1