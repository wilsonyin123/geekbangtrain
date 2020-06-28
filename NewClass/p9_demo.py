#1 实现缓存功能

from werkzeug.utils import cached_property

# werkzeug.utils.py p53

class Foo(object):
    @cached_property
    def cal(self):
        print('show me one time')
        var1 = 'cached info'
        return var1


bar = Foo()
bar.cal
bar.cal

######################
#ORM(flask.ext.sqlalchemy)
# 一个表记录一个节点的心跳更新
# 通过一个属性来获取节点是否可用，而不用写复杂的查询语句
class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    updated_at = db.Column(db.DateTime) # 节点最后心跳时间
    state = db.Column(db.Integer, nullable=False) # 节点是否禁用

    @property
    def is_active(self):
        if(datetime.datetime.now() - self.updated_at).secondes > 60 \
            and self.vm_state == 0:
            return False
        return True

#########################
# 限制传入的类型和范围（整数，且满足18-65）
class Age(object):
    def __init__(self, default_age = 18):
        self.age_range = range(18,66)
        self.default_age = default_age
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default_age)
    
    def __set__(self, isinstance, value):
        if value not in self.age_range:
            raise ValueError('must be in (18-65)')

        self.data[isinstance] = value

class Student(object):
    age = Age()

if __name__ == '__main__':
    s1 = Student()
    s1.age = 30
    s1.age = 100

############################
# 固定部分传递的参数
def xxyun_client(apitype, ak, sk, region='cn-beijing-3'):
    s = get_session()
    client = s.create_client(
        apitype,
        region,
        user_ssl = True,
        access_key =ak,
        secret_access_key =sk
    )
    return client


class XXYunBase(object):
    def __init__(self, account):
        self.account = account
        self.ak = self.account.ak
        self.sk = self.account.sk
    
    @property
    def eip_(self):
        return partial(xxyun_client, 'eip', self.ak, self.sk)
    
    @property
    def vpc_(self):
        return partial(xxyun_client, 'vpc', self.ak, self.sk)



##################
@property
def current_state(self):
    instance_state = {
       1: '运行',
       2: '离线',
       3: '下线',

   } 
    if(time_diff.seconds) >= 300:
       return instance_state[2]

    if self.state in range(10):
        return instance_state.get(self.state, '其他')
    return None 
