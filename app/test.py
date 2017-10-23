async def get_content():
    return 'content'


async def fetch():
    r = await get_content()
    return r

get_content()
