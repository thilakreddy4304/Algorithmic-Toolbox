n = int(input())
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
arr1.sort()
arr2.sort()
sol = sum([arr1[i]*arr2[i] for i in range(n)])
print(sol)
