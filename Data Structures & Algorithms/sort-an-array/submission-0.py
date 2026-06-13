class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return sorted(nums)
        self.mergeSort(nums, 0, len(nums)-1)
        return nums
        
    def mergeSort(self, arr, l, r ):
        if l >= r:
            return
        m = (l+r) // 2
        self.mergeSort(arr,l, m)
        self.mergeSort(arr, m+1, r)
        self.merge(arr, l, m, r)

    def merge(self, a, l, m, r):
        temp = []
        i = l
        j = m+1

        while(i<=m and j<=r):
            if a[i] <= a[j]:
                temp.append(a[i])
                i += 1
            else:
                temp.append(a[j])
                j += 1
        while(i<=m):
            temp.append(a[i])
            i += 1
        while(j<=r):
            temp.append(a[j])
            j += 1
        
        for i in range(l,r+1):
            a[i] = temp[i-l]

        
        