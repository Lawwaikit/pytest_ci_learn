import pytest


@pytest.fixture(scope="session", autouse=False)
def log_request():
    print("session start")
    yield
    print("session end")


@pytest.fixture(scope="module", autouse=False)
def log_request2():
    print("module start")
    yield
    print("module end")


@pytest.fixture(scope="class", autouse=False)
def log_request3():
    print("class start")
    yield
    print("class end")


@pytest.fixture(scope="function", autouse=False)
def log_request4():
    print("function start")
    yield
    print("function end")


# conftest.py
def pytest_configure(config):
    """测试配置初始化"""
    print("hook pytest_configure...")


def pytest_sessionstart(session):
    """测试会话开始前执行"""
    print("hook pytest_sessionstart...")


def pytest_sessionfinish(session, exitstatus):
    """测试会话结束后执行"""
    print("\nhook pytest_sessionfinish...")


def pytest_generate_tests(metafunc):
    """根据条件动态生成测试用例"""
    print("hook pytest_generate_tests...")


def pytest_collection_modifyitems(config, items):
    """修改收集到的测试项"""
    print("hook pytest_collection_modifyitems...")


def pytest_runtest_setup(item):
    """单个测试执行前的设置"""
    print("\nhook pytest_runtest_setup...")


def pytest_runtest_teardown(item, nextitem):
    """单个测试执行后的清理"""
    print("\nhook pytest_runtest_teardown...")
