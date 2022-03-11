import requests
from lxml.html import etree
import json

def get_weather(city_url):
    response = requests.get(city_url)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    district_name = html.xpath("//div[@class='search_default']/em/text()")[0].split('，')[0]
    weather = html.xpath("//div//div//div//ul[@class='days clearfix']//li/text()")[3].strip()
    temperature = html.xpath("//div//div//div//ul[@class='days clearfix']//li/text()")[4].strip().split(' / ')
    wind = html.xpath("//div//div//div//ul[@class='days clearfix']//li//em/text()")[0].strip() + html.xpath("//div//div//div//ul[@class='days clearfix']//li//b/text()")[0].strip()
    air_quality = html.xpath("//div//div//div//ul[@class='days clearfix']//li//strong/text()")[0].strip()
    tip = html.xpath("//div//div//div[@class='wea_tips clearfix']//em/text()")[0].strip().replace('，', ',').replace('。', '.')
    return district_name, weather, temperature, wind, air_quality, tip


district_name, weather, temperature, wind, air_quality, tip = get_weather('http://tianqi.moji.com/weather/china/shanghai/changning-district')
res1 = f'{district_name}今日天气为{weather},气温在{temperature[0]}到{temperature[1]}之间,空气质量为{air_quality},风力为{wind},{tip}'
district_name, weather, temperature, wind, air_quality, tip = get_weather('http://tianqi.moji.com/weather/china/hubei/huangpi-district')
res2 = f'{district_name}今日天气为{weather},气温在{temperature[0]}到{temperature[1]}之间,空气质量为{air_quality},风力为{wind},{tip}'
print(res1)
print(res2)