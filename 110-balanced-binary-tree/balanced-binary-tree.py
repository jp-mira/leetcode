class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def dfs(root):
            #if the node is none, it's balanced
            if not root: return [True, 0]

            #check the left and right node
            left, right = dfs(root.left), dfs(root.right)

            #right and left are balanced and is less than or equal to 1
            balanced = (left[0] and right[0] and
            abs(left[1] - right[1]) <= 1)

            #return whether balanced and the height
            return [balanced, 1 + max(left[1],right[1])]

            #final answer, balanced or not
        return dfs(root)[0]

