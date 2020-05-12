class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        i = post.index(pre[1])+1
        root.left = self.constructFromPrePost(pre[1:i+1], post[:i])
        root.right = self.constructFromPrePost(pre[i+1:], post[i:-1])
        return root