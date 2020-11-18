import unittest
import copy
class TestList(unittest.TestCase):
    # We need to get the size of the list
    def test_list_size(self):
        l1 = [1,4,5]
        assert len(l1) > 0
    
    def test_list_size_empty(self):
        l1 = []
        self.assertEqual(l1,0)

    def test_list_size_null(self):
        l1 = []
        l1.append(None)
        assert len(l1) != 0

    # We need to clear the list
    def test_clean_list(self):
        l1 = ["foo","bar","mov","lea"]
        l1.clear()
        self.assertEqual(l1,0)

    def test_clear_after_dereferencing(self):
        l1=[1,2,3,4]
        l2 = l1
        l2.clear()
        self.assertEqual(l1,l2)

    def test_clear_after_copy(self):
        l1 = [0,1,1,2,3,5]
        l2 = copy.copy(l1)
        l2.clear()
        assert l2 != l1

    # We need to add Items
    def test_add_single(self):
        l1 = []
        l1.append("foo")
        assert len(l1) != 0
    
    def test_add_list(self):
        l1 = []
        l2 = [1,2,3]
        l1.append(l2)
        self.assertEqual(l1[0],l2)
    
    def test_add_diff_types(self):
        l1 = []
        l1.append(1)
        l1.append(2.5)
        l1.append("bar")
        self.assertEqual(l1,3)

    # We need to be able to check if an item exists
    def test_item_exists(self):
        l1 = ["Alice","Bob","Charles"]
        assert "Alice" in l1
    
    def test_sublist_exists(self):
        l1 = [[2,3,4],[6,7,8]]
        l2 = [2,3,4]
        assert l2 in l1
    
    def test_object_exists(self):
        import sys
        l1 = []
        l1.append(sys.stdin)
        self.assertEqual(l1[0],sys.stdin)

    # We need to get elements by index
    def test_get_index(self):
        l1 = [2,4,6]
        self.assertEqual(l1[0],2)

    def test_out_of_bound_index(self):
        l1 = [5,3,2]
        with self.assertRaises(IndexError):
            foo = l1[5]
    
    def test_index_range(self):
        l1 = [2,4,6,8]
        self.assertEqual(l1[0:2],[2,4])

    # We need to remove an item by index
    def remove_by_index(self):
        l1 = [1,2,3,4,5,9]
        l1.pop(5)
        self.assertTrue(9 not in l1)
    
    def remove_index_out_of_bound(self):
        l1 = [1,2,3]
        with self.assertRaises(IndexError):
            l1.pop(3)
    
    def remove_index_null(self):
        l1 = [1,2,3]
        with self.assertRaises(TypeError):
            l1.pop(None)