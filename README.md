# Divisibility-rule(배수 판별법)

## 3의 배수 판별

### 배수 판정법은 배수인지 확인하려는 수의 배수가 맞는지 간단히 확인하는 절차임
  
n의 배수 판정법은 n의 이론적 성질을 이용하여 m = ∑_{k=0}^{l-1} m_k 10^k의 자리수 m_k에 대한 정보를 통해 m이 n의 배수인지 판정할 수 있는 절차이다.

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
