#посчитаем цену товара со скидкой и узнаем, сколько сэкономили на разнице!

original_price = int(input('Какая цена без скидки на ценнике?: '))
discount_perc = int(input('И сколько процентов скидки обещают в магазине?: '))
disc_price = original_price / 100 * discount_perc
to_pay = original_price - disc_price
saved = original_price - to_pay
print(f'Значит, платим {to_pay} рубликов за эту вещь со скидкой {discount_perc} процентов ({disc_price} рублей)')
print(f'И мы сэкономили {saved} рубликов на бургер! Ура!')