# 분자량 계산하기... 
# 성현이가 실망하길래... 직접 함...

import periodictable as pt

#나트륨의 분자량을 변수로!
Na = pt.Na
#수소의 분자량을 변수로!
H = pt.H
#탄소의 분자량을 변수로!
C = pt.C
#산소값을 변수로
O = pt.O
tansansusonatryum_mass = Na.mass + H.mass + C.mass + O.mass*3
print(f'탄산수소나트륨의 분자량은 {tansansusonatryum_mass}/mol 입니다.')