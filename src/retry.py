import time

def retry(func, max_attempts=5):
    attempt = 0
    while attempt < max_attempts:
        try:
            return func()
        except Exception as e:
            print(f"failed: {e}")  
            attempt += 1
            time.sleep(1)
    raise e  

