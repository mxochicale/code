# content of conftest.py
import pytest

def pytest_collect_file(parent, file_path):
    print(f"\n")
    print(f'PRINT pytest_collect_file > parent: {parent}')
    print(f'PRINT pytest_collect_fiel > file_path: {file_path}')
    if file_path.suffix == ".yaml" and file_path.name.startswith("test"):
        return YamlFile.from_parent(parent, path=file_path)


class YamlFile(pytest.File):
    def collect(self):
        # We need a yaml parser, e.g. PyYAML.
        import yaml

        print(f'PRINT YamlFile > pytest.File: {pytest.File}')
        print(f'PRINT YamlFile > self: {self}')
        
        raw = yaml.safe_load(self.path.open())
        print(f'PRINT YamlFile > raw: {raw}')
        for name, spec in sorted(raw.items()):
            print(f'  PRINT YamlFile > name: {name}')
            print(f'  PRINT YamlFile > spec: {spec}')
            yield YamlItem.from_parent(self, name=name, spec=spec)


class YamlItem(pytest.Item):
    def __init__(self, *, spec, **kwargs):
        super().__init__(**kwargs)
        self.spec = spec
        #print(f'PRINT2 YamlItem > self.spec: {self.spec}')

    def runtest(self):
        for name, value in sorted(self.spec.items()):
            # Some custom test execution (dumb example follows).
            print(f"\n")
            print(f'PRINT2 YamlItem::runtest() > name: {name}')
            print(f'PRINT2 YamlItem::runtest() > value: {value}')
            if name != value:
                raise YamlException(self, name, value)

    def repr_failure(self, excinfo):
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, YamlException):
            return "\n".join(
                [
                    "usecase execution failed",
                    "   spec failed: {1!r}: {2!r}".format(*excinfo.value.args),
                    "   no further details known at this point.",
                ]
            )

    def reportinfo(self):
        return self.path, 0, f"usecase: {self.name}"


class YamlException(Exception):
    """Custom exception for error reporting."""
