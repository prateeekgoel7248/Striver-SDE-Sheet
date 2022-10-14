def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
        if len(arr)<=2:
            return arr[0]
        slow=arr[0]
        fast=arr[0]
        slow = arr[slow]
        fast = arr[arr[fast]]
        while slow!=fast:
            slow = arr[slow]
            fast = arr[arr[fast]]
        fast = arr[0]
        while slow!=fast:
            slow=arr[slow]
            fast=arr[fast]
        return slow