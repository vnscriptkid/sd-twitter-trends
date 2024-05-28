import redis

# Example data with scores (counts)
data = [
    ("2024-05-28T14:00:00", "2024-05-28T15:00:00", "apple", 150),
    ("2024-05-28T14:00:00", "2024-05-28T15:00:00", "joe biden", 75),
    ("2024-05-28T15:00:00", "2024-05-28T16:00:00", "apple", 200),
    ("2024-05-28T15:00:00", "2024-05-28T16:00:00", "microsoft", 100),
    ("2024-05-28T14:00:00", "2024-05-28T15:00:00", "google", 120),
    ("2024-05-28T14:00:00", "2024-05-28T15:00:00", "openai", 90),
    ("2024-05-28T15:00:00", "2024-05-28T16:00:00", "tesla", 180),
    ("2024-05-28T15:00:00", "2024-05-28T16:00:00", "amazon", 130)
]

# Redis connection
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Store data in Redis sorted sets with expiration
for start_time, end_time, entity, count in data:
    key = f"{start_time}_{end_time}"
    redis_client.zadd(key, {entity: count})
    # Set expiration to 1 hour (3600 seconds) from now
    redis_client.expire(key, 3600)

# Function to find the top N trending entities in a given time window using sorted sets
def find_top_n_trending_sorted_set(start_time, end_time, n=5):
    key = f"{start_time}_{end_time}"
    
    # Get the top N entities with the highest counts
    trending_entities = redis_client.zrevrange(key, 0, n-1, withscores=True)
    
    # Convert results to a list of tuples (entity, count)
    trending_list = [(entity.decode('utf-8'), int(count)) for entity, count in trending_entities]
    
    return trending_list

# Define time window
start_time = "2024-05-28T14:00:00"
end_time = "2024-05-28T15:00:00"

# Find the top 2 trending entities in the specified time window
top_5_trending = find_top_n_trending_sorted_set(start_time, end_time, n=2)

print("Top 2 Trending Entities:")
for entity, count in top_5_trending:
    print(f"Entity: {entity}, Count: {count}")

# Entity: apple, Count: 150
# Entity: google, Count: 120