from API_UI_TestFramework.pages.app import App
from API_UI_TestFramework.pages.member_invite import MemberInvite


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        invitepage = self.main.goto_addresslist().add_member().addmember_by_manual().input_name().input_number().click_save()
        assert "成功" in invitepage.get_toast()