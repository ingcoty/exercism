def latest(scores):
    return(scores[-1])


def personal_best(scores):
    return(max(scores))


def personal_top_three(scores):
    finalist = []
    for score in range(len(scores)):
        finalist.append(max(scores))
        scores.pop(scores.index(max(scores)))
        if score == 2:
            break

    return(finalist)
