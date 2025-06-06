from openai import OpenAI # type: ignore


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

def gen_answer(input):
    completion = client.chat.completions.create(
        extra_body={},
        model="meta-llama/llama-3.3-70b-instruct",
        messages=[
            {
            "role": "user",
            "content": input
            }
        ]
    )
    
    if not completion.choices[0]:
        return "Đã hết hạn sử dụng hôm nay, hãy quay lại sau!"
    
    return completion.choices[0].message.content

def gen_quiz(topic):
    prompt = f'''
            Generate just 10 quiz questions with four-choice answer about {topic} in English. 
            Include the question and answers in the format: Question | Answer 1, Answer 2,  Answer 3, Answer 4 | Correct Answer.
            Return only question and answers.
            Examples:
            What __ your name? | am, is, are, was | is
            He __ in Paris for three years. | have lived, had lived, lived, has lived | had lived
            '''
    
    response = gen_answer(prompt)

    response = response.splitlines()
    
    return response
