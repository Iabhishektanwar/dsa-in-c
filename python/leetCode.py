def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        L = nums[:mid]
        R = nums[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1


A = [7, 5, 8, -8, 3]
mergeSort(A)
print(A)