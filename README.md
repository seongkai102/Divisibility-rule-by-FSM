# Divisibility-rule(배수 판별법)

## 3의 배수 판별코드

### 배수 판정법은 배수인지 확인하려는 수의 배수가 맞는지 간단히 확인하는 절차
  
n의 배수 판정법은 n의 이론적 성질을 이용하여 m = ∑_{k=0}^{l-1} m_k 10^k의 자리수 m_k에 대한 정보를 통해 m이 n의 배수인지 판정할 수 있는 절차이다.
<br />
상태 (State):
<br />
FSM은 여러 개의 상태를 가질 수 있습니다. 각 상태는 시스템의 특정 조건이나 상황을 나타냅니다.
<br />
초기 상태 (Initial State):
<br />
FSM은 항상 특정한 초기 상태에서 시작합니다.
<br />
입력 (Input):
<br />
FSM은 입력을 받아서 상태를 전이(변경)합니다. 입력은 이벤트, 신호, 문자 등 다양한 형태일 수 있습니다.
<br />
상태 전이 (State Transition):
<br />
특정 입력을 받았을 때 현재 상태에서 다음 상태로 이동하는 규칙입니다. 상태 전이 규칙은 상태 전이 테이블이나 상태 전이 함수로 표현될 수 있습니다.
<br />
최종 상태 (Final State):
<br />
FSM의 특정 상태 중 일부는 최종 상태로 정의될 수 있습니다. 최종 상태에 도달하면 FSM은 특정 동작을 수행하거나, 입력을 처리 완료했음을 나타냅니다.
