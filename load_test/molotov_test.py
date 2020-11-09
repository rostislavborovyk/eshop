from molotov import scenario

_API1 = "http://localhost:8000/products"
_API2 = "http://localhost:8000/users"


@scenario(weight=40)
async def scenario_one(session):
    async with session.get(_API1) as resp:
        # res = await resp.json()
        # assert res["result"] == "OK"
        assert resp.status == 200


@scenario(weight=60)
async def scenario_two(session):
    async with session.get(_API2) as resp:
        assert resp.status == 200
