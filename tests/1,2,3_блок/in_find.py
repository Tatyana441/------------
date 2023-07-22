# s = 'My Name is Julia'

# # if 'Name' in s:
# #     print('Substring found')

# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')    


# проверка, что в текущем url содержится строка login (нужно реализовать, это часть)

assert "login" in browser.current_url # сообщение об ошибке

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"    