import os
import json

def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def calculate_match_score(resume, job_desc):
    resume_words = set(resume.lower().split())
    job_words = set(job_desc.lower().split())
    matches = len(resume_words & job_words)
    score = int((matches / max(len(job_words), 1)) * 100)
    return score

def generate_cover_letter(resume, job_desc):
    # This is a placeholder for actual AI generation code
    # Replace with generative AI API call if available
    return (
        "Dear Hiring Manager,\n"
        "I am excited to apply for your position. My experience in Python, API development, "
        "and cloud deployments aligns with the job requirements. "
        "I am enthusiastic about mentoring teams and delivering scalable solutions.\n"
        "Sincerely,\nYour Name"
    )

def main():
    resume_path = os.path.join('inputs', 'resume.txt')
    job_path = os.path.join('inputs', 'job_description.txt')

    resume = load_file(resume_path)
    job_desc = load_file(job_path)

    score = calculate_match_score(resume, job_desc)
    cover_letter = generate_cover_letter(resume, job_desc)

    result = {
        "match_score": score,
        "cover_letter": cover_letter,
        "suggestions": [
            "Expand on cloud experience",
            "Highlight project leadership",
            "Mention any successful API deployments"
        ]
    }
    print("=== Demo Output ===")
    print(json.dumps(result, indent=2))

    with open("sample_output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print("Output also saved to sample_output.json")

if __name__ == "__main__":
    main()
