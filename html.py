import requests


def get_html(url):
    # HTTP GET Request
    req = requests.get('https://media.daum.net/ranking/age/')

    # HTML 소스 가져오기
    html = req.text
    # HTTP Header 가져오기
    header = req.headers
    # HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok

    return html