import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_completion_system():
    """Test the dual completion system"""
    
    print("=== Testing Dual Completion System ===\n")
    
    try:
        # First, get all issues to find a ticket ID
        print("1. Getting all issues...")
        response = requests.get(f"{BASE_URL}/issues")
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            issues = response.json()
            print(f"   Found {len(issues)} issues")
            
            if issues:
                ticket_id = issues[0]['ticket_id']
                print(f"   Using ticket ID: {ticket_id}")
                
                # Test 1: Try to mark user completion before admin (should fail)
                print("\n2. Test 1: User completion before admin (should fail)")
                user_completion_data = {
                    "email": "user@example.com",
                    "completion_type": "user"
                }
                
                try:
                    user_response = requests.post(
                        f"{BASE_URL}/issues/{ticket_id}/complete",
                        json=user_completion_data,
                        headers={'Content-Type': 'application/json'}
                    )
                    
                    print(f"   Response Status: {user_response.status_code}")
                    if user_response.status_code == 400:
                        print("   ✅ Correctly rejected: User cannot complete before admin")
                    else:
                        print(f"   ❌ Unexpected response: {user_response.text}")
                        
                except Exception as e:
                    print(f"   ❌ Exception: {e}")
                
                # Test 2: Mark admin completion (should succeed)
                print("\n3. Test 2: Admin completion (should succeed)")
                admin_completion_data = {
                    "email": "admin@example.com",
                    "completion_type": "admin"
                }
                
                try:
                    admin_response = requests.post(
                        f"{BASE_URL}/issues/{ticket_id}/complete",
                        json=admin_completion_data,
                        headers={'Content-Type': 'application/json'}
                    )
                    
                    print(f"   Response Status: {admin_response.status_code}")
                    if admin_response.status_code == 200:
                        result = admin_response.json()
                        print("   ✅ Admin completion successful!")
                        print(f"   Response: {json.dumps(result, indent=2)}")
                    else:
                        print(f"   ❌ Admin completion failed: {admin_response.text}")
                        
                except Exception as e:
                    print(f"   ❌ Exception: {e}")
                
                # Test 3: Now try user completion (should succeed)
                print("\n4. Test 3: User completion after admin (should succeed)")
                
                try:
                    user_response2 = requests.post(
                        f"{BASE_URL}/issues/{ticket_id}/complete",
                        json=user_completion_data,
                        headers={'Content-Type': 'application/json'}
                    )
                    
                    print(f"   Response Status: {user_response2.status_code}")
                    if user_response2.status_code == 200:
                        result = user_response2.json()
                        print("   ✅ User completion successful!")
                        print(f"   Response: {json.dumps(result, indent=2)}")
                        
                        # Check if issue is fully completed
                        if result.get("is_fully_completed"):
                            print("   🎉 Issue is now fully completed!")
                        else:
                            print("   ⚠️  Issue not yet fully completed")
                    else:
                        print(f"   ❌ User completion failed: {user_response2.text}")
                        
                except Exception as e:
                    print(f"   ❌ Exception: {e}")
                
                # Test 4: Check final issue status
                print("\n5. Test 4: Check final issue status")
                try:
                    final_response = requests.get(f"{BASE_URL}/issues")
                    if final_response.status_code == 200:
                        final_issues = final_response.json()
                        for issue in final_issues:
                            if issue['ticket_id'] == ticket_id:
                                print(f"   Final Status: {issue['status']}")
                                print(f"   Admin Completed: {issue.get('admin_completed_at', 'No')}")
                                print(f"   User Completed: {issue.get('user_completed_at', 'No')}")
                                print(f"   Fully Completed: {issue.get('completed_at', 'No')}")
                                break
                    else:
                        print(f"   ❌ Failed to get final status: {final_response.text}")
                        
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
    test_completion_system()
