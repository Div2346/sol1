import json

resume_text = """
[Insert your resume content here]
"""

# Example structure for parsing (simplified)
resume_data = {
    "Contact Information": {
        "Name": "Divyanshi Sharma",
        "Email": "your-email@example.com",
        "Phone": "123-456-7890",
        "Location": "Delhi, India",
        "LinkedIn": "https://www.linkedin.com/in/divyanshi-sharma23",
        "GitHub": "https://github.com/Div2346"
    },
    "Summary": "Data Analyst with experience in machine learning, deep learning, and AI, seeking to leverage skills in data analysis, LLMs, and prompt engineering to contribute to innovative projects.",
    "Education": [
        {
            "Degree": "Bachelor of Technology in Computer Science",
            "Institution": "XYZ University",
            "Graduation Year": "2024"
        }
    ],
    "Experience": [
        {
            "Position": "Product Development Intern",
            "Company": "Vegapay",
            "Duration": "July 2024",
            "Responsibilities": [
                "Worked on enhancing product features",
                "Collaborated with cross-functional teams"
            ]
        },
        {
            "Position": "Data Analyst Intern",
            "Company": "Stride One (Stride Green)",
            "Location": "Gurgaon",
            "Responsibilities": [
                "Analyzed large datasets to extract actionable insights",
                "Supported the development of data-driven strategies"
            ]
        }
    ],
    "Skills": [
        "Data Analysis"
        "Machine Learning",
        "Deep Learning",
        "Python",
        "Prompt Engineering",
        "AWS"
    ],
    "Projects": [
        {
            "Title": "MBTI Data Analysis",
            "Duration": "November 2023 - December 2023",
            "Description": "Conducted sentiment analysis on user tweets, examined personality types, and analyzed socio-cultural data using NLP techniques."
        },
        {
            "Title": "SignSpeak: Sign Language Recognition and Translation",
            "Duration": "February 2024 - April 2024",
            "Description": "Developed an LSTM-based model for sign language recognition, integrated knowledge distillation over BERT for translation, and streamlined information flow using NVIDIA A100 servers."
        }
    ]
}

# Convert to JSON
json_output = json.dumps(resume_data, indent=4)
print(json_output)
