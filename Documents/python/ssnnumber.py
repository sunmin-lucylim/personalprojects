# -*- coding: utf-8 -*- 

print("주민등록번호 검증 시스템입니다!")
ssn_number = input("주민등록번호를 입력하세요.")

# 성별 검증 
sex = ssn_number[6]
if ssn_number[6] in ['1','2','3','4'] :
    print("성별 검증되었습니다.")
else:
    print("잘못된 성별입니다.")

# 지역 검증 

region = ssn_number[7:9]
if ssn_number[7:9] in ["%.2d" % i for i in range(96)]:
    print("지역 검증되었습니다.")
else: 
    print("잘못된 지역입니다.")

# 종합 검증 

logic = [2,3,4,5,6,7,8,9,2,3,4,5]
number = 0
for i in range(0, len(logic)):
    number += int(ssn_number[i]) * int(logic[i])
if 11-(number%11) == int(ssn_number[12]):
    print ("이 주민등록번호는 유효한 주민등록번호 입니다.")
else:
    print ("이 주민등록번호는 유효하지 않은 주민등록번호 입니다.")


