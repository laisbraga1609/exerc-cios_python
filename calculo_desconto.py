preco = float(input('qual é o preco deste produto?R$'))
novo = preco-(preco*5/100)
print('o produto que custava {:.2f}, na promoçao, com desconto de 5% vai custar {:.2f}'.format(preco,novo))