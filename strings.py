text1 = 'hello world';


print('world!' not in text1);



for symbol in text1:
    print(symbol);


print(text1[4]);

print(len(text1));
# print(text1.__len__());


print(text1[2:7]);
print(text1[:6]);
print(text1[2:]);
print(text1[:]);
print(text1[:-3]);
text2= '      OZodbek       ' 
print(text2.upper());
print(text2.lower());

print(text2.rstrip().lstrip(), 4);
print(text2.strip(), 4);


# print(input('dsfdsf').strip());


print(text1.replace('world', text2.strip().lower().title()));


print(text1.split(' '));


text3 = 'ozodbek-odilbek'

print(text3.split('-'));



print(text3 + ' ' + 'asdd asdas'); 

print(text3 + str(3));

name = 'Ozodbek'
ocenka = 10

# text4 = 'Privet '+ name +', tvoya ocenka ' + ocenka;
text4 = 'Privet \'{0}\b\' \n tvoya \f ocenka \ooo {1}'.format(name, ocenka);
# text4 = '"sda d" - \'asdasd\' '
print(text4);


print('afgdf sdfgfdfg'.capitalize()); # делает предложение с заглавной