# برنامه ای بنویسید که یک متن از کاربر دریافت کند
# سپس دو کلمه از ورودی بگیرد
# و یکی را با دیگری در آن متن جابجا کند
text = input("Enter your text : ").lower()
str1 = input("Enter first string : ").lower()
str2 = input("Enter second string : ").lower()
print(text.replace(str1,str2))