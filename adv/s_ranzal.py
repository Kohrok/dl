import adv.adv_test
from adv import *
from slot.a import *

def module():
    return S_Ranzal

class S_Ranzal(Adv):
    comment = 'no bog'

    conf = {}
    conf['slot.a'] = RR() + FRH()
    conf['acl'] = """
        `s1, x=5
        `s2, x=5
        `s3, x=5
        """

    a1 = ('lo',0.4)
    a3 = ('primed_def', 0.08)

    def init(this):
        this.a3_iscding = 0
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc
       # if this.condition('bog resist 60'):
       #     this.afflics.bog.resist = 60
       # else:
       #     this.afflics.bog.resist = 100

    #def s1_proc(this, e):
    #    r = this.afflics.bog('s1',100)
    #    if r:
    #       Debuff('s1_bog',-0.5*r,8,1,'att','bog').on()


    def c_s2_proc(this, e):
        Teambuff('s2',0.10,15).on()

    def s2_proc(this, e):
        Selfbuff('s2',0.10,15).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)
