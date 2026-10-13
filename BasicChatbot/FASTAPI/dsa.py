def findLeaders(arr):
        """
        Finds all right-side leaders in the given array.
        :param arr: List[int] - The input array of integers.
        :return: List[int] - Leaders in the order they appear.
        """
        zeroindex=0
        for i in range(len(arr)):
                if arr[i]!=0:
                        arr[zeroindex],arr[i]=arr[i],arr[zeroindex]
                        zeroindex+=1
        return arr
arr=[2,4,7,0,2,5,0,2]
x=findLeaders(arr)
print(x)

