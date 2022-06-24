#!/usr/bin/env python
# coding: utf-8

# In[21]:


# #3+4 -> 7 계산기 프로그램 작성
# 반복해서 작성
# 처음 문자에 'q'가 입력되면 프로그램 종료
# 1.문자열 입력 -> 리스트에 저장
# 2.리스트의 자료를 가져 옴
# 3.리스트의 처음 자료가 'q'이면 프로그램 종료
# 4.계속 입력 -> 리스트에 저장
input_data=[]
input_data=input('계산식 입력 : (ex:10 + 20)').split()
#print(input_data)
# a=int(input_data[0])+int(input_data[2])
# print(a)
while True:
    if input_data[0] == 'q' :
        print('종료합니다')
        break
    elif len(input_data) != 3 :
        print('계산식의 형식이 다릅니다')
        input_data=input('계산식 입력 : (ex:10 + 20)').split()
    else :
        if input_data[0] !='q':
        
            if '+' in input_data :
                a=int(input_data[0])+int(input_data[2])
                print('답은 {}입니다'.format(a))
                print()
            elif '-' in input_data :
                a=int(input_data[0])-int(input_data[2])
                print('답은 {}입니다'.format(a))
                print()
            elif '*' in input_data :
                a=int(input_data[0])*int(input_data[2])
                print('답은 {}입니다'.format(a))
                print()
            elif '/' in input_data :
                a=int(input_data[0])/int(input_data[2])
                print('답은 {}입니다'.format(a))
                print()
            input_data=input('계산식 입력 : (ex:10 + 20)').split()
        


# In[ ]:




