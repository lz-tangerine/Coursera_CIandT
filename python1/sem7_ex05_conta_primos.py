def maior_primo(v):
    primo = 0
    i = 2
    while i <= v:
        div = 0
        c = 1
        while c <= v:
            if i % c == 0:
                div += 1
            c += 1
        if div <= 2:
            primo = i
        i += 1
    return(primo)