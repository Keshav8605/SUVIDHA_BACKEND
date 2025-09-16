import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_similar_issues():
    """Test the new intelligent duplicate detection"""
    
    print("🧪 Testing Intelligent Duplicate Detection")
    print("=" * 60)
    
    # Test Case 1: Exact same issue (should be duplicate)
    print("\n1️⃣ Test Case 1: Exact same issue")
    test_data_1 = {
        "text": "मेरा नाम अजय है, गली में गड्ढा है, सेक्टर 5 में",
        "email": "ajay@example.com",
        "name": "Ajay",
        "location": {
            "longitude": 77.2090,
            "latitude": 28.6139
        },
        "photo": None
    }
    
    response = requests.post(f"{BASE_URL}/submit-issue", json=test_data_1)
    print(f"First submission - Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Ticket ID: {result['ticket_id']}")
        print(f"Issue Count: {result['issue_count']}")
    
    # Test Case 2: Similar text, same location (should be duplicate)
    print("\n2️⃣ Test Case 2: Similar text, same location")
    test_data_2 = {
        "text": "मेरा नाम प्रिया है, सड़क में गड्ढा है, सेक्टर 5 में",
        "email": "priya@example.com",
        "name": "Priya",
        "location": {
            "longitude": 77.2090,
            "latitude": 28.6139
        },
        "photo": None
    }
    
    response = requests.post(f"{BASE_URL}/submit-issue", json=test_data_2)
    print(f"Second submission - Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Ticket ID: {result['ticket_id']}")
        print(f"Issue Count: {result['issue_count']}")
        print(f"Users: {result['users']}")
    
    # Test Case 3: Similar text, nearby location (should be duplicate)
    print("\n3️⃣ Test Case 3: Similar text, nearby location (within 500m)")
    test_data_3 = {
        "text": "मेरा नाम राहुल है, गली में गड्ढा है, सेक्टर 5 में",
        "email": "rahul@example.com",
        "name": "Rahul",
        "location": {
            "longitude": 77.2095,  # Very close to original
            "latitude": 28.6140
        },
        "photo": None
    }
    
    response = requests.post(f"{BASE_URL}/submit-issue", json=test_data_3)
    print(f"Third submission - Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Ticket ID: {result['ticket_id']}")
        print(f"Issue Count: {result['issue_count']}")
        print(f"Users: {result['users']}")
    
    # Test Case 4: Different category, same location (should NOT be duplicate)
    print("\n4️⃣ Test Case 4: Different category, same location")
    test_data_4 = {
        "text": "मेरा नाम सीता है, पानी की समस्या है, सेक्टर 5 में",
        "email": "sita@example.com",
        "name": "Sita",
        "location": {
            "longitude": 77.2090,
            "latitude": 28.6139
        },
        "photo": None
    }
    
    response = requests.post(f"{BASE_URL}/submit-issue", json=test_data_4)
    print(f"Fourth submission - Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Ticket ID: {result['ticket_id']}")
        print(f"Category: {result['category']}")
        print(f"Issue Count: {result['issue_count']}")
    
    # Test Case 5: Far location, similar text (should NOT be duplicate)
    print("\n5️⃣ Test Case 5: Far location, similar text")
    test_data_5 = {
        "text": "मेरा नाम अमित है, गली में गड्ढा है, सेक्टर 5 में",
        "email": "amit@example.com",
        "name": "Amit",
        "location": {
            "longitude": 77.2200,  # Far from original
            "latitude": 28.6200
        },
        "photo": None
    }
    
    response = requests.post(f"{BASE_URL}/submit-issue", json=test_data_5)
    print(f"Fifth submission - Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Ticket ID: {result['ticket_id']}")
        print(f"Issue Count: {result['issue_count']}")
    
    # Get all issues
    print("\n📊 Final Summary:")
    response = requests.get(f"{BASE_URL}/issues")
    if response.status_code == 200:
        issues = response.json()
        print(f"Total issues: {len(issues)}")
        for issue in issues:
            print(f"- {issue['ticket_id']}: {issue['category']} in {issue['address']} (Count: {issue['issue_count']})")

if __name__ == "__main__":
    test_similar_issues()
