def course_serializer(course) -> dict:
    return {
        "id": str(express["_id"]),
        "weight":express["weight"],
        "price1":express["price1"],
        "region1":express["region1"],
        "price2":express["price2"],
        "region2":express["region2"]
    }

def expresses_serializer(expresses) -> list:
    return [express_serializer(express) for express in expresses]
