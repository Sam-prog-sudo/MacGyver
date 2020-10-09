axe_x = []
axe_y = []

for i in range(15):
    axe_x.append(0)
for j in range(15):
    axe_y.append(axe_x)

print(axe_x)
print(axe_y)

with open('test.txt', 'w+') as f:
    for item in axe_y:
        f.write(f"{item}\n")
