#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Terminal 执行命令：  pytest
# 这是pytest测试用例执行的入口主函数
import pytest

# pytest.main(['-s', 'web自动化\\test_example1.py'])
# pytest.main(['-s', 'web自动化\\test_example1.py','--reruns','1'])
pytest.main(['-s', 'web自动化\\test_example3.py', '-n', '3'])
