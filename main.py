from classes import storage_1, storage_2, shop_1, Request

while True:
    print("Текущие площади:")
    print(f"Склад_1: {storage_1}")
    print(f"Склад_2: {storage_2}")
    print(f"Магазин: {shop_1}")
    user_text = input("Введите команду:\n")
    if user_text == "стоп":
        break
    else:
        try:
            req = Request(user_text)
            req.move()
        except Exception as e:
            print(f"Произошла ошибка {e}, но не расстраивайтесь, играйте далее")
