import adv_test
import adv

def module():
    return Eleonora

class Eleonora(adv.Adv):
    def condition(this):
        this.init = this.c_init
        return 'afflic'

    def init(this):
        this.charge("prep",'50%')

    def c_init(this):
        this.charge("prep",'50%')
        this.dmg_make("o_poison",2.65)
        this.dmg_make("o_poison",2.65)
        this.dmg_make("o_poison",2.65)


if __name__ == '__main__':
    module().comment = 'poison by s1 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    adv_test.test(module(), conf, verbose=0)
    module().comment += ' & spawn c1+fs'
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        `fs, seq=1
        """
    adv_test.test(module(), conf, verbose=0)
