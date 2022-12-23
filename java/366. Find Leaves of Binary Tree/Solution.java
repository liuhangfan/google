import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        while (root != null) {
            List<Integer> l = new ArrayList<>();
            root = trim(l, root);
            res.add(l);
        }
        return res;
    }

    public TreeNode trim(List<Integer> leaves, TreeNode root) {
        if (root == null) return null;
        if (root.left == null && root.right == null) {
            leaves.add(root.val);
            return null;
        }
        root.left = trim(leaves, root.left);
        root.right = trim(leaves, root.right);
        return root;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}