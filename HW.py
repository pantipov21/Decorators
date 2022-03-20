import datetime
import json

LOG_PATH = '/tmp/'


def decorator_log(path):
    def _decorator_log(old_function):
        def new_function(*args, **kwargs):
            res = old_function(*args, **kwargs)
            dt = datetime.datetime.now()
            res_dict = dict()
            res_dict["Date"] = str(dt.date())
            res_dict["Time"] = str(dt.hour)+':'+str(dt.minute)+':'+str(dt.second)
            res_dict["Function_name"] = old_function.__name__
            res_dict["args"] = args
            res_dict["kwargs"] = kwargs

            with open(f"{path+old_function.__name__}.log", "a") as f:
                json.dump(res_dict, f, ensure_ascii=False)
                f.write('\n')
            return res
        return new_function
    return _decorator_log

@decorator_log(LOG_PATH)
def mul(a, b):
    return a*b



print(mul(3,4))
