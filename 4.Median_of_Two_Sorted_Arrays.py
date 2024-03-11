class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def _bins(x, fnctr, left, right):
            if left > right: return left
            if left > len(fnctr): return left
            mid = (right+left)//2
            if fnctr[mid] < x: return _bins(x, fnctr, mid+1, right)
            return _bins(x, fnctr, left, mid-1)
            
        def bins(x, fnctr):
            return _bins(x, fnctr, 0, len(fnctr)-1)

        def fmm(n1, n2, l, r):
            if n1 == [] or n2 == []:
                result = n1+n2
                return result[len(result)//2]
            mid = (l+r)//2
            if mid < 0:
                return None
            pos = bins(n1[mid], n2)
            print("mid: {} pos: {}".format(mid, pos))
            
            rl, rf = mid+pos, len(n1)-mid + len(n2)-pos-1
            print("rl: {}, rf: {}".format(rl, rf))
            
            if rl == rf:
                return n1[mid]

            if rl > rf:
                return fmm(n1, n2, l, mid-1)
                
            while pos+1 < len(n2) and n2[pos] == n1[mid]:
                pos = pos+1
                rl, rf = mid+pos, len(n1)-mid + len(n2)-pos-1
                print("rl: {}, rf: {}".format(rl, rf))
                
                if rl == rf:
                    return n1[mid]
            
            if l > r:
                return None
            
            if rl < rf:
                return fmm(n1, n2, mid+1, r)
            
            return None
        
        def try_median(nums1, nums2, left, right):
            mid = (left+right)//2
            if len(nums1) == 0:
                return None
            if len(nums2) == 0:
                return nums1[mid]
            place = binary_insert(nums1[mid], nums2)
            print("place {}, mid {}".format(place, mid))
            rleft, rright = mid+place, len(nums1)-mid+len(nums2)-place-1
            print(rleft, rright)
            if rleft == rright:
                return nums1[mid]
            if left > right:
                return None
            if rleft < rright:
                return try_median(nums1, nums2, mid+1, right)
            else:
                return try_median(nums1, nums2, left, mid-1)
        
        def get_median(nums1, nums2):

            print(nums1)
            print(nums2)

            fff = fmm(nums1, nums2, 0, len(nums1)-1)
            print(fff)
            if fff != None:
                return fff
            fff = fmm(nums2, nums1, 0, len(nums2)-1)
            print(fff)
            return fff



        size = len(nums1) + len(nums2)

        #nums1 always longer
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        if len(nums2) == 0:
            if len(nums1) % 2 == 1:
                return nums1[len(nums1)//2]
            asdf = nums1[(len(nums1)//2)] + nums1[(len(nums1)//2)-1]
            return asdf/2
        

        if size % 2 == 1:
            print("asdf")
            return get_median(nums1, nums2)
        else:
            #removing first number
            if nums1[0] < nums2[0]:
                a = get_median(nums1[1:], nums2)
            else:
                a = get_median(nums1, nums2[1:])     
    
            if nums1[-1] > nums2[-1]:
                b = get_median(nums1[:-1], nums2)
            else:
                b = get_median(nums1, nums2[:-1])     
            
            print(a, b)
    
            return (a+b)/2
