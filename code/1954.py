class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # 2n(n+1)(2n+1) has diameter 8n
        min_idx = floor(((neededApples * 2)**(1/3)) / 2)
        max_idx = ceil((neededApples / 4)**(1/3))
        for i in range(min_idx,max_idx+1):
            if 2*i*(i+1)*(2*i+1) >= neededApples:
                return 8*i