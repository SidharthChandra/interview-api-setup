import time
import threading

# --------------------------
# TokenBucket: core logic
# --------------------------
class TokenBucket:
    def __init__(self, capacity, fill_rate):
        """
        :param capacity: Max tokens (burst size)
        :param fill_rate: Tokens added per second
        """
        self.capacity = capacity
        self.fill_rate = fill_rate
        self.tokens = capacity
        self.last_time = time.time()
        self.lock = threading.Lock()  # Thread safety

    def allow_request(self, tokens=1):
        """Return True if request is allowed, False otherwise."""
        with self.lock:
            now = time.time()
            time_passed = now - self.last_time

            # Refill tokens
            self.tokens = min(
                self.capacity,
                self.tokens + time_passed * self.fill_rate
            )
            self.last_time = now

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True

            return False


# --------------------------
# RateLimiter: manages buckets
# --------------------------
class RateLimiter:
    def __init__(self, capacity, fill_rate):
        """
        :param capacity: Max tokens per user/service
        :param fill_rate: Tokens/sec per user/service
        """
        self.capacity = capacity
        self.fill_rate = fill_rate
        self.buckets = {}             # user_id -> TokenBucket
        self.lock = threading.Lock()  # Protects buckets dict

    def get_bucket(self, user_id):
        """Get or create a token bucket for a user/service"""
        with self.lock:
            if user_id not in self.buckets:
                self.buckets[user_id] = TokenBucket(
                    self.capacity,
                    self.fill_rate
                )
            return self.buckets[user_id]

    def allow_request(self, user_id, tokens=1):
        """Check if request is allowed for a given user"""
        bucket = self.get_bucket(user_id)
        return bucket.allow_request(tokens)


# --------------------------
# Singleton instance
# --------------------------
rate_limiter = RateLimiter(capacity=5, fill_rate=1)
