import pytest
print(__name__)

def computeGCp(seq):
    return (seq.count("C") + seq.count("G"))/len(seq)


def test_answer():
    print("running test answer")
    assert computeGCp("CCG") == 1
    
def test_answer2():
    assert computeGCp("AAATT") == 0

if __name__ == "__main__":
    pytest.main()