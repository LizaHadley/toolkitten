#Code that prints the '10 green bottles' song
a = 'There are '
b = ' green bottles sitting on the wall,'
c = 'And if 1 green bottle were to accidentally fall,'
d = 'there\'d be '
e = ' green bottles sitting on the wall.'

j=10
while j > 0:
	if j == 1:
		print('Now there\'s just ' + str(j) + ' bottle sitting on the wall,')
		print('Just ' + str(j) + ' bottle sitting on the wall,')
		print('And if that 1 bottle were to accidentaly fall,')
		print(d + 'no' + e + ' Argh!')
		break
	else:
 		print(a + str(j) + b)
 		print(str(j) + b)
 		print(c)
 		print(d + str(j-1) + e)
 		print('')
 		j -= 1
