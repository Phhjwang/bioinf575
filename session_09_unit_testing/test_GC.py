import unittest


def computeGCp(seq):
    if seq == None:
        return None
    elif seq == "":
        return 0
    else:
        return 100 * (seq.count("C") + seq.count("G"))/len(seq)
        
        

class TestComputeGCp(unittest.TestCase):
    """
    Class to test the function computeGCp 
    Each method in this class will be a test case
    """
    
    def test_computeGCp(self, seq = "CCGG", p = 100):
        """
        General test case when we expect a certain percentage
        """
        self.assertEqual(computeGCp(seq), p, f"The result should be {p}")

    def test_computeGCp_None(self):
        """
        Exceptional case when we have None as the input sequence
        """
        self.assertEqual(computeGCp(None), None, "The result should be None")

if __name__ == "__main__":
    unittest.main()


