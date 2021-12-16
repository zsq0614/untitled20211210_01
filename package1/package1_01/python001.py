#coding=utf-8
money = int(input("请输入你手上有多少钱$"))
print(money)
print("你的金额为"+ str(money) +"元")
shop = [
    ("agv头盔",1780),
    ("MT纤维头盔",1300),
    ("SHoe仙鹤头盔",3699),
    ("Arai头盔",4600),
    ("LS2头盔",379),
    ("so1头盔",699),
    ("坦克头盔",350)
]

shoping_cart = []
print("<<<<<<<<<<<<<<<<<<<<<下面是头盔商品列表：")
for shoping in shop:
    print (shop.index(shoping),shoping)
while True:
    shop_id = raw_input("请输入你要购买的商品id：")
    if shop_id.isdigit():
        shop_id = int(shop_id)
        print(type(shop_id))
        if shop_id < len(shop) and shop_id >= 0:
            price = shop[shop_id][1]
            print(price)
            if money > price:
                money = money -price
                print("购买成功本次消费金额："+str(price)+";剩余金额："+str(money))
            else:
                print("您的金额不足，你要购买商品价格为"+str(price)+";剩余金额："+str(money))
        else:
            print("请输入编号范围之内的数字")
    elif shop_id == "q" or "Q":
        print("欢迎下次光临")
        break
    else:
        print("输入有误，请重新输入")