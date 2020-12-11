def distance(strand_a, strand_b):
    cont = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Different strings.")
    else:
        for item in range(len(strand_a)):
            if(strand_a[item] != strand_b[item]):
                cont += 1
        return(cont)
