# بوت متجر عبايات - ثناء | thanaa.codes

print("=" * 40)
print("👗 متجر ثناء للعبايات - اهلا فيك")
print("=" * 40)

print("\n✨ تشكيلة العبايات:")
print("1. عباية كلاسيك سوداء - 250 ريال")
print("2. عباية مطرزة - 350 ريال")
print("3. عباية عملية يومية - 180 ريال")
print("4. عباية مناسبات فخمة - 550 ريال")
print("5. عباية ملونة - 300 ريال")

choice = input("\nاختاري رقم العباية: ")

abayas = {
    "1": ("عباية كلاسيك سوداء", 250),
    "2": ("عباية مطرزة", 350),
    "3": ("عباية عملية يومية", 180),
    "4": ("عباية مناسبات فخمة", 550),
    "5": ("عباية ملونة", 300),
}

abaya_name, abaya_price = abayas.get(choice, ("غير معروفة", 0))
print(f"\nاخترتي: {abaya_name} - {abaya_price} ريال")

print("\n📏 المقاسات:")
print("1. S")
print("2. M")
print("3. L")
print("4. XL")
print("5. XXL")

size_choice = input("اختاري المقاس: ")
sizes = {"1":"S","2":"M","3":"L","4":"XL","5":"XXL"}
size_name = sizes.get(size_choice, "M")

print("\n🎨 اللون:")
print("1. اسود")
print("2. كحلي")
print("3. بيج")
print("4. رمادي")
print("5. بني")

color_choice = input("اختاري اللون: ")
colors = {"1":"اسود","2":"كحلي","3":"بيج","4":"رمادي","5":"بني"}
color_name = colors.get(color_choice, "اسود")

qty = int(input("\nكم حبة تبي؟ "))
total = abaya_price * qty

print("\n🚚 الشحن:")
print("1. استلام من المتجر - مجاني")
print("2. توصيل داخل المدينة - 20 ريال")
print("3. توصيل خارج المدينة - 35 ريال")

ship_choice = input("اختاري الشحن: ")
ships = {"1": ("استلام من المتجر", 0), "2": ("توصيل داخل المدينة", 20), "3": ("توصيل خارج المدينة", 35)}
ship_name, ship_price = ships.get(ship_choice, ("استلام من المتجر", 0))

total = total + ship_price

print("\n--- بيانات الطلب ---")
name = input("اسمك: ")
phone = input("رقم جوالك: ")
address = input("عنوانك: ")

print("\n" + "=" * 40)
print("✅ تم استلام طلبك!")
print("=" * 40)
print(f"الاسم: {name}")
print(f"الجوال: {phone}")
print(f"العنوان: {address}")
print(f"العباية: {abaya_name}")
print(f"المقاس: {size_name}")
print(f"اللون: {color_name}")
print(f"العدد: {qty}")
print(f"الشحن: {ship_name} - {ship_price} ريال")
print(f"الاجمالي: {total} ريال")
print("\nشكرا لتسوقك من متجر ثناء 👗💖")
print("=" * 40)
