import requests


class TeliaSmsClient:

    def __init__(self, from_phone, password):
        self.country_number = '47'
        self.from_phone = from_phone
        self.password = password
        assert self.from_phone and self.password
        self.session = None

    def __enter__(self):

        self.session = self.login()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @property
    def msisdn(self):
        return self.country_number + self.from_phone

    def send_sms(self, to_phone, message, save=True):
        send_url = 'https://min-side.telia.no/re/api/mssa-proxy/no/rs/messaging/sms/send'
        payload = {
            "Message": message,
            "Contacts": to_phone,
            "Save": str(save).lower(),
        }
        response = requests.post(
            send_url,
            params={
                'msisdn': self.msisdn,
            },
            json=payload,
        )
        pass

    def login(self):
        session = requests.session()
        response = session.post(
            'https://min-side.telia.no/re/api/mssa-proxy/no/rs/auth/basic?goToMinbedrift=false',
            params={
                'msisdn': self.msisdn,
            },
            json={
                "Username": self.from_phone,
                "Password": self.password,
            },
        )
        return session
