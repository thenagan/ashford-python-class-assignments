user_list = []
print("You will be able to enter 20 numbers, and numbers only please")
count = 0
for i in range(1, 21):
    print("Enter one of your numbers", i, ':')
    nums = int(input())
    user_list.append(nums)
    count += 1

print("Numbers in list are: ", count, "numbers", user_list)
print("Maximum number is: ", max(user_list))
print("Minimum number is: ", min(user_list))
print("Sum of numbers is: ", sum(user_list))
