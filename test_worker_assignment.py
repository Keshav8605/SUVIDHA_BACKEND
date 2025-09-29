import requests
import json

BASE_URL = "http://localhost:8000"

def test_worker_assignment():
    # 1. Get all departments
    print("1. Getting departments...")
    response = requests.get(f"{BASE_URL}/departments")
    print(f"Departments: {response.status_code}")
    
    # 2. Get all workers  
    print("2. Getting workers...")
    response = requests.get(f"{BASE_URL}/workers")
    print(f"Workers: {response.status_code}")
    
    # 3. Get unassigned issues
    print("3. Getting unassigned issues...")
    response = requests.get(f"{BASE_URL}/issues/unassigned")
    print(f"Unassigned issues: {response.status_code}")
    if response.status_code == 200:
        issues = response.json()
        print(f"Found {len(issues)} unassigned issues")
    
    # 4. Get assignments
    print("4. Getting assignments...")
    response = requests.get(f"{BASE_URL}/assignments")
    print(f"Assignments: {response.status_code}")

if __name__ == "__main__":
    test_worker_assignment()