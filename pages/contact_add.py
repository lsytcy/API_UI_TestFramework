class ContactAdd:
    def input_name(self):
        # 输入完成停留在当前页面，所以return self
        return self

    def input_number(self):
        return self

    def click_save(self):
        from API_UI_TestFramework.pages.app.member_invite import MemberInvite
        return MemberInvite()
