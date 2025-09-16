import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_submit_issue():
    """Test the submit-issue endpoint"""
    
    # Test data - This should now categorize as "Roads & Transport" instead of "Road Issues"
    test_data = {
        "text": "मेरा नाम अजय है, गली में गड्ढा है, सेक्टर 5 में",
        "email": "ajay@example.com",
        "name": "Ajay",
        "location": {
            "longitude": 77.2090,
            "latitude": 28.6139
        },
        "photo": None
    }
    
    print("Testing submit-issue endpoint...")
    print(f"Request data: {json.dumps(test_data, indent=2)}")
    
    try:
        response = requests.post(f"{BASE_URL}/submit-issue", json=test_data)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("Success! Response:")
            print(json.dumps(result, indent=2))
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")

def test_get_issues():
    """Test the get-issues endpoint"""
    
    print("\nTesting get-issues endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/issues")
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Success! Found {len(result)} issues:")
            for issue in result:
                print(f"- {issue['ticket_id']}: {issue['title']}")
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")

def test_get_issues_with_filters():
    """Test the get-issues endpoint with filters"""
    
    print("\nTesting get-issues endpoint with filters...")
    
    # Test with category filter
    try:
        response = requests.get(f"{BASE_URL}/issues?category=Roads%20%26%20Transport")
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Success! Found {len(result)} Roads & Transport issues:")
            for issue in result:
                print(f"- {issue['ticket_id']}: {issue['title']} ({issue['category']})")
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")

def test_get_categories():
    """Test the get-issues/categories endpoint"""
    
    print("\nTesting get-issues/categories endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/issues/categories")
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("Success! Available categories:")
            for category in result['categories']:
                print(f"- {category}")
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")

def test_get_issues_count():
    """Test the get-issues/count endpoint"""
    
    print("\nTesting get-issues/count endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/issues/count")
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Success! Total issues: {result['total_count']}")
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")

def test_update_issue_status():
    """Test the update issue status endpoint"""
    
    print("\nTesting update issue status endpoint...")
    
    # First, we need to get a ticket ID from an existing issue
    try:
        # Get all issues to find a ticket ID
        response = requests.get(f"{BASE_URL}/issues")
        
        if response.status_code == 200:
            issues = response.json()
            if issues:
                ticket_id = issues[0]['ticket_id']
                print(f"Found ticket ID: {ticket_id}")
                
                # Test updating status to "in_progress"
                status_data = {"status": "in_progress", "email": "admin@example.com"}
                print(f"Updating status to: {status_data['status']} by {status_data['email']}")
                
                update_response = requests.put(
                    f"{BASE_URL}/issues/{ticket_id}/status",
                    json=status_data,
                    headers={'Content-Type': 'application/json'}
                )
                
                print(f"Update Status Code: {update_response.status_code}")
                
                if update_response.status_code == 200:
                    result = update_response.json()
                    print("Success! Status updated:")
                    print(json.dumps(result, indent=2))
                else:
                    print(f"Error updating status: {update_response.text}")
            else:
                print("No issues found to test status update")
        else:
            print(f"Error getting issues: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")

def test_health_check():
    """Test the health-check endpoint"""
    
    print("\nTesting health-check endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("Success! Response:")
            print(json.dumps(result, indent=2))
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")

def test_duplicate_issue():
    """Test duplicate issue detection"""
    
    print("\nTesting duplicate issue detection...")
    
    # Same data as before
    test_data = {
        "text": "मेरा नाम अजय है, गली में गड्ढा है, सेक्टर 5 में",
        "email": "priya@example.com",  # Different email
        "name": "Priya",
        "location": {
            "longitude": 77.2090,
            "latitude": 28.6139
        },
        "photo": None
    }
    
    print(f"Request data: {json.dumps(test_data, indent=2)}")
    
    try:
        response = requests.post(f"{BASE_URL}/submit-issue", json=test_data)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("Success! Response:")
            print(json.dumps(result, indent=2))
            print(f"Issue count: {result.get('issue_count', 'N/A')}")
            print(f"Users: {result.get('users', [])}")
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("=== Municipal Voice Assistant API Test ===\n")
    
    # Test health check first
    test_health_check()
    
    # Test submit issue
    test_submit_issue()
    
    # Test get all issues
    test_get_issues()
    
    # Test get issues with filters
    test_get_issues_with_filters()
    
    # Test get categories
    test_get_categories()
    
    # Test get issues count
    test_get_issues_count()
    
    # Test update issue status
    test_update_issue_status()
    
    # Test duplicate issue
    test_duplicate_issue()
    
    print("\n=== Test Complete ===")
