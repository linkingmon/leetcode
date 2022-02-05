class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            if flowerbed[0] == 1 and n == 0:
                return True
            return False
        if flowerbed[0] == 0 and len(flowerbed) > 1 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and len(flowerbed) > 1 and flowerbed[-2] == 0:
            n -= 1
            flowerbed[-1] = 1
        zero_cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if zero_cnt > 0:
                    n -= ceil( (zero_cnt - 2) / 2)
                if n <= 0:
                    return True
                zero_cnt = 0
            else:
                zero_cnt += 1
        print(n)
        return False