import requests
import json

# API base URL
BASE_URL = "http://localhost:5600"

def test_get_user_issues():
    """Test the get-user-issues endpoint"""
    
    # Test data
    test_data = {
        "email": "ajay@example.com"
    }
    
    print("Testing get-user-issues endpoint...")
    print(f"Request data: {json.dumps(test_data, indent=2)}")
    
    try:
        response = requests.post(f"{BASE_URL}/issues/user", json=test_data)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Success! Found {len(result)} issues for user:")
            for issue in result:
                print(f"- {issue['ticket_id']}: {issue['title']} ({issue['category']}) - Status: {issue['status']}")
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running on port 5600.")
    except Exception as e:
        print(f"Error: {e}")

def test_get_user_issues_empty():
    """Test the endpoint with a user who has no issues"""
    
    # Test data for user with no issues
    test_data = {
        "email": "nonexistent@example.com"
    }
    
    print("\nTesting get-user-issues endpoint with non-existent user...")
    print(f"Request data: {json.dumps(test_data, indent=2)}")
    
    try:
        response = requests.post(f"{BASE_URL}/issues/user", json=test_data)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Success! Found {len(result)} issues for user (expected 0)")
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running on port 5600.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_get_user_issues()
    test_get_user_issues_empty()
