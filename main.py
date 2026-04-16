# 34. Do‘kon chegirmalari

class Discount:
    def __init__(self, name, price, discount_percent):
        self.name = name
        self.price = price                      # asl narx ($)
        self.discount = discount_percent        # chegirma foizi (%)

    def final_price(self):
        """Chegirmadan keyingi narx"""
        return self.price * (1 - self.discount / 100)

    def __str__(self):
        final = self.final_price()
        saved = self.price - final
        return f"{self.name:14} | {self.price:6.2f}$ | {self.discount:5}% | {final:7.2f}$ (tejaldi: {saved:.2f}$)"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class SaleDiscount(Discount):
    def __str__(self):
        final = self.final_price()
        saved = self.price - final
        return f"🔥 {self.name:12} → {self.price:6.2f}$ − {self.discount}% → {final:6.2f}$ (tejaldi {saved:.2f}$)"


class RegularDiscount(Discount):
    def __str__(self):
        final = self.final_price()
        saved = self.price - final
        return f"🛍️ {self.name:12} → {self.price:6.2f}$ − {self.discount}% → {final:6.2f}$ (tejaldi {saved:.2f}$)"


# --------------------------------------------------
# Chegirmali narxlarni chiqarish
# --------------------------------------------------

def show_discounted_prices(items):
    print("\n" + "═" * 75)
    print("          DO‘KON CHEGIRMALARI — NARX HISOBI          ".center(75))
    print("═" * 75)
    print("Mahsulot          Asl narx    Chegirma    Yakuniy narx     Tejaldi")
    print("─" * 75)

    total_original = 0
    total_final = 0
    total_saved = 0

    for item in items:
        print(item)
        orig = item.price
        fin = item.final_price()
        sav = orig - fin
        
        total_original += orig
        total_final += fin
        total_saved += sav

    print("─" * 75)
    print(f"Jami asl narx:                  {total_original:10.2f}$")
    print(f"Jami chegirmadan keyin:         {total_final:10.2f}$")
    print(f"Jami tejamkorlik:               {total_saved:10.2f}$")
    print("═" * 75 + "\n")


# Test ma'lumotlari
mahsulotlar = [
    SaleDiscount("Kiyim (yozgi)", 65.00, 35),
    RegularDiscount("Telefon qopqovi", 12.50, 15),
    SaleDiscount("Sovutgich", 480.00, 22),
    RegularDiscount("Naushniklar", 89.90, 10),
    SaleDiscount("Krossovka", 120.00, 40),
]

show_discounted_prices(mahsulotlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol mahsulotlaringiz:\n")
misol_mahsulotlar = [
    SaleDiscount("Kiyim", 50, 20),
    RegularDiscount("Elektronika", 100, 10),
]

show_discounted_prices(misol_mahsulotlar)
