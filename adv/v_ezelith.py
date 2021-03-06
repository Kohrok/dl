import adv.adv_test
import adv
from adv import *
from module import energy
from slot.a import *
from slot.d import *

def module():
    return V_Ezelith

class V_Ezelith(Adv):
    a3 = ('bk',0.2)
    conf = {}
    conf['slot.a'] = EE()+DD()
    conf['slot.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, fsc and not this.s3_buff_on
        `s1, fsc
        `s2, fsc
        `fs, seq=2
    """
    conf['cond_afflict_res'] = 0

    def c_prerun(this):
        this.o_prerun()
        this.energy = energy.Energy(this, 
                self={'hit':1},
                team={}
                )

    def prerun(this):
        this.ehit = 0
        this.energy = energy.Energy(this, 
                self={},
                team={}
                )

    def init(this):
        if this.condition('never lose combos'):
            this.o_prerun = this.prerun
            this.prerun = this.c_prerun
            this.dmg_proc = this.c_dmg_proc

        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100

    def c_dmg_proc(this, name, amount):
        if this.hits // 30 > this.ehit:
            this.energy.add_energy('hit')
            this.ehit = this.hits // 30

    def s1_proc(this, e):
        this.afflics.burn('s1',110,0.883)
        this.hits += 8
            
    def s2_proc(this, e):
        this.hits += 1


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

