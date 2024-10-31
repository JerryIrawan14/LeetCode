class Solution:
    def twoSum(self, nums, target):
        map = {} #map kosong untuk menyimpan value:indeks
        for i,n in enumerate (nums):
            different = target - n
            if different in map:
                return [i,map[different]]
            map[n] = i
        return None