import pytest

@pytest.fixture
def empty_stack():
    return Stack()

@pytest.fixture
def stack_with_element():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack
@pytest.fixture
def stack_with_limit():
    return Stack(5)