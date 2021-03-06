import adv.adv_test
from adv import *
import adv
from slot.a import *

def module():
    return Naveed

class Naveed(adv.Adv):
    a1 = ('a',0.08,'hit15')
    a3 = ('prep','100%')
    conf = {}
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s2, this.s1level < 5
        `s1
        `fs, seq=3 and cancel
        """
    conf['slot.a'] = TSO()+Primal_Crisis()
            
    def prerun(this):
        this.s1level = 0

    def s1_proc(this, e):
        this.dmg_make("o_s1_boost",3*this.s1level*0.7,'s')

    def s2_proc(this, e):
        this.s1level += 1
        if this.s1level >= 5:
            this.s1level = 5
        adv.Event('defchain')()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

