from pages.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontac(self):
        self.main.goto_addresslist().add_member().add_by_manual().input_name().input_number().click_save()