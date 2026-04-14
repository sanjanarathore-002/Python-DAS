amount=int(input("enter the amount:"));

if amount>=15000:
    gst=amount*(15/100);
    print(f"amount is {amount}");
    print(f"gst is {gst}");
    print(f"total amount is {amount+gst}");
else:
    print(f"without gst amount is {amount}");
    