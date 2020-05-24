
import json
import os
import pprint

import a00_get_prices as get
import a01_calc_stats as calc
import a02_do_report as rep

if __name__ == '__main__':
    get.main()
    calc.main()
    rep.main()



def dump_json(obj,fn):
    p = "/Users/imhiro/Desktop/conferences_2020/4_enterpy/enterpy_2/code/dumps"
    fp = os.path.join(p,os.path.basename(fn))
    with open(fp, mode="w", encoding="utf-8") as out:
        try:
            jtxt = json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=4)
            out.write(jtxt)
        except Exception as ex:
            out.write(str(ex))

def dump_pp(obj,fn):
    p = "/Users/imhiro/Desktop/conferences_2020/4_enterpy/enterpy_2/code/dumps"
    fp = os.path.join(p,os.path.basename(fn))
    with open(fp, mode="w", encoding="utf-8") as out:
        try:
            jtxt = pprint.pformat(obj,indent=4)
            out.write(jtxt)
        except Exception as ex:
            out.write(str(ex))



