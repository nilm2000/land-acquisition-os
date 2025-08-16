import redis.asyncio as redis

redis_client = None

async def init_redis():
    global redis_client
    redis_client = redis.from_url(
        "redis://localhost:6379",  # Update host/port if needed
        decode_responses=True
    )
    try:
        await redis_client.ping()
        print("✅ Connected to Redis")
    except Exception as e:
        print(f"❌ Redis connection failed: {e}")

def get_redis():
    return redis_client
