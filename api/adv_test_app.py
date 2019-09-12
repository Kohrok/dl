import io
import inspect
from os import listdir
from os.path import isfile, join
import re

from contextlib import redirect_stdout
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

from core.advbase import Adv as adventurer
import adv
import slot.a
import slot.d
import slot.w

app = Flask(__name__)
CORS(app)

# Helpers
def get_adv_module(adv_name):
    return getattr(
                __import__('adv.{}'.format(adv_name.lower())),
                adv_name.lower()
           ).module()
def is_amulet(obj):
    return (inspect.isclass(obj) and issubclass(obj, slot.a.Amulet)
            and obj.__module__ != 'slot.a'
            and obj.__module__ != 'slot')
def is_dragon(obj):
    return (inspect.isclass(obj) and issubclass(obj, slot.d.DragonBase)
            and obj.__module__ != 'slot.d'
            and obj.__module__ != 'slot')
def is_weapon(obj):
    return (inspect.isclass(obj) and issubclass(obj, slot.d.WeaponBase)
            and obj.__module__ != 'slot.w'
            and obj.__module__ != 'slot')
def list_members(module, predicate, element=None):
    members = inspect.getmembers(module, predicate)
    member_list = []
    for m in members:
        n, c = m
        if element is not None:
            if issubclass(c, slot.d.WeaponBase)  and element not in getattr(c, 'ele'):
                continue
        if c.__qualname__ not in member_list:
            member_list.append(c.__qualname__)
    return member_list

# API
@app.route('/adv_test', methods=['POST'])
def run_adv_test():
    params = request.get_json(silent=True)
    adv_name = params['adv'] if 'adv' in params else 'euden'
    wp1 = params['wp1'] if 'wp1' in params else None
    wp2 = params['wp2'] if 'wp2' in params else None
    dra = params['dra'] if 'dra' in params else None
    wep = params['wep'] if 'wep' in params else None
    ex  = params['ex'] if 'ex' in params else ''
    acl = params['acl'] if 'acl' in params else None
    afflict = max(abs(int(params['afflict'])), 100) if 'afflict' in params else None
    t   = abs(int(params['t']) if 't' in params else 180)

    log = -2

    import adv.adv_test
    adv.adv_test.set_ex(ex)
    adv_module = get_adv_module(adv_name)
    conf = {}
    def slot_injection(this):
        if wp1 is not None and wp2 is not None:
            this.conf['slots.a'] = getattr(slot.a, wp1)() + getattr(slot.a, wp2)()
        if dra is not None:
            this.conf['slots.d'] = getattr(slot.d, dra)()
        if wep is not None:
            this.conf['slots.w'] = getattr(slot.w, wep)()
        if afflict is not None:
            this.conf['cond_afflict_res'] = afflict
    def acl_injection(this):
        if acl is not None:
            this.conf['acl'] = acl
    adv_module.slot_backdoor = slot_injection
    adv_module.acl_backdoor = acl_injection

    f = io.StringIO()
    with redirect_stdout(f):
        adv.adv_test.test(adv_module, conf, verbose=log, duration=t)
    return f.getvalue()


ADV_DIR = 'D:\\Desktop\\degenlost\\dl\\adv'
@app.route('/adv_slotlist', methods=['GET'])
def get_adv_slotlist():
    result = {}
    result['adv'] = {}
    result['adv']['name'] = request.args.get('adv', default=None)
    adv_ele = None
    dragon_module = slot.d
    weap_module = slot.w
    if result['adv']['name'] is not None:
        adv_instance = get_adv_module(result['adv']['name'])()
        adv_ele = adv_instance.slots.c.ele.lower()
        result['adv']['ele'] = adv_ele
        dragon_module = getattr(slot.d, adv_ele)
        result['adv']['wt'] = adv_instance.slots.c.wt.lower()
        weap_module = getattr(slot.w, result['adv']['wt'])
        result['adv']['dragon'] = type(adv_instance.slots.d).__qualname__
        result['adv']['pref_wep'] = type(adv_instance.slots.w).__qualname__
        result['adv']['pref_wp'] = {
            'wp1': type(adv_instance.slots.a).__qualname__,
            'wp2': type(adv_instance.slots.a.a2).__qualname__
        }
        result['adv']['acl'] = adv_instance.conf.acl
        result['adv']['afflict_res'] = adv_instance.conf.cond_afflict_res
    # result['amulets'] = list_members(slot.a, is_amulet)
    result['dragons'] = list_members(dragon_module, is_dragon, element=adv_ele)
    result['weapons'] = list_members(weap_module, is_weapon, element=adv_ele)
    return jsonify(result)


ADV_DIR = 'D:\\Desktop\\degenlost\\dl\\adv'
@app.route('/adv_wp_list', methods=['GET'])
def get_adv_wp_list():
    result = {}
    result['adv'] = []
    result['amulets'] = list_members(slot.a, is_amulet)
    py_pattern = re.compile(r'([A-Za-z]*)\.py')
    for f in listdir(ADV_DIR):
        match = py_pattern.fullmatch(f)
        if isfile(join(ADV_DIR, f)) and match is not None:
            result['adv'].append(match.group(1))
    return jsonify(result)