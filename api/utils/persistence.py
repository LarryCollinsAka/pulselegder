import logging
from upstash_redis import Redis

logger = logging.getLogger(__name__)

# Automatically uses UPSTASH_REDIS_REST_URL and UPSTASH_REDIS_REST_TOKEN from your .env
redis = Redis.from_env()

async def save_config(data: dict):
    """Persists the wallet set and wallet metadata to Upstash."""
    try:
        # Upstash Redis handles the dictionary conversion
        redis.set("treasury_config", data)
        logger.info("Treasury configuration saved to Upstash Redis.")
    except Exception as e:
        logger.error(f"Failed to save to Redis: {e}")

async def load_config():
    """Retrieves the treasury configuration."""
    try:
        return redis.get("treasury_config")
    except Exception as e:
        logger.error(f"Failed to load from Redis: {e}")
        return None