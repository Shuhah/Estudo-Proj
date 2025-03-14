#two_sum leetcode

class algoritmo: 
    def twosum(self, nums: list[int], result: int) :
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == result:
                    return [i, j]
                
        return []
    

# prova

def prova():
    prova = algoritmo()
    
    prova_1 = [1, 5, 9, 17, 55]
    result_1 = 72
    print(f"prova 1: {prova.twosum(prova_1, result_1)}") # [3, 4]

    prova_1 = [1, 5, 7, 69]
    result_1 = 3
    print(f"prova 1: {prova.twosum(prova_1, result_1)}") # sem retorno

    prova_1 = [7, 15, 9, 7]
    result_1 = 14
    print(f"prova 1: {prova.twosum(prova_1, result_1)}") # [0, 3]


prova()