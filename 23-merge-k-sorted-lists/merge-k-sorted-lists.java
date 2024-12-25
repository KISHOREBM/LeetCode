class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // Check if the input array is null or empty
        if (lists == null || lists.length == 0) {
            return null;
        }
        boolean allNull = true;
        for (ListNode node : lists) {
            if (node != null) {
                allNull = false;
                break;
            }
        }
        if (allNull) {
            return null;
        }

        ListNode ret = new ListNode();
        ListNode cur = ret;
        while (true) {
            int minIndex = -1;
            int minValue = Integer.MAX_VALUE;
            for (int i = 0; i < lists.length; i++) {
                if (lists[i] != null && lists[i].val < minValue) {
                    minIndex = i;
                    minValue = lists[i].val;
                }
            }
            if (minIndex == -1) {
                break;
            }

            cur.next = lists[minIndex];
            cur = cur.next;

            // Move to the next node in the list that had the smallest value
            lists[minIndex] = lists[minIndex].next;
        }

        return ret.next;
    }
}
