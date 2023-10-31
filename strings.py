def my_function(text, method):
  """
  Возвращает результат применения указанного метода к исходной строке.

  Args:
    text: Исходная строка.
    method: Название метода.

  Returns:
    Результат применения метода.
  """

  # Получаем результат применения метода
  result = getattr(text, method)()

  return result


# Выводим оригинальную строку
print(text)

# Делаем первую букву каждого слова заглавной
print(my_function(text, "capitalize"))

# Переводим текст в нижний регистр
print(my_function(text, "casefold"))

# Добавляем пробелы. Конкретно то количество пробелов которые мы указываем в параметре
print(my_function(text, "center"))

def my_function(text):
  """
  Возвращает словарь, где ключ - это название метода, а значение - результат его применения к исходной строке.

  Args:
    text: Исходная строка.

  Returns:
    Словарь.
  """

  results = {}

  # Делаем первую букву каждого слова заглавной
  results["capitalize"] = text.capitalize()

  # Переводим текст в нижний регистр
  results["casefold"] = text.casefold()

  # Добавляем пробелы. Конкретно то количество пробелов которые мы указываем в параметре
  results["center"] = text.center(40)

  return results


print(my_function("Привет всем, как дела?"))
