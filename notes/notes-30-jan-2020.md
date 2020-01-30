# 30-jan-2020


### 1 - Patching patch and mock

- just a thought experiment, to understand whether patching patch itself will cause issues.

```python
from unittest.mock import patch
from unittest.mock import Mock

with patch("__main__.patch") as patch_mock:



    with patch("__main__.patch") as patched_patch_mock:

        
        print(patched_patch_mock.mock_calls)

    print(patch_mock.mock_calls)


with patch("__main__.Mock") as mock_mock:

    x = Mock()
    print(x)


    print(mock_mock.mock_calls)
```

```bash
[]
[call('__main__.patch'), call().__enter__(), call().__exit__(None, None, None)]
<MagicMock name='Mock()' id='4530692392'>
[call(), call().__str__()]
```
