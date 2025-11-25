def reverse_str_rec(s):
    if len(s) <= 1: #ako e prazen ili edinitsa(1)
        return s
    return reverse_str_rec(s[1:]) + s[0]
