def test_string_methods(string):
  """
  Проверяет все методы строк на указанной строке.

  Args:
    string: Строка для проверки.
  """

  # capitalize()
  assert string.capitalize() == "Hello world"

  # casefold()
  assert string.casefold() == "hello world"

  # center()
  assert string.center(10, "*") == "***hello***"

  # count()
  assert string.count("l") == 3

  # encode()
  assert string.encode("utf-8") == b"hello world"

  # endswith()
  assert string.endswith("world") == True

  # expandtabs()
  assert string.expandtabs(4) == "hello    world"

  # find()
  assert string.find("l") == 2

  # format()
  assert string.format(name="John Doe") == "Hello, John Doe!"

  # format_map()
  assert string.format_map({"name": "John Doe"}) == "Hello, John Doe!"

  # index()
  assert string.index("l") == 2

  # isalnum()
  assert string.isalnum() == True

  # isalpha()
  assert string.isalpha() == True

  # isascii()
  assert string.isascii() == True

  # isdecimal()
  assert string.isdecimal() == False

  # isdigit()
  assert string.isdigit() == False

  # isidentifier()
  assert string.isidentifier() == True

  # islower()
  assert string.islower() == True

  # isnumeric()
  assert string.isnumeric() == False

  # isprintable()
  assert string.isprintable() == True

  # isspace()
  assert string.isspace() == False

  # istitle()
  assert string.istitle() == False

  # isupper()
  assert string.isupper() == False

  # join()
  assert " ".join(["a", "b", "c"]) == "a b c"

  # ljust()
  assert string.ljust(10, "*") == "**********hello world"

  # lower()
  assert string.lower() == "hello world"

  # lstrip()
  assert string.lstrip() == "ello world"

  # maketrans()
  assert "".maketrans("a", "b") == {}

  # partition()
  assert string.partition(" ") == ("hello", " ", "world")

  # replace()
  assert string.replace("world", "universe") == "hello universe"

  # rfind()
  assert string.rfind("l") == 5

  # rindex()
  assert string.rindex("l") == 5

  # rjust()
  assert string.rjust(10, "*") == "hello world**********"

  # rpartition()
  assert string.rpartition(" ") == ("hello world", "", " ")

  # rsplit()
  assert string.rsplit(" ", 1) == ("hello", "world")

  # rstrip()
  assert string.rstrip() == "hello world"

  # split()
  assert string.split(" ") == ["hello", "world"]

  # splitlines()
  assert string.splitlines() == ["hello world"]

  # startswith()
  assert string.startswith("hello") == True

  # strip()
  assert string.strip() == "hello world"

  # swapcase()
  assert string.swapcase() == "HELLO WORLD"

  # title()
  assert string.title() == "Hello World"

  # translate()
  assert string.translate({" ": "-"}) == "hello-world"

  # upper()
  assert string.upper() == "HELLO WORLD"

  # zfill()
  assert string.zfill(10) == "00000000hello world"


def main():
  string = "hello world"
  test_string_methods(string)
