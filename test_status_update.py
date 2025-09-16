import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_status_update():
    """Test the status update endpoint with detailed debugging"""
    
    print("=== Testing Status Update Endpoint ===\n")
    
    # First, get all issues to find a ticket ID
    try:
        print("1. Getting all issues...")
        response = requests.get(f"{BASE_URL}/issues")
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            issues = response.json()
            print(f"   Found {len(issues)} issues")
            
            if issues:
                ticket_id = issues[0]['ticket_id']
                print(f"   Using ticket ID: {ticket_id}")
                
                # Test different status update formats
                test_cases = [
                    {"status": "new", "email": "admin@example.com"},
                    {"status": "in_progress", "email": "admin@example.com"},
                    {"status": "in progress", "email": "admin@example.com"},  # Test space version
                    {"status": "completed", "email": "admin@example.com"}
                ]
                
                for i, test_data in enumerate(test_cases, 1):
                    print(f"\n2. Test Case {i}: Updating status to '{test_data['status']}'")
                    print(f"   Request URL: {BASE_URL}/issues/{ticket_id}/status")
                    print(f"   Request Body: {json.dumps(test_data, indent=2)}")
                    
                    try:
                        update_response = requests.put(
                            f"{BASE_URL}/issues/{ticket_id}/status",
                            json=test_data,
                            headers={'Content-Type': 'application/json'}
                        )
                        
                        print(f"   Response Status: {update_response.status_code}")
                        print(f"   Response Headers: {dict(update_response.headers)}")
                        
                        if update_response.status_code == 200:
                            result = update_response.json()
                            print("   ✅ Success! Response:")
                            print(f"   {json.dumps(result, indent=2)}")
                            
                            # Verify timestamp tracking for specific statuses
                            if test_data['status'] == 'in_progress' and result.get('in_progress_at'):
                                print(f"   ✅ Timestamp tracked: in_progress_at = {result['in_progress_at']}")
                            elif test_data['status'] == 'completed' and result.get('completed_at'):
                                print(f"   ✅ Timestamp tracked: completed_at = {result['completed_at']}")
                        else:
                            print(f"   ❌ Error Response:")
                            print(f"   {update_response.text}")
                            
                    except Exception as e:
                        print(f"   ❌ Exception: {e}")
            else:
                print("   No issues found to test")
        else:
            print(f"   Error getting issues: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_status_update()
