import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

# 修改导入语句，增加了 subtract
from calculator import add, divide, subtract

def test_add():
    assert add(1, 2) == 3

def test_divide():
    assert divide(6, 2) == 3

def test_divide_by_zero():
    try:
        divide(1, 0)
        assert False
    except ValueError:
        assert True

# 新增的测试函数
def test_subtract():
    assert subtract(5, 3) == 2