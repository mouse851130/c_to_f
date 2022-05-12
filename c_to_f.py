c = input('請輸入攝氏溫度：') #攝氏轉華氏溫度練習
c = int(c) 
c = float(c) #可能是小數，所以用float
f = c / 5 * 9 + 32 #新的數字f，以c去做轉換得到的
print('華氏溫度為：', f) #把f給print出來，中間記得加逗號