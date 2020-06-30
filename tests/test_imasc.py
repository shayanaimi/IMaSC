import importlib.util

spec = importlib.util.spec_from_file_location(
    "get_article_text", "/mnt/c/Users/pavle/Documents/Github/medvidov/IMaSC/parser.py"
)
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(
    foo,
    "data/microwave_limb_sounder/mls_pubs.jsonl",
    "data/microwave_limb_sounder/article_text.jsonl"
)
foo.MyClass()


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
