import matplotlib.pyplot as plt
f = open("DS4.txt","r")
i = 0
a = list()
b = list()
while True:
    c = list()
    c = f.readline().split(" ")
    if (c[0] == ""):
        break
    a.append(float(c[0]))
    b.append(float(c[1].replace("\n","")))
a2 = list()
b2 = list()
j = 0
while (j<len(a)):
    a2.append(960*(540-a[j])/(960-b[j]))
    b2.append(96000/(960-b[j]))
    j+=1
plt.figure(figsize=(960/100, 540/100))
plt.plot(a2,b2)
plt.xlabel("X1")
plt.ylabel("Z")
plt.savefig("cpr.png")
plt.show()
