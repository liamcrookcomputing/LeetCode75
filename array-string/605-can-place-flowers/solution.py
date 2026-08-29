class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        totalCanPlace = 0
        flowerbedLength = len(flowerbed)
        for x in range(flowerbedLength):
            if x == 0:
                if flowerbedLength == 1 and flowerbed[x] == 0:
                    flowerbed[x] = 1
                    totalCanPlace += 1
                elif flowerbed[x] == 0 and flowerbed[x + 1] == 0:
                    flowerbed[x] = 1
                    totalCanPlace += 1
            elif x == flowerbedLength - 1:
                if flowerbed[x] == 0 and flowerbed[x - 1] == 0:
                    flowerbed[x] = 1
                    totalCanPlace += 1
            elif flowerbed[x] == 0 and flowerbed[x + 1] == 0 and flowerbed[x - 1] == 0:
                flowerbed[x] = 1
                totalCanPlace += 1
        
        return(totalCanPlace >= n)