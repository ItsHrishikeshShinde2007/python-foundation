drivers = set()
number = int(input("Ok so how many F1 drievrs are your favirout: "))

for i in range(number):
    newd = str(input("Alright mate start listing your favriout drivers: "))
    drivers.add(newd)

print("Alright so the elements are:")
for d in drivers:
    print(d)
print("On retrying you will observe the elements will the printed in unordered output" \
"and the drivers name will nver repeat even on trying try it for yourself again if you want")