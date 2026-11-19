from pathlib import Path

import pyreadstat
import pytest

DATA = Path(__file__).resolve().parents[1] / "data" / "dataset_1A.sav"


def load():
    return pyreadstat.read_sav(DATA)


def test_shape_and_no_missing():
    df, _ = load()
    assert df.shape == (5, 5)
    assert df.isna().sum().sum() == 0


def test_summary_statistics():
    df, _ = load()
    assert df.Age.mean() == pytest.approx(28.0)
    assert df.Grade_Statistics.mean() == pytest.approx(3.6)


def test_value_labels():
    _, meta = load()
    assert meta.variable_value_labels["School_year"] == {
        2.0: "sophomore",
        3.0: "junior",
    }
    assert meta.variable_value_labels["Grade_Statistics"][5.0] == "A"
