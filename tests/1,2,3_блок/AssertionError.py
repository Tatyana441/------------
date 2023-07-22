#assert abs(-42) == -42,"Should be absolute value of a number"

str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")

print(f"{2+3}")



# неправильно: 
assert self.catalog_link.text  == "Каталог", \
    f"Wrong language, got {self.catalog_link.text} instead of 'Каталог'" 


# правильно: 
catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'" 