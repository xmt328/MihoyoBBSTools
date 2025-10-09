from test_nine.main import get_pic
from loghelper import log

import json


def captcha(gt: str, challenge: str):
    log.info("captcha gt:" + gt + " challenge:" + challenge)
    try:
        res = get_pic(gt, challenge)
        datas = json.loads(res.body).get("data", {})
        if datas.get("result") == "success":
            return adapt(challenge, datas.get("validate"))
    except Exception as e:
        log.exception(f"Error during captcha processing: {e}")
    return adapt(challenge, None)


def adapt(challenge: str, validate: str | None) -> dict[str, str] | None:
    # challenge不要直接用传入的，老格式也还支持，但是建议优先使用新格式
    # 失败返回None 成功返回{"challenge":challenge,"validate":validate}
    if validate is None:
        return None
    else:
        return {"challenge": challenge, "validate": validate}


def game_captcha(gt: str, challenge: str) -> dict:
    return captcha(gt, challenge)


def bbs_captcha(gt: str, challenge: str) -> dict:
    return captcha(gt, challenge)
