# TODO Найдите количество книг, которое можно разместить на дискете

obiomdisk = 1.44 * 1024**2
obiomkniga = 4 * 25 * 50 * 100

skolkoknig = obiomdisk / obiomkniga

print("Количество книг, помещающихся на дискету:", int(skolkoknig))
