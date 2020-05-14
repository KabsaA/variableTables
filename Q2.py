  def createTargetArray(nums, ind):
        lst = []
        for n, i in zip(nums, ind):
            lst.insert(i, n)
        return lst

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
