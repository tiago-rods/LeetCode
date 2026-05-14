class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]  #memoria continua O(1)?
        nums.sort() #preciso procurar se sort cria memoria auxiliar em python, pois se utilizar merge, cria
        #exercicio pede que rode em O(n), porém se array for grande, o sort roda em O(nlogn)
        target = 1
        for n in nums:
            if n == target:
                target += 1
            elif n > target:
                return target
        return target
        # essa resposta não é O(n) e O(1) em memoria, porem funcionaz