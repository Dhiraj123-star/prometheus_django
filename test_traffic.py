
"""
Traffic generator for Django monitoring demo
"""
import requests
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor

BASE_URL = 'http://localhost:8000/app'

# All available endpoints
ENDPOINTS = [
    ('GET', '/'),                      # home_view
    ('GET', '/user/profile/'),         # user_profile  
    ('GET', '/search/?q=python'),      # search_api
    ('GET', '/search/?q=django'),      # search_api
    ('GET', '/search/?q=error'),       # search_api (triggers error)
    ('GET', '/compute/'),              # heavy_computation
    ('GET', '/upload/'),               # file_upload
    ('GET', '/analytics/'),            # analytics_data
    ('GET', '/health/'),               # health_check
    ('GET', '/loadtest/'),             # load_test
]

def make_request(method, endpoint):
    """Make a single request to an endpoint"""
    try:
        url = f"{BASE_URL}{endpoint}"
        response = requests.request(method, url, timeout=10)
        status = "✅" if response.status_code < 400 else "❌"
        print(f"{status} {method} {endpoint} -> {response.status_code} ({response.elapsed.total_seconds():.3f}s)")
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"❌ {method} {endpoint} -> Error: {e}")
        return 0

def generate_continuous_traffic(duration_minutes=5):
    """Generate continuous traffic for specified duration"""
    print(f"🚀 Starting continuous traffic generation for {duration_minutes} minutes...")
    print("📊 Watch your Grafana dashboard at http://localhost:3000")
    
    end_time = time.time() + (duration_minutes * 60)
    request_count = 0
    
    while time.time() < end_time:
        # Pick a random endpoint
        method, endpoint = random.choice(ENDPOINTS)
        
        # Make the request
        make_request(method, endpoint)
        request_count += 1
        
        # Random delay between requests
        time.sleep(random.uniform(0.1, 2.0))
        
        # Print progress every 50 requests
        if request_count % 50 == 0:
            remaining = int((end_time - time.time()) / 60)
            print(f"📈 {request_count} requests sent. {remaining} minutes remaining...")
    
    print(f"✅ Traffic generation completed! Total requests: {request_count}")

def generate_burst_traffic(num_requests=100, num_threads=5):
    """Generate burst traffic with multiple threads"""
    print(f"💥 Generating burst traffic: {num_requests} requests with {num_threads} threads...")
    
    def worker():
        for _ in range(num_requests // num_threads):
            method, endpoint = random.choice(ENDPOINTS)
            make_request(method, endpoint)
            time.sleep(random.uniform(0.05, 0.5))
    
    # Start threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print("✅ Burst traffic generation completed!")

def test_all_endpoints():
    """Test all endpoints once"""
    print("🧪 Testing all endpoints...")
    
    for method, endpoint in ENDPOINTS:
        make_request(method, endpoint)
        time.sleep(0.5)  # Small delay between tests
    
    print("✅ All endpoints tested!")

def generate_error_scenarios():
    """Generate various error scenarios"""
    print("🔥 Generating error scenarios...")
    
    error_endpoints = [
        ('GET', '/search/?q=error'),      # Triggers search error
        ('GET', '/compute/'),             # May timeout
        ('GET', '/upload/'),              # May be too large
        ('GET', '/user/profile/'),        # May have DB error
    ]
    
    for _ in range(20):
        method, endpoint = random.choice(error_endpoints)
        make_request(method, endpoint)
        time.sleep(random.uniform(0.2, 1.0))
    
    print("✅ Error scenario testing completed!")

if __name__ == "__main__":
    print("🎯 Django Monitoring Traffic Generator")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Test all endpoints once")
        print("2. Generate continuous traffic (5 minutes)")
        print("3. Generate burst traffic (100 requests)")
        print("4. Generate error scenarios")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            test_all_endpoints()
        elif choice == '2':
            generate_continuous_traffic(5)
        elif choice == '3':
            generate_burst_traffic(100, 5)
        elif choice == '4':
            generate_error_scenarios()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
        
        print("\n" + "=" * 50)