'''
    Time complexity: O(N*logN)
    Space complexity: O(N)
    
    Where 'N' is the number of points.
'''

from typing import List
from collections import defaultdict

def count(pointX: List[int], pointY: List[int], n: int) -> int:
    
    # Create maps.
    mpX = defaultdict(int)
    mpY = defaultdict(int)
    mpXY = defaultdict(int)
    
    # To store count.
    countX = 0
    countY = 0
    countXY = 0
    
    for i in range(n):
        
        # Check if X-coordinate is already present.   
        if pointX[i] in mpX:
            
            # Update countX.
            countX += mpX[pointX[i]]
        
        # Update X-coordinate in mapX.
        mpX[pointX[i]] += 1
        
        # Check if Y-coordinate is already present.   
        if pointY[i] in mpY:
            
            # Update countY.
            countY += mpY[pointY[i]]
        
        # Update Y-coordinate in mapY.
        mpY[pointY[i]] += 1
        
        temp = [pointX[i], pointY[i]]
        temp = tuple(temp)

        # Check if a point is already present. 
        if temp in mpXY:
            
            # Update countXY.
            countXY += mpXY[temp]
        
        # Update point in mapXY.
        mpXY[temp] += 1
    
    return countX + countY - 2 * countXY
