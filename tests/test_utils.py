import pytest
import pandas as pd
from python_utils.utils import add, mean

@pytest.mark.parametrize(['a', 'b', 'c'], [[1, 2, 3], [0, 5, 5], [6, 5, 11]])
def test_convert_to_idx_encodings(a, b, c):
    assert add(a, b) == c

@pytest.mark.parametrize(['data'], [[{'foo': [10, 20, 30, 40]}]])
def test_pandas(data):
    df = pd.DataFrame(data)
    assert mean(df, 'foo') == 25.0