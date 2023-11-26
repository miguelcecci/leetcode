class Solution:

    def is_inbounds(self, sr, sc, image):
        if 0 <= sr < len(image) and 0 <= sc < len(image[0]):
            return True
        return False

    def recursive_fill(self, image, sr, sc, color, initial_color):

        #check if position is valid
        if not self.is_inbounds(sr, sc, image):
            return 0

        #get the current color
        current_color = image[sr][sc]

        # paint and visit neighbors if the current color match the inital color
        if initial_color == current_color:
            image[sr][sc] = color

            #visit neighbors
            self.recursive_fill(image, sr-1, sc, color, initial_color)
            self.recursive_fill(image, sr+1, sc, color, initial_color)
            self.recursive_fill(image, sr, sc-1, color, initial_color)
            self.recursive_fill(image, sr, sc+1, color, initial_color)
            
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]

        if color == initial_color:
            return image

        self.recursive_fill(image, sr, sc, color, initial_color)
        
        return image
