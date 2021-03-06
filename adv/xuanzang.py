import adv.adv_test
from adv import *
from slot.a import *
import random
from slot.d import *

def module():
    return Xuanzang

class Xuanzang(Adv):
    a3 = ('cc',0.06,'hp70')
    conf = {}
    conf['slot.d'] = Dreadking_Rathalos()
    conf['slot.a'] = RR()+Jewels_of_the_Sun()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1, fsc
        `s2, cancel
        `fs, seq=4
        """

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = RR()+JotS()

    def s1_proc(this, e):
        if this.mod('def')!= 1:
            this.dmg_make('o_s1_boost',2.51*3*0.2*0.91)

    def s2_proc(this, e):
        Debuff('s2_defdown',0.1,20,0.7).on()





if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)

