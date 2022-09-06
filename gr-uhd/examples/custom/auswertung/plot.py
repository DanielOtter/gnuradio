import numpy as np
import matplotlib.pyplot as plt
import math

# Number of samples to be plotted
a = 10000000

# Max. error
b = 150     # sinus
# b = 170   # noise

# Decimal adjustment
c = 1000000 # sinus
# c = 100   # noise


# 2 Empty lists with b entries
lst = [0] * b
cnt = [0] * b

# Fill lst with 0 to b-1
begin = 0
for i in range(b):
    lst[i] = begin
    print(begin)
    begin += 1


# Read cpu and fpga data
cpu = np.fromfile(open("cpuout"), dtype=np.complex64)
fpga = np.fromfile(open("fpgaout"), dtype=np.complex64)

print(len(cpu))
print(len(fpga))


# Calculate sum(abs(cpu - fpga)) / number of samples
dif = cpu[0:a] - fpga[0:a]
mag = abs(dif)
s = sum(mag)
print(sum(mag)/a)


# Plot Samples x Dif
plt.plot(mag[0:a])
plt.xlabel("Sample")
plt.ylabel("Difference between CPU and FPGA FIR filter")
plt.savefig('sinus_difference.png')
# plt.show()

for i in mag:
    ind = lst.index(round(i*c))
    cnt[ind] += 1


# Write Dif x Occurences to file
f = open("sinus_occurences", "w")
f.write("Difference in e-6, Number of occurences")
for i in range(b):
    f.write(str(lst[i]))
    f.write(", ")
    f.write(str(cnt[i]))
    f.write("\n")
f.close()


# Plot Dif x Occurences
plt.plot(lst, cnt)
plt.xlabel("Difference between CPU and FPGA FIR filter in e-6")
plt.ylabel("Number of occurences")
plt.savefig('sinus_occurences.png')
# plt.show()