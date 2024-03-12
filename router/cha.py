def findMedianSortedArrays(nums1, nums2):
    x = len(nums1)
    y = len(nums2)
    if x > y:
        nums1, nums2, x, y = nums2, nums1, y, x
    
    low = 0
    high = x
    while low <= high:
        px = (low + high) // 2
        py = (x + y + 1) // 2 - px
        
        maxLeftX = float('-inf') if px == 0 else nums1[px - 1]
        minRightX = float('inf') if px == x else nums1[px]
        
        maxLeftY = float('-inf') if py == 0 else nums2[py - 1]
        minRightY = float('inf') if py == y else nums2[py]
        
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = px - 1
        else:
            low = px + 1

nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))
