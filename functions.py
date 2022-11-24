import aiohttp

async def get_monitoring_stats(url):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            cpu_temp = round(res[0]["k10temp"][0][1], 1)
            ram_total = round((((res[2][0] / 1024) / 1024) / 1024), 1) # round to 2 decimal places
            ram_used = round((((res[2][3] / 1024) / 1024) / 1024), 1)
            ram_free = round((((res[2][1] / 1024) / 1024) / 1024), 1)
            load_1m = res[1][0]
            load_5m = res[1][1]
            load_15m = res[1][2]
            return [cpu_temp, ram_total, ram_used, ram_free, load_1m, load_5m, load_15m]