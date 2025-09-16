import asyncio
import sys
import os

# Add the app directory to the path so we can import the gemini_service
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from gemini_service import analyze_text

async def test_descriptions():
    """Test the new varied description generation"""
    
    print("=== Testing New Varied Descriptions ===\n")
    
    # Test cases with different types of issues
    test_cases = [
        {
            "text": "मेरा नाम अजय है, गली में गड्ढा है, सेक्टर 5 में",
            "expected_category": "Roads & Transport",
            "description": "Hindi text about pothole in street"
        },
        {
            "text": "There is a huge pothole on the main road near sector 3",
            "expected_category": "Roads & Transport", 
            "description": "English text about pothole on main road"
        },
        {
            "text": "Garbage is overflowing from dustbin in sector 7",
            "expected_category": "Sanitation & Waste",
            "description": "English text about overflowing garbage"
        },
        {
            "text": "सड़क पर कचरा फैला हुआ है, सेक्टर 2 में",
            "expected_category": "Sanitation & Waste",
            "description": "Hindi text about garbage on road"
        },
        {
            "text": "Streetlight is not working in sector 4",
            "expected_category": "Electricity & Streetlights",
            "description": "English text about broken streetlight"
        },
        {
            "text": "बिजली की समस्या है, सेक्टर 6 में",
            "expected_category": "Electricity & Streetlights",
            "description": "Hindi text about electricity problem"
        },
        {
            "text": "Water supply is interrupted in sector 1",
            "expected_category": "Water & Drainage",
            "description": "English text about water supply issue"
        },
        {
            "text": "नाली बंद है, सेक्टर 8 में",
            "expected_category": "Water & Drainage",
            "description": "Hindi text about blocked drainage"
        },
        {
            "text": "Traffic signal is not working properly",
            "expected_category": "Roads & Transport",
            "description": "English text about traffic signal issue"
        },
        {
            "text": "पार्क में पेड़ गिर गया है",
            "expected_category": "Environment & Parks",
            "description": "Hindi text about fallen tree in park"
        },
        {
            "text": "There is a huge pothole on the main road near sector 3 market",
            "expected_category": "Roads & Transport",
            "description": "English text about huge pothole near market"
        },
        {
            "text": "बिजली की समस्या है, सेक्टर 6 में, अस्पताल के पास",
            "expected_category": "Electricity & Streetlights",
            "description": "Hindi text about electricity problem near hospital"
        },
        {
            "text": "Garbage is overflowing from dustbin in sector 7, urgent matter",
            "expected_category": "Sanitation & Waste",
            "description": "English text about urgent overflowing garbage"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input Text: {test_case['text']}")
        
        try:
            result = await analyze_text(test_case['text'])
            
            print(f"Category: {result['category']}")
            print(f"Address: {result['address']}")
            print(f"Title: {result['title']}")
            print(f"Original Text: {result['original_text']}")
            print(f"Description: {result['description']}")
            
            # Check if category matches expected
            if result['category'] == test_case['expected_category']:
                print("✅ Category matched!")
            else:
                print(f"❌ Category mismatch! Expected: {test_case['expected_category']}, Got: {result['category']}")
            
            print("-" * 80)
            print()
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("-" * 80)
            print()

if __name__ == "__main__":
    asyncio.run(test_descriptions())
