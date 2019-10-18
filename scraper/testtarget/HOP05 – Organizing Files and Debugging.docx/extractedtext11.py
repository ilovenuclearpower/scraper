[/Module5] $ python debugging. py
Can I skip this task?
Traceback (most recent call last):
File "debugging.py", line 10, in <module>
function1()
File "debugging.py", line 3, in function1
function2()
File "debugging.py", line 7, in function2
raise Exception('It is not a good idea to skip tasks')
Exception: It is not a good idea to skip tasks