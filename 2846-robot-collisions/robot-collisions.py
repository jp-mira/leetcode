from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Step 1: Sort robots by position
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        
        stack = []  # stores indices of robots moving right
        alive = [True] * len(robots)
        curr_health = [h for _, h, _, _ in robots]

        for i, (pos, health, direction, original_idx) in enumerate(robots):
            if direction == 'R':
                stack.append(i)
            else:  # direction == 'L'
                while stack and alive[i]:
                    j = stack[-1]  # last right-moving robot
                    
                    if not alive[j]:
                        stack.pop()
                        continue
                    
                    # Collision happens
                    if curr_health[j] > curr_health[i]:
                        curr_health[j] -= 1
                        alive[i] = False
                    elif curr_health[j] < curr_health[i]:
                        curr_health[i] -= 1
                        alive[j] = False
                        stack.pop()
                    else:
                        alive[i] = False
                        alive[j] = False
                        stack.pop()
        
        # Step 3: Collect survivors in original order
        result = []
        for i, (_, _, _, original_idx) in enumerate(robots):
            if alive[i]:
                result.append((original_idx, curr_health[i]))
        
        result.sort()  # restore original order
        return [health for _, health in result]