import requests
import json
from pprint import pprint

cookies = {
    'gdpr': '0',
    '_ym_uid': '1669543799440878266',
    'skid': '8692579331669561538',
    'L': 'VmlpcU1lUF1reENGbWB/BmACQkINXlFRGj88RFUCOzYqLgVaJiA=.1669725631.15176.379867.b115ed9031b5dfacc3bac6f2fcf4ed74',
    'yandex_login': 'nesterkakoi-to',
    'font_loaded': 'YSv1',
    'yashr': '3988093341674047649',
    'yandexuid': '9224006771669487094',
    'yuidss': '9224006771669487094',
    'ymex': '1681751583.oyu.8892232741678864546#1994224547.yrts.1678864547#1993799102.yrtsi.1678439102',
    'i': 'vLYQDF4AAEPf5229jRVmZhqq7v24vWhdhso3seGxIv31nwbXOYTiie6JrAPrj7GM/HvXls8/plEBbCF9GROSUMPJeF4=',
    'my': 'YwA=',
    'Cookie_check': '1',
    '_ym_d': '1685396133',
    'device_id': 'aee9cf45bfd397fc46d86253707248fef6d3768c7',
    'fullscreen-saved-data': '%7B%22summer-vibe-lastcall-1%22%3A%7B%22compositeId%22%3A%22summer-vibe-lastcall-1%22%2C%22actualUntil%22%3A1724665748609%7D%7D',
    'is_gdpr': '1',
    'Session_id': '3:1695923119.5.0.1669725631475:hcSuVQ:29.1.2:1|874991658.-1.2.1:177978072|3:10276423.868777.p0_t5ZY4pHm4yGmUeGpF8pBUVhE',
    'sessar': '1.1182.CiACzuKFSi_JqAK6hDK-9EoYHJD1KrnKVwzs7q08WMTvww.BLCC50RI7j5Em07MOmCwO3f-3nqHWarFUwXjjBspQlk',
    'sessionid2': '3:1695923119.5.0.1669725631475:hcSuVQ:29.1.2:1|874991658.-1.2.1:177978072|3:10276423.868777.fakesign0000000000000000000',
    '_ym_isad': '2',
    'is_gdpr_b': 'CKDSYBCE0QEYASgB',
    'active-browser-timestamp': '1695928633850',
    'lastVisitedPage': '%7B%22874991658%22%3A%22%2Falbum%2F6323647%2Ftrack%2F46839137%22%7D',
    'ys': 'svt.2#udn.cDrQndC10YHRgtC10YAg0JrQsNC60L7QuS3QotC+#wprid.1695929332894870-16588264212021068090-balancer-l7leveler-kubr-yp-vla-65-BAL-8615#c_chck.3416877966',
    'bh': 'EjsiTm90LkEvQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjExNCIsICJPcGVyYSBHWCI7dj0iMTAwIhoFImFybSIiDyIxMDAuMC40ODE1LjgyIioCPzA6ByJtYWNPUyJCCCIxMy4yLjEiSgQiNjQiUlUiTm90LkEvQnJhbmQiO3Y9IjguMC4wLjAiLCJDaHJvbWl1bSI7dj0iMTE0LjAuNTczNS4xOTkiLCJPcGVyYSBHWCI7dj0iMTAwLjAuNDgxNS44MiIi',
    'yp': '2011289333.pcs.1#1703793849.pgp.5_27870957#1706186318.stltp.serp_bk-map_1_1674650318#1985085631.udn.cDrQndC10YHRgtC10YAg0JrQsNC60L7QuS3QotC+#1697963991.hdrc.0#1711443730.szm.2_200000047683716:1440x900:1272x727#1696103034.gpauto.43_572553:39_768329:14:1:1695930224',
    '_yasc': 'e79Qo5EF0KWylKhSAzRPye1xZa0U+KElkosDrY7rIqvsmf2lKYaHXi87o1yBT72mWQPPTB45GG0huSXWlI4yOMMRyqI=',
    'cycada': 'JuDyNVb/VwmjGxeiQOdV7178uTdpKhcxF/bUJZ5LEfA=',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'gdpr=0; _ym_uid=1669543799440878266; skid=8692579331669561538; L=VmlpcU1lUF1reENGbWB/BmACQkINXlFRGj88RFUCOzYqLgVaJiA=.1669725631.15176.379867.b115ed9031b5dfacc3bac6f2fcf4ed74; yandex_login=nesterkakoi-to; font_loaded=YSv1; yashr=3988093341674047649; yandexuid=9224006771669487094; yuidss=9224006771669487094; ymex=1681751583.oyu.8892232741678864546#1994224547.yrts.1678864547#1993799102.yrtsi.1678439102; i=vLYQDF4AAEPf5229jRVmZhqq7v24vWhdhso3seGxIv31nwbXOYTiie6JrAPrj7GM/HvXls8/plEBbCF9GROSUMPJeF4=; my=YwA=; Cookie_check=1; _ym_d=1685396133; device_id=aee9cf45bfd397fc46d86253707248fef6d3768c7; fullscreen-saved-data=%7B%22summer-vibe-lastcall-1%22%3A%7B%22compositeId%22%3A%22summer-vibe-lastcall-1%22%2C%22actualUntil%22%3A1724665748609%7D%7D; is_gdpr=1; Session_id=3:1695923119.5.0.1669725631475:hcSuVQ:29.1.2:1|874991658.-1.2.1:177978072|3:10276423.868777.p0_t5ZY4pHm4yGmUeGpF8pBUVhE; sessar=1.1182.CiACzuKFSi_JqAK6hDK-9EoYHJD1KrnKVwzs7q08WMTvww.BLCC50RI7j5Em07MOmCwO3f-3nqHWarFUwXjjBspQlk; sessionid2=3:1695923119.5.0.1669725631475:hcSuVQ:29.1.2:1|874991658.-1.2.1:177978072|3:10276423.868777.fakesign0000000000000000000; _ym_isad=2; is_gdpr_b=CKDSYBCE0QEYASgB; active-browser-timestamp=1695928633850; lastVisitedPage=%7B%22874991658%22%3A%22%2Falbum%2F6323647%2Ftrack%2F46839137%22%7D; ys=svt.2#udn.cDrQndC10YHRgtC10YAg0JrQsNC60L7QuS3QotC+#wprid.1695929332894870-16588264212021068090-balancer-l7leveler-kubr-yp-vla-65-BAL-8615#c_chck.3416877966; bh=EjsiTm90LkEvQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjExNCIsICJPcGVyYSBHWCI7dj0iMTAwIhoFImFybSIiDyIxMDAuMC40ODE1LjgyIioCPzA6ByJtYWNPUyJCCCIxMy4yLjEiSgQiNjQiUlUiTm90LkEvQnJhbmQiO3Y9IjguMC4wLjAiLCJDaHJvbWl1bSI7dj0iMTE0LjAuNTczNS4xOTkiLCJPcGVyYSBHWCI7dj0iMTAwLjAuNDgxNS44MiIi; yp=2011289333.pcs.1#1703793849.pgp.5_27870957#1706186318.stltp.serp_bk-map_1_1674650318#1985085631.udn.cDrQndC10YHRgtC10YAg0JrQsNC60L7QuS3QotC+#1697963991.hdrc.0#1711443730.szm.2_200000047683716:1440x900:1272x727#1696103034.gpauto.43_572553:39_768329:14:1:1695930224; _yasc=e79Qo5EF0KWylKhSAzRPye1xZa0U+KElkosDrY7rIqvsmf2lKYaHXi87o1yBT72mWQPPTB45GG0huSXWlI4yOMMRyqI=; cycada=JuDyNVb/VwmjGxeiQOdV7178uTdpKhcxF/bUJZ5LEfA=',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition Yx GX)',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.4346034032624708',
}

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, cookies=cookies, headers=headers).json()

with open('chart.json', 'w') as f:
    json.dump(response, f, indent=4, ensure_ascii=False)

with open('chart.json', 'r') as f:
    chart = json.load(f)

parsed_chart = dict()
for i, track_info in enumerate(chart['chartPositions']):
    track = track_info['track']
    parsed_chart[i + 1] = {tuple([artist['name'] for artist in track['artists']]): track['title']}

pprint(parsed_chart)