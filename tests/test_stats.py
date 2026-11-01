from stats import FileStats


def test_empty_dir(tmp_path):
    s = FileStats(tmp_path)
    r = s.summary()

    assert r["files"] == 0
    assert r["total_size"] == 0
    assert r["by_ext"] == {}
    assert r["top_files"] == []

def test_normal_dir(tmp_path):
    (tmp_path / "a.py").write_text("print('a')", encoding="utf-8")     # 10 字节
    (tmp_path / "b.py").write_text("x = 1", encoding="utf-8")          # 5 字节
    (tmp_path / "note.md").write_text("hi", encoding="utf-8")          # 2 字节

    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "c.txt").write_text("abc", encoding="utf-8")                # 3 字节

    r = FileStats(tmp_path).summary()

    assert r["files"] == 4
    assert r["total_size"] == 10 + 5 + 2 + 3
    assert r["by_ext"] == {".py": 2, ".md": 1, ".txt": 1}

def test_top_n(tmp_path):
    (tmp_path / "big.bin").write_bytes(b"x" * 1000)
    (tmp_path / "mid.bin").write_bytes(b"x" * 500)
    (tmp_path / "small.bin").write_bytes(b"x" * 10)
    (tmp_path / "tiny.bin").write_bytes(b"x" * 1)

    r = FileStats(tmp_path).summary(top_n=2)

    assert len(r["top_files"]) == 2
    assert r["top_files"][0] == ("big.bin", 1000)
    assert r["top_files"][1] == ("mid.bin", 500)

    sizes = [size for _, size in r["top_files"]]
    assert sizes == sorted(sizes, reverse=True)
    # N 比文件数还大时，返回全部，不报错
    r_all = FileStats(tmp_path).summary(top_n=10)
    assert len(r_all["top_files"]) == 4