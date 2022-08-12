import sys



num1 = "2376732"
num2 = "131042"
num1 = num1[::-1]
num2 = num2[::-1]
print(num1,num2)
num1_size = len(num1)
num2_size = len(num2)
size = min(num1_size,num2_size)
temp = ""
flag = False
for i in range(size):
    a = int(num1[i]) +  int(num2[i])
    if flag == True:# 전의 자릿수 덧셈에서 올림이 발생하였다면 1증가 시켜줌
        a += 1
    if a >= 8:
        flag = True # 다음 자리는 1올림해주어야한다는 표시를 함
        a %= 8 # 8진수이므로 8이상이되면 올림이되고 나머지로 확정
    else:# 8미만이면 그냥 더하면되므로 올림발생하지 않도록 flag변수 설정을 해줌
        flag = False
    temp += str(a)


# 위의 과정이 끝나도 마지막 원소가 8이상이되면 올림수 1을 해주어야하므로 또 한번더 체크한다
# 또 자릿수가 다르므로 계속해서 더 길이가 긴 문자열 나머지를 붙여주어야 한다
for i in range(len(num2),len(num1)):
    a = int(num1[i])
    if flag == True:
        a += 1
        flag = False
    temp += str(a)
temp = temp[::-1] # 최종적으로 다 더한 후에 다시 뒤집어주어야함
print(temp)