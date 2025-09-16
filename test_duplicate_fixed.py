import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_duplicate_detection():
    """Test the duplicate detection with your specific example"""
    
    print("🧪 Testing Duplicate Detection - Clean Test")
    print("=" * 60)
    
    # First, clear any existing data by checking current state
    response = requests.get(f"{BASE_URL}/issues")
    if response.status_code == 200:
        issues = response.json()
        print(f"Current issues in system: {len(issues)}")
    
    # Test Case 1: Shyam reports light issue
    print("\n1️⃣ Test Case 1: Shyam reports light issue")
    data_shyam = {
        "text": "मेरा नाम है shyam, light की समस्या है, vijay nagar में",
        "email": "shyam_new@example.com",  # Use new email to avoid previous data
        "name": "shyam",
        "location": {
            "latitude": 28.6139,  # Valid coordinates (Delhi)
            "longitude": 77.2090
        }
    }
    
    response1 = requests.post(f"{BASE_URL}/submit-issue", json=data_shyam)
    print(f"Status: {response1.status_code}")
    if response1.status_code == 200:
        result1 = response1.json()
        print(f"Ticket ID: {result1['ticket_id']}")
        print(f"Category: {result1['category']}")
        print(f"Issue Count: {result1['issue_count']}")
        print(f"Users: {result1['users']}")
        
        # Test Case 2: Monu reports very similar light issue
        print("\n2️⃣ Test Case 2: Monu reports similar light issue")
        data_monu = {
            "text": "मेरा नाम है monu, light की समस्या है, vijay nagar में",
            "email": "monu_new@example.com",  # Use new email
            "name": "monu", 
            "location": {
                "latitude": 28.6140,  # Very close location (11m difference)
                "longitude": 77.2091
            }
        }
        
        response2 = requests.post(f"{BASE_URL}/submit-issue", json=data_monu)
        print(f"Status: {response2.status_code}")
        if response2.status_code == 200:
            result2 = response2.json()
            print(f"Ticket ID: {result2['ticket_id']}")
            print(f"Category: {result2['category']}")
            print(f"Issue Count: {result2['issue_count']}")
            print(f"Users: {result2['users']}")
            
            # Check if they got the same ticket ID (duplicate detected)
            if result1['ticket_id'] == result2['ticket_id']:
                print("✅ SUCCESS: Duplicate detected! Same ticket ID returned.")
                print(f"   Issue count increased from {result1['issue_count']} to {result2['issue_count']}")
                print(f"   Users combined: {result2['users']}")
            else:
                print("❌ FAILED: Different ticket IDs - duplicate not detected.")
                print(f"   Shyam's ticket: {result1['ticket_id']}")
                print(f"   Monu's ticket: {result2['ticket_id']}")
        else:
            print(f"Error: {response2.text}")
    else:
        print(f"Error: {response1.text}")
    
    # Final summary
    print("\n📊 Final Summary:")
    response = requests.get(f"{BASE_URL}/issues")
    if response.status_code == 200:
        issues = response.json()
        print(f"Total issues: {len(issues)}")
        for issue in issues[-2:]:  # Show last 2 issues
            print(f"- {issue['ticket_id']}: {issue['category']} (Count: {issue['issue_count']}, Users: {len(issue['users'])})")

if __name__ == "__main__":
    test_duplicate_detection()
