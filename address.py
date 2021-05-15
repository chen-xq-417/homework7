import requests

from homework7.base import Base


class Address(Base):

    def get_member_information(self, user_id):
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        # 继承了Base类中的self.s,获取的token给了self.s，所以params里不用再写'access_token' :self.get_token()
        params = {
            'userid': user_id
        }
        # 继承了Base类中的self.s，这里请求就可以不用requests，可以直接使用self.s
        # r = self.s.get(get_member_url, params=params)
        r = self.send("GET", get_member_url, params=params)
        return r.json()

    def update_member(self, user_id, name, mobile):
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
        }
        # r = self.s.post(url=update_member_url, json=data)
        r = self.send("POST", url=update_member_url, json=data)
        return r.json()

    def create_member(self, user_id, name, mobile, department):
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            'department': department
        }
        # r = self.s.post(url=create_member_url, json=data)
        r = self.send("POST", url=create_member_url, json=data)
        return r.json()

    def delete_members(self, userid):
        # url太长，可以把参数单独写出来，参数是指？之后的,把参数放在params
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {
            'userid': userid}
        # r = self.s.get(delete_url, params=params)
        r = self.send("GET", delete_url, params=params)
        return r.json()
