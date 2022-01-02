sand_ratio = int(input("Please enter the ratio of sand to beton : "))
cement_ratio = int(input("Please enter the ratio of cement to beton : "))
total_beton = int(input("Please enter the total beton : "))

sand2beton_ratio_str = f"sand to beton ratio : {sand_ratio} / {cement_ratio+sand_ratio}"
total_sand = sand_ratio / (cement_ratio+sand_ratio) * total_beton
total_cement = cement_ratio / (cement_ratio+sand_ratio) * total_beton
print(sand2beton_ratio_str)
print(f"total sand : {total_sand}")
print(f"total cement : {total_cement}")