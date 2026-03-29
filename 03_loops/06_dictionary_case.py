users = [
    {"id": 1, "total": 100, "coupon": "t20"},
    {"id": 2, "total": 150, "coupon": "p20"},
    {"id": 3, "total": 200, "coupon": "s20"},
]

discounts = {
    "t20": (0.2, 0),
    "p20": (0.5, 0),
    "s20": (0, 10),
}

for user in users:
    percent, flat = discounts.get(user["coupon"],(0,0))
    total = user["total"]
    discount = user["total"] * percent + flat
    final_price = total - discount
    print(f"{user["id"]} total bill is {user["total"]} and got a dicount of {discount} rupees. So the final bill is of {final_price} rupees")



from collections import namedtuple

chaiProfile = namedtuple("chaiprofile",["flavour", "aroma"])