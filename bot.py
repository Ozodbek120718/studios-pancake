"hello world".capitalize()
 # Output: "Hello world"
"HELLO WORLD".casefold()
# Output: "hello world"
"hello".center(10, "*")
# Output: "***hello***"
"hello world".count("l")
# Output: 3
"hello world".encode("utf-8")
# Output: b'hello world'
"hello world".endswith("world")
# Output: True
"hello\tworld".expandtabs(4)
# Output: "hello    world"
"hello world".find("l")
# Output: 2
"Hello, {name}!".format(name="John Doe")
# Output: "Hello, John Doe!"
format_map = {"name": "John Doe"}
"Hello, {name}!".format_map(format_map)
# Output: "Hello, John Doe!"
"hello world".index("l")
# Output: 2
"hello123".isalnum()
# Output: True
"hello".isalpha()
# Output: True
"hello".isascii()
# Output: True
"123".isdecimal()
# Output: True
"123".isdigit()
# Output: True
"my_variable".isidentifier()
# Output: True
"hello".islower()
# Output: True
"123".isnumeric()
# Output: True
"hello world".isprintable()
# Output: True

