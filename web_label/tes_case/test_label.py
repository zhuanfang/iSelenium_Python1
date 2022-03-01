from web_label.api.label import Label


class TestLabel:
    def test_get(self):
        print(Label().test_get("4"))

    def test_create(self):
        print(Label().test_create("hub钱包","1","1","4"))

    def test_update(self):
        print(Label().test_update("4","修改后"))


    def test_delete(self):
        print(Label().test_delete("4"))