names = ["Cooper", "Michael", "Lee", "Jackie", "Caleb", "Jack", "Meghan"]
print(names)
del names[-1]
#or names.remove("")
print(names)
names.append("Kendall")
print(names)
for name in names:
    print(f"{name} is at my table")
names.sort(reverse=True)
print(names)
