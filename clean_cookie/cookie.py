import re, pyperclip

curl = """
curl 'https://bj.lianjia.com/ershoufang/c1111027381003/' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -b 'SECKEY_ABVK=vvR+KBylzs341tIeurubnC63QkuzoCT4z28NwsewLu8%3D; BMAP_SECKEY=HONR2i8zc6cMsGE7x3f74kMeK0YTAPBcnmTv7Gp0Ro5gleGJusap5tyBcSMGE-obRC3mH_rO9q1uFNX8o4vniGg3BXqwWSPWmYy9xWEYEDzh6xCMRN3c8ns-7UMcyFVGUsaVrpKtg-4nCa82C6KUWkAoFKVLIrd5G-_8ZybetM9-OhdOQsFf56b3SVbb_Ad9; lianjia_uuid=d929ba72-679f-4718-8933-4901ec4ff338; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219b0c307531211-0ff3e212874-26061b51-1821369-19b0c30753222cd%22%2C%22%24device_id%22%3A%2219b0c307531211-0ff3e212874-26061b51-1821369-19b0c30753222cd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; crosSdkDT2019DeviceId=-t4vocm--1vlpj0-oiejge3gamr0gu6-h87tudo0r; _ga=GA1.2.1772040068.1765436072; _gid=GA1.2.1003414472.1765436072; ftkrc_=58a7b8d4-022b-42ee-90c9-4bcdb435ca79; lfrc_=5a67ae8f-1cf4-4aa8-96c3-4b86f1901c30; select_city=110000; _jzqckmp=1; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1765436061,1765456879,1765514166,1765589539; HMACCOUNT=3F18AC6E8ACD690D; _qzjc=1; _jzqc=1; lianjia_ssid=15efd7ef-3765-42e3-a465-6d95b0200a53; login_ucid=2000000483328062; lianjia_token=2.0012f6530b47bc3ed9035b7a3a3e971a69; lianjia_token_secure=2.0012f6530b47bc3ed9035b7a3a3e971a69; security_ticket=IeBuEYZ747wMIWqW31xzPZqZBcTgouskFZujcwMRrieoCMOitoS7JbKlPWhUFj5WKuyueFBXA3wJGocJaaq12I4WzdmU5kN9CN0YolrktKv+adjpeAhGPsUGwhZekxIfSXirVYnl+z5bxPUArz7G25i+owzAMZ/cvnDvvADKKVU=; _qzja=1.1379139782.1765436061258.1765591577117.1765601152811.1765594983850.1765601152811.0.0.0.58.10; _qzjto=8.3.0; _jzqa=1.787719326959594200.1765436061.1765591577.1765601153.10; _jzqx=1.1765453672.1765601153.4.jzqsr=bj%2Elianjia%2Ecom|jzqct=/.jzqsr=clogin%2Elianjia%2Ecom|jzqct=/; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1765601153; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZjg1ZjllNDhjZjM2ZDNjZTE0ZjI1OTVjNmNhNjM0ZDFmNTZhNGJkMWY1OGQ5MDdmMmFjMjBkYWRhOWRhZTg1Njg0NGMyNzBjOGU1NTIwYTcyM2VlNjMwYmE5OWY1NDA1NTY1ZGVkOGY0MDI3MmI5MTlmZjY0YjA3YzVmNzEyMWQ2ZmE1MDljNjNjMWE5OTIwNmNkNWM4MmUwMzFjNGNjZTQ0NWQ3OGI4OTRlMTE0MDkyYjZiNzc1NGUwNWNlMzFmYzlkZDM2MWQxYmIyZmZiMjA4ZjdhNWFlMjc2NDVjMzViZDU5NzQ4NTlkM2MyOGE5ODk4YmY1ZDA1MzM2ZGQ0Y1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJmNzViYTBiZFwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvYzExMTEwMjczODEwMDMvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; _qzjb=1.1765601152811.1.0.0.0; _jzqb=1.1.10.1765601153.1; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _ga_KJTRWRHDL1=GS2.2.s1765601164$o7$g0$t1765601164$j60$l0$h0; _ga_QJN1VP0CMS=GS2.2.s1765601164$o7$g0$t1765601164$j60$l0$h0' \
  -H 'Referer: https://clogin.lianjia.com/' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
"""

cookie_match = re.search(r"-b\s+'([^']+)'", curl) or re.search(r"Cookie:\s*'([^']+)'", curl, re.S)
if cookie_match:
    cookie = cookie_match.group(1)
    cookie = re.sub(r"\s+", " ", cookie).strip()
    pyperclip.copy(cookie)
    print("✅ 已清洗并复制到剪贴板：\n", cookie)
else:
    print("❌ 没找到 Cookie，请确认 cURL 格式")