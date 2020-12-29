import os
import fire
import uvicorn
from telia_sms.telia_sms import TeliaSmsClient


class TeliaSmsCli:

    def send_sms(self, to_phone: str, message: str, from_phone: str = None, password: str = None):
        from_phone = os.environ.get('TELIA_PHONE') if from_phone is None else str(from_phone)
        password = os.environ.get('TELIA_PASSWORD') if password is None else str(password)
        with TeliaSmsClient(from_phone, password) as client:
            client.send_sms(to_phone, message)

    def run_server(self):
        from telia_sms.app import app
        uvicorn.run("telia_sms.app:app", reload=True)
        # app.run(host='0.0.0.0', use_reloader=False, threaded=True)


if __name__ == '__main__':
    fire.Fire(TeliaSmsCli)

    # import uvicorn
    # print(uvicorn.__version__)