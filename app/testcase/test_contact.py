import pytest
import yaml

from app.page.app import App

with open("../data/data_add.yaml","r",encoding = 'utf-8') as f:
    data_add = yaml.safe_load(f)

with open("../data/data_delete.yaml","r",encoding= "utf-8") as f:
    data_del = yaml.safe_load(f)

class TestContact():

    def setup_class(self):
        self.app = App()
    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.main = self.app.start().goto_main()
    def teardown(self):
        self.app.back(5)  # 返回5次，尽量回到首页，目的是为了用例间不受干扰

    @pytest.mark.parametrize('name,gender,phonenum',data_add)
    def test_addcontact(self,name,gender,phonenum):
        """
        添加联系人
        :return:
        """
        # name="冰墩墩1"
        # gender='女'
        # phonenum='13910000000'
        """
        业务流程 --清晰明确
        1. App(),调用方法atart() --启动app，goto_main() --进入主页
        2. 主页有2个方法，选择通讯录，选择添加联系人，选择手动添加，进入添加页
        3. 调用添加字段的方法
        """
        mypage_add = self.main.goto_contactListPage().add_contact().add_menual().\
            set_name(name).set_gender(gender).set_phonenum(phonenum).click_save()
        text= mypage_add.get_toast()
        # mypage.add_munual()
        assert '成功' in text
        self.app.back()

    @pytest.mark.parametrize('name', data_del)
    def test_deletecontact(self,name):
        mypage_dele = self.main.goto_contactListPage().search_contact().\
            send_contact(name).click_contact().delinfo().editinfo().delelement().delconfirm()







