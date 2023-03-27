def course_serializer(course) -> dict:
    return {
        "id": str(express["_id"]),
        "weight":express["weight"],
        "price":express["price"],
        "region":express["region"]
    }

def expresses_serializer(expresses) -> list:
    return [express_serializer(express) for express in expresses]