import os
from gitbook_worker.utils import download_remote_images

class DummyResponse:
    def __init__(self, content=b'x', status_code=200):
        self.content = content
        self.status_code = status_code
    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception("bad status")

def test_download_remote_images(tmp_path, monkeypatch):
    md = tmp_path / "doc.md"
    md.write_text("![](http://ex.com/a.png)")
    dest = tmp_path / "imgs"

    def fake_get(url, timeout=10):
        return DummyResponse(b"data")

    monkeypatch.setattr('gitbook_worker.utils.requests.get', fake_get)
    count = download_remote_images(str(md), str(dest))
    assert count == 1
    text = md.read_text()
    assert "ex.com" not in text
    assert (dest / "a.png").exists()
