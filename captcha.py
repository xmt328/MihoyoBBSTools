from test_nine.main import get_pic
from loghelper import log

import json


def captcha(gt: str, challenge: str):
    log.info("captcha gt:" + gt + " challenge:" + challenge)
    try:
        res = get_pic(gt, challenge)
        datas = json.loads(res.body).get("data", {})
        if datas.get("result") == "success":
            return datas.get("validate")
    except Exception as e:
        log.exception(f"Error during captcha processing: {e}")
    return None  # 失败时返回 None


def game_captcha(gt: str, challenge: str):
    return captcha(gt, challenge)


def bbs_captcha(gt: str, challenge: str):
    return captcha(gt, challenge)
