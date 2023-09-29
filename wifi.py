import wifi_qrcode_generator.generator
# install the wifi_qrcode_generator
# pip install wifi_qrcode_generator

qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    # enter name of wifi where it says SSID
    # enter the wifi Password
    ssid='', hidden=False, authentication_type='WPA', password=''
)
qr_code.print_ascii()
qr_code.make_image().save('TT-WIFI.png')