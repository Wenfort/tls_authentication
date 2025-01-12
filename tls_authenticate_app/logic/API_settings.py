from urllib.parse import urlparse

API_ENDPOINT = 'https://slb.medv.ru/api/v2/'
API_HOST = urlparse(API_ENDPOINT).netloc

PRIVATE_KEY_DATA = b"""
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC76eyroh2mFLQO
TVxjD/ZKnWB7QexLgcjEyTfKfN2CDBSGtFgxPIsP/uzo2VDFc4WIitPqREzVFHr5
zSCroH7rHS6IrYmMH3lOTDwquMt57Y+D85szjLwgRfgT4ObpXY1DtkgbJUfeQIK4
0GRPXulGyH1sm0rW5bEWIeFAKBtmgFMbvygqRCp8WVajSTBTVMY4cUtKu5ihtCiq
mquHNf+nT2FKy+7MSgYOIOed1opBEhYX/8yFUpRlrRegI/5ibsy7S7gO5JznCGrA
RjTuxSdYEp6CrLUs7GZ8mqYWFCb+SICdhoJhIPUWANXCowNe2zpG3hSts+sYgwEz
1LhHczFFAgMBAAECggEAZcwosSYGp8UJccII7YVlKDCvZrZkutbZG3niJmiUWvIO
YJbsO+gPcZ/pWY74ia62RSzn9j3/3WLV5+Nu8mrktpu9bL+OBwG55me4JHCtkiTW
nWXnyvpPo7Aj3yj0DrHmaCskTshYcZdC+bmyzaid+QF9qMtLtLUDxPifnPDdPx4Q
J7O9S3AwUdYGfGzt6SWVaso+U18+ymdOUS2B4Y54DekmUYAHFgZ47pVi8cjcPWtC
oBnWXmzEncdpjDgIlRFVeU8w3nmZTkUxiuUtV87iXvekHI1azMDxZu3xUWZdWZn+
UL7RlA+RGumkrAFYQrVp4CoVyg3GajlZU4zutd3VlQKBgQD2aoXflAMWD9WFt32a
E6ED9LlU7ZGzHNhw/EhzNh+DisY4qiAERlXgZz9bJ3Rb7ljGp3WFo79uvDH7H5lI
DKBjHMgp39JouqFjnWKZzH+vz5XhvKuwCnx3jLoYsK8rLIu5sZvhkTyHMz1yCszK
JsO1nR1DZsWzyG7KghK4LCNRYwKBgQDDOOopOCMg4jvO4mlEZJTFRMfwult3+ika
s5CIuOs1kR3BGXn2sciEBHG6rJ+dlrsvTJHuY9shfYZHPgp8jjG6cFbZGQoHS5W/
QKn2V3LFK9+b/+b3JSLJD3M8qb8gO70jXwxSPQginhOJ+vt6pBpIa8ysEa7WlPMc
3dPWc8EHNwKBgAismUfUiwNEzWxmmCpLVJiyDbAaqM1YT5oyl05O8m8L/IxUGMpt
u2op2EYaLnNqAYAEtxNcP0njoBLJ+vhZUXALvFQVB/Ad2b6K9MSbOUd0FD+dB6Ir
zFPdBVQHLDNl3wlLYkRfe3T67cfM74aSNMN442XTAVSh0pyYVZZcH2YnAoGAUVw5
8r3LnhvLEzi26GMGwYQd08zG7CSc1tz5IpH2rNdy0BQ/CTokuChmAYeJ6hJ0pozB
0Nla7QU0XiKUGj7kqK/C8i2GSW4N1awsaVcepN/ZDFnFN0EJ00OWIjUYS2W6OLCX
IPsAlfTNbdbk0cLslTwgC6I+/H0NKP2mGJ0bWFcCgYEArpuAo9RSX9vkbdYkOi63
zcdIXjwxJw2ddKzp1EMRuEMU6oIFaXoz1MRVsys2JB/K1WGQO9afjIvgpoITPEe4
1SVdHIHamTjjcEJXlZ6rn1oiMkqchRNLyEiW5C1+c20uvV1NwoR9Tlr+ryGJ7UXW
QeZTD6mCdLOxGaN/FMvOUdQ=
-----END PRIVATE KEY-----
"""

CERTIFICATE_DATA = b"""
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number: 390570 (0x5f5aa)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=RU, ST=Ufa, L=Ufa, O=slb, OU=dimon, CN=etc/emailAddress=support@slb.medv.ru
        Validity
            Not Before: Aug 27 18:34:18 2020 GMT
            Not After : Aug 27 18:34:18 2021 GMT
        Subject: C=RU, ST=Moscow, L=Moscow, O=Test, CN=test@test.test
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:bb:e9:ec:ab:a2:1d:a6:14:b4:0e:4d:5c:63:0f:
                    f6:4a:9d:60:7b:41:ec:4b:81:c8:c4:c9:37:ca:7c:
                    dd:82:0c:14:86:b4:58:31:3c:8b:0f:fe:ec:e8:d9:
                    50:c5:73:85:88:8a:d3:ea:44:4c:d5:14:7a:f9:cd:
                    20:ab:a0:7e:eb:1d:2e:88:ad:89:8c:1f:79:4e:4c:
                    3c:2a:b8:cb:79:ed:8f:83:f3:9b:33:8c:bc:20:45:
                    f8:13:e0:e6:e9:5d:8d:43:b6:48:1b:25:47:de:40:
                    82:b8:d0:64:4f:5e:e9:46:c8:7d:6c:9b:4a:d6:e5:
                    b1:16:21:e1:40:28:1b:66:80:53:1b:bf:28:2a:44:
                    2a:7c:59:56:a3:49:30:53:54:c6:38:71:4b:4a:bb:
                    98:a1:b4:28:aa:9a:ab:87:35:ff:a7:4f:61:4a:cb:
                    ee:cc:4a:06:0e:20:e7:9d:d6:8a:41:12:16:17:ff:
                    cc:85:52:94:65:ad:17:a0:23:fe:62:6e:cc:bb:4b:
                    b8:0e:e4:9c:e7:08:6a:c0:46:34:ee:c5:27:58:12:
                    9e:82:ac:b5:2c:ec:66:7c:9a:a6:16:14:26:fe:48:
                    80:9d:86:82:61:20:f5:16:00:d5:c2:a3:03:5e:db:
                    3a:46:de:14:ad:b3:eb:18:83:01:33:d4:b8:47:73:
                    31:45
                Exponent: 65537 (0x10001)
    Signature Algorithm: sha256WithRSAEncryption
         26:8a:cd:e7:1b:2e:41:18:96:d2:9b:e7:be:8d:1b:a7:f5:7e:
         17:f9:2c:75:36:25:3f:0b:67:3f:99:6a:f1:0c:8b:d4:50:38:
         19:c7:06:0c:d1:8a:e2:c1:93:0c:bb:2d:45:1d:1f:f7:82:98:
         e6:e8:0c:76:7f:b9:d3:29:66:5a:ee:a3:d7:b1:19:b4:aa:95:
         44:99:23:9d:5f:c0:75:56:c7:19:d1:17:13:f1:cd:8e:57:15:
         ba:4e:56:99:d2:7f:98:36:7e:85:03:dc:e9:d6:0b:02:4e:2c:
         5f:76:3f:39:55:57:62:01:27:f7:c8:f9:38:08:ac:84:d2:16:
         19:1f:8a:ab:ce:bf:83:0d:1b:38:e7:62:88:5b:3c:05:28:4e:
         b9:ee:00:23:99:4b:5f:f2:91:1e:0a:99:99:6f:1f:99:a3:cc:
         41:e4:89:e8:17:84:69:9b:82:31:81:7c:62:6b:f4:58:52:9d:
         cc:2c:99:47:19:ae:e7:3f:36:74:91:55:a7:5d:e2:1a:0a:08:
         53:b6:88:1f:a0:84:61:77:70:17:6d:65:e0:84:78:e8:50:e3:
         10:fb:f0:8d:72:f0:ea:70:4e:f2:0c:51:93:16:52:2a:39:04:
         c6:44:e4:8f:77:c1:1f:35:58:fc:66:18:ec:cc:50:57:b3:8a:
         93:c1:fa:1f
-----BEGIN CERTIFICATE-----
MIIDRjCCAi4CAwX1qjANBgkqhkiG9w0BAQsFADB5MQswCQYDVQQGEwJSVTEMMAoG
A1UECAwDVWZhMQwwCgYDVQQHDANVZmExDDAKBgNVBAoMA3NsYjEOMAwGA1UECwwF
ZGltb24xDDAKBgNVBAMMA2V0YzEiMCAGCSqGSIb3DQEJARYTc3VwcG9ydEBzbGIu
bWVkdi5ydTAeFw0yMDA4MjcxODM0MThaFw0yMTA4MjcxODM0MThaMFcxCzAJBgNV
BAYTAlJVMQ8wDQYDVQQIDAZNb3Njb3cxDzANBgNVBAcMBk1vc2NvdzENMAsGA1UE
CgwEVGVzdDEXMBUGA1UEAwwOdGVzdEB0ZXN0LnRlc3QwggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQC76eyroh2mFLQOTVxjD/ZKnWB7QexLgcjEyTfKfN2C
DBSGtFgxPIsP/uzo2VDFc4WIitPqREzVFHr5zSCroH7rHS6IrYmMH3lOTDwquMt5
7Y+D85szjLwgRfgT4ObpXY1DtkgbJUfeQIK40GRPXulGyH1sm0rW5bEWIeFAKBtm
gFMbvygqRCp8WVajSTBTVMY4cUtKu5ihtCiqmquHNf+nT2FKy+7MSgYOIOed1opB
EhYX/8yFUpRlrRegI/5ibsy7S7gO5JznCGrARjTuxSdYEp6CrLUs7GZ8mqYWFCb+
SICdhoJhIPUWANXCowNe2zpG3hSts+sYgwEz1LhHczFFAgMBAAEwDQYJKoZIhvcN
AQELBQADggEBACaKzecbLkEYltKb576NG6f1fhf5LHU2JT8LZz+ZavEMi9RQOBnH
BgzRiuLBkwy7LUUdH/eCmOboDHZ/udMpZlruo9exGbSqlUSZI51fwHVWxxnRFxPx
zY5XFbpOVpnSf5g2foUD3OnWCwJOLF92PzlVV2IBJ/fI+TgIrITSFhkfiqvOv4MN
GzjnYohbPAUoTrnuACOZS1/ykR4KmZlvH5mjzEHkiegXhGmbgjGBfGJr9FhSncws
mUcZruc/NnSRVadd4hoKCFO2iB+ghGF3cBdtZeCEeOhQ4xD78I1y8OpwTvIMUZMW
Uio5BMZE5I93wR81WPxmGOzMUFezipPB+h8=
-----END CERTIFICATE-----
"""