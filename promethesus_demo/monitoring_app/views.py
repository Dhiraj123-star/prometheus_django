
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from prometheus_client import Counter, Histogram, Gauge
import time
import random
import json

# Custom Prometheus metrics
CUSTOM_REQUEST_COUNT = Counter('custom_requests_total', 'Custom request counter', ['view_name', 'method'])
CUSTOM_RESPONSE_TIME = Histogram('custom_response_time_seconds', 'Custom response time', ['view_name'])
ACTIVE_USERS = Gauge('active_users_count', 'Number of active users')
API_ERRORS = Counter('api_errors_total', 'API errors counter', ['view_name', 'error_type'])

def home_view(request):
    """Main dashboard view"""
    start_time = time.time()
    
    # Track custom metrics
    CUSTOM_REQUEST_COUNT.labels(view_name='home', method=request.method).inc()
    
    # Simulate some processing
    time.sleep(random.uniform(0.05, 0.2))
    
    # Track response time
    CUSTOM_RESPONSE_TIME.labels(view_name='home').observe(time.time() - start_time)
    
    # Update active users (simulate)
    ACTIVE_USERS.set(random.randint(10, 50))
    
    context = {
        'message': 'Welcome to Django Monitoring',
        'active_users': random.randint(10, 50),
        'timestamp': time.time()
    }
    
    return JsonResponse(context)

@never_cache
def user_profile(request):
    """User profile endpoint"""
    start_time = time.time()
    
    CUSTOM_REQUEST_COUNT.labels(view_name='user_profile', method=request.method).inc()
    
    # Simulate database lookup time
    time.sleep(random.uniform(0.1, 0.4))
    
    # Simulate occasional errors
    if random.random() < 0.1:  # 10% error rate
        API_ERRORS.labels(view_name='user_profile', error_type='database_error').inc()
        return JsonResponse({'error': 'Database connection failed'}, status=500)
    
    CUSTOM_RESPONSE_TIME.labels(view_name='user_profile').observe(time.time() - start_time)
    
    return JsonResponse({
        'user_id': random.randint(1, 1000),
        'username': f'user_{random.randint(1, 100)}',
        'profile_loaded': True,
        'load_time': time.time() - start_time
    })

@never_cache
def search_api(request):
    """Search API endpoint"""
    start_time = time.time()
    
    CUSTOM_REQUEST_COUNT.labels(view_name='search_api', method=request.method).inc()
    
    # Get search query
    query = request.GET.get('q', 'default')
    
    # Simulate search processing time based on query length
    search_time = len(query) * 0.02 + random.uniform(0.05, 0.3)
    time.sleep(search_time)
    
    # Simulate search errors for certain queries
    if 'error' in query.lower():
        API_ERRORS.labels(view_name='search_api', error_type='invalid_query').inc()
        return JsonResponse({'error': 'Invalid search query'}, status=400)
    
    CUSTOM_RESPONSE_TIME.labels(view_name='search_api').observe(time.time() - start_time)
    
    # Generate fake search results
    results = [
        {'id': i, 'title': f'Result {i} for "{query}"', 'score': random.uniform(0.1, 1.0)}
        for i in range(random.randint(0, 10))
    ]
    
    return JsonResponse({
        'query': query,
        'results': results,
        'total_results': len(results),
        'search_time': time.time() - start_time
    })

@never_cache
def heavy_computation(request):
    """CPU intensive endpoint"""
    start_time = time.time()
    
    CUSTOM_REQUEST_COUNT.labels(view_name='heavy_computation', method=request.method).inc()
    
    # Simulate heavy computation
    computation_time = random.uniform(0.5, 2.0)
    time.sleep(computation_time)
    
    # Simulate occasional timeouts
    if computation_time > 1.5:
        API_ERRORS.labels(view_name='heavy_computation', error_type='timeout').inc()
        return JsonResponse({'error': 'Computation timed out'}, status=408)
    
    CUSTOM_RESPONSE_TIME.labels(view_name='heavy_computation').observe(time.time() - start_time)
    
    return JsonResponse({
        'result': random.randint(1000, 9999),
        'computation_time': time.time() - start_time,
        'status': 'completed'
    })

@never_cache
def file_upload(request):
    """File upload simulation"""
    start_time = time.time()
    
    CUSTOM_REQUEST_COUNT.labels(view_name='file_upload', method=request.method).inc()
    
    # Simulate file processing
    file_size = random.randint(1, 100)  # MB
    processing_time = file_size * 0.01 + random.uniform(0.1, 0.5)
    time.sleep(processing_time)
    
    # Simulate upload errors for large files
    if file_size > 80:
        API_ERRORS.labels(view_name='file_upload', error_type='file_too_large').inc()
        return JsonResponse({'error': 'File too large'}, status=413)
    
    CUSTOM_RESPONSE_TIME.labels(view_name='file_upload').observe(time.time() - start_time)
    
    return JsonResponse({
        'filename': f'file_{random.randint(1, 1000)}.txt',
        'size_mb': file_size,
        'upload_time': time.time() - start_time,
        'status': 'uploaded'
    })

@never_cache
def analytics_data(request):
    """Analytics dashboard data"""
    start_time = time.time()
    
    CUSTOM_REQUEST_COUNT.labels(view_name='analytics_data', method=request.method).inc()
    
    # Simulate database aggregation
    time.sleep(random.uniform(0.2, 0.8))
    
    CUSTOM_RESPONSE_TIME.labels(view_name='analytics_data').observe(time.time() - start_time)
    
    return JsonResponse({
        'daily_users': random.randint(100, 500),
        'page_views': random.randint(1000, 5000),
        'bounce_rate': random.uniform(0.2, 0.8),
        'avg_session_duration': random.uniform(120, 600),
        'generated_at': time.time()
    })

# Health check endpoint
@never_cache
def health_check(request):
    """Simple health check"""
    CUSTOM_REQUEST_COUNT.labels(view_name='health_check', method=request.method).inc()
    
    return JsonResponse({
        'status': 'healthy',
        'timestamp': time.time(),
        'version': '1.0.0'
    })

# Load test endpoint
@never_cache
def load_test(request):
    """Endpoint for load testing"""
    start_time = time.time()
    
    CUSTOM_REQUEST_COUNT.labels(view_name='load_test', method=request.method).inc()
    
    # Variable processing time
    processing_time = random.uniform(0.1, 1.0)
    time.sleep(processing_time)
    
    CUSTOM_RESPONSE_TIME.labels(view_name='load_test').observe(time.time() - start_time)
    
    return JsonResponse({
        'message': f'Load test completed in {time.time() - start_time:.3f}s',
        'request_id': random.randint(10000, 99999)
    })