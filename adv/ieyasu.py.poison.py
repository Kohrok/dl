import adv.adv_test
import ieyasu
from slot.a import *

def module():
    return Ieyasu

class Ieyasu(ieyasu.Ieyasu):
    comment = ''
    def prerun(this):
        super().prerun()
        from adv.adv_test import sim_duration
        if this.condition('always poisoned'):
            this.afflics.poison.resist=0
            this.afflics.poison.on('always_poisoned', 1, 0, duration=sim_duration, iv=sim_duration)

    def d_slots(this):
        this.slots.a = HoH()+The_Plaguebringer()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)
