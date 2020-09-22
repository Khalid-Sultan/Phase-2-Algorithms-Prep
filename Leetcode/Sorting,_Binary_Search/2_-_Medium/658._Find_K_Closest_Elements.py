class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        while l<r:
            m = l + (r-l)//2
            if arr[m]>x:
                r = m
            elif arr[m]==x:
                l = m
                break
            else:
                l = m + 1

        res = []
        print(l)
        if arr[l]!=x and abs(arr[l] - x) > abs(arr[l-1] - x):
            l -= 1
        elif arr[l]!=x and abs(arr[l] - x) == abs(arr[l-1] - x):
            l -= 1
        print(l)
        left_ptr = l
        right_ptr = l + 1
        length = len(arr)
        while len(res)!=k:
            if left_ptr>-1 and right_ptr<length:
                if abs(arr[left_ptr] - x) <= abs(arr[right_ptr] - x):
                    res.append(arr[left_ptr])
                    left_ptr-=1
                else:
                    res.append(arr[right_ptr])
                    right_ptr+=1
            elif left_ptr>-1:
                res.append(arr[left_ptr])
                left_ptr-=1
            elif right_ptr<length:
                res.append(arr[right_ptr])
                right_ptr+=1
        res.sort()
        return res
            
            