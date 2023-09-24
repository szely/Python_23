import itertools
import chess

val = [1, 2, 3, 4, 5, 6, 7, 8]

perm_set_one = list(itertools.permutations(val,8))
perm_set_two = itertools.permutations(perm_set_one,2)

chess.find_iterr(perm_set_two, 4)