from unittest import main

from classes import Request, Store, Shop

storage = Store(items={"телефон": 10, "компьютер": 10, "телевизор": 20})
shop = Shop(items={"телефон": 3, "компьютер": 3, "телевизор": 3})

storages = {
    'склад': storage,
    'магазин': shop,
}

while True:
    for storage_name in storages:
        print(f"Сейчас в {storage_name}:\n {storages[storage_name].get_items()}")
    user_text = input("Введите команду:\n")
    if user_text == "стоп":
        break
    else:
        try:
            request = Request(request=user_text)
            request.move()
        except Exception as e:
            print(f"Произошла ошибка {e}, играем дальше")

    # print("Текущие площади:")
    # print(f"Склад: {storage}")
    # print(f"Магазин: {shop}")
    # user_text = input("Введите команду:\n")
    # if user_text == "стоп":
    #     break
    # else:
    #     try:
    #         req = Request(user_text)
    #         req.move()
    #     except Exception as e:
    #         print(f"Произошла ошибка {e}, но не расстраивайтесь, играйте далее")

if __name__ == '__main__':
    main()
