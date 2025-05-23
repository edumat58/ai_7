from main import model_summary

def test_model_summary():
    df = model_summary()
    assert len(df) == 5
    assert "prediction" in df.columns
