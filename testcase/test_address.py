from homework7.address import Address
from homework7.base import Base


class TestAddress():
    def setup(self):
        self.address = Address()
        self.user_id = 'aaa24'
        self.name = 'aaa24'
        self.mobile = '18918290024'
        self.department = [1]

    def test_create_member(self):
        # 利用删除接口进行数据清理
        self.address.delete_members(self.user_id)
        r = self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        # 删除无用数据，做好清理工作，断言之前删除，是为防止断言未通过的情况下删除没有被调用
        # self.address.delete_members(self.user_id)
        # 断言，判断r中errmsg对应的值是否为created，如果没则显示network error
        # 使用get（），当数据不存在时，也不会报错，是返回空值，若是get[]，当数据不存在时，会抛异常
        assert r.get('errmsg', 'network error') == 'created'
        # 添加完成后，还可以去查询客户的name来判断是否添加成功
        r = self.address.get_member_information(self.user_id)
        assert r.get('name') == self.name

    # 获取成员信息
    def test_get_member_information(self):
        # 为防止获取不到成员信息，先创建成员
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.get_member_information(self.user_id)
        assert r.get('errmsg') == 'ok'
        assert r.get('name') == self.name

    def test_delete_member(self):
        # 防止删除之前该用户不存在，所有先创建用户，再调用删除接口
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.delete_members(self.user_id)
        assert r.get('errmsg') == 'deleted'
        # 用户已删除，再去获取用户信息，应该报错，错误码是60111
        r = self.address.get_member_information(self.user_id)
        assert r.get('errcode') == 60111

    def test_update_member(self):
        # 先删除再添加，是为保证用户是新添加的
        self.address.delete_members(self.user_id)
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        new_name = self.name + 'a'
        r = self.address.update_member(self.user_id, new_name, self.mobile)
        assert r.get('errmsg') == 'updated'
        r = self.address.get_member_information(self.user_id)
        assert r.get('name') == new_name
