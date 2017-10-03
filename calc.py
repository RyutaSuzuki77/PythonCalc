# -*- coding: utf-8 -*-
flag = False;

while 1:

   if(flag == True):
       break;
   print("2桁または1桁同士の計算式を入力してください。");
   print("入力値同士はスペースで区切ってください。");
   a = raw_input().split();

   if a[1] == '+':
       print(int(a[0]) + int(a[2]));
   elif a[1] == '-':
       print(int(a[0]) - int(a[2]));
   elif a[1] == '*':
       print(int(a[0]) * int(a[2]));
   elif a[1] == '/':
       print(int(a[0]) / int(a[2]));
   else:
       print("入力形式が間違っています。");

   while 1:
       print("続けますか？ y/n");
       ans = raw_input();
       if(ans == 'y'):
           break;
       elif(ans == 'n'):
           flag = True;
           break;
       else:
           print("yかnを入力してください。");
       #2桁計算
       #エラーの文言修正
