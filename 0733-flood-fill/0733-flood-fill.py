class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]

        if image[sr][sc] == color:
            return image

        image[sr][sc] = color

        if sr > 0 and image[sr - 1][sc] == target:
            self.floodFill(image,sr - 1,sc,color)
        if sr < len(image) - 1 and image[sr + 1][sc] == target:
            self.floodFill(image,sr + 1,sc,color)
        if sc > 0 and image[sr][sc - 1] == target:
            self.floodFill(image,sr,sc - 1,color)
        if sc < len(image[sr]) - 1 and image[sr][sc + 1] == target:
            self.floodFill(image,sr,sc + 1,color)
        
        return image