# Yeh function hai add_vat jo price mein VAT add karta hai
# Iske do inputs hain: price (original price) aur vat_rate (VAT ki percentage)
def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100  # Price mein VAT add karke final amount return karta hai

# Ek list hai orders jisme alag-alag price rakhe hain
orders = [100, 150, 200]

# For loop chalake har price ke liye final amount calculate kar rahe hain aur print kar rahe hain
for price in orders:
    final_amount = add_vat(price, 10)  # 10% VAT lagata hai
    print(f"Original: {price}, Final with VAT: {final_amount}")
