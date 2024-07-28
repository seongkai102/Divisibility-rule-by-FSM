n = input()

transitions = [
    [0, 1, 2, 0, 1, 2, 0, 1, 2, 0],
    [1, 2, 0, 1, 2, 0, 1, 2, 0, 1],
    [2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
]

state_list = [0]

[state_list.append(transitions[state_list[i]][int(digit)]) for i, digit in enumerate(n)]

final_state = state_list[len(n)]

print(int(final_state == 0))
