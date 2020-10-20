import importlib.util
mName = "demo.test1"


module_file_path = r'/test_ex/test1.py'
module_spec = importlib.util.spec_from_file_location('test1', module_file_path)
print(module_spec)
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)

module.getName()
module.hello()
c = getattr(module, 'sum')
parms = {"x": 1, "y": 2}
c(**parms)

# print(c)
