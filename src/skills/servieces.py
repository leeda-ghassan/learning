from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class CourseRecommender:
    def __init__(self, openai_api_key: str, model_name: str = "gpt-4o-mini", temperature: float = 0):
        self.openai_api_key = openai_api_key
        self.model_name = model_name
        self.temperature = temperature

        # Initialize OpenAI LLM
        self.llm = ChatOpenAI(
            temperature=self.temperature,
            model_name=self.model_name,
            openai_api_key=self.openai_api_key
        )

        # Define the PromptTemplate to recommend courses with priorities
        self.prompt_template = PromptTemplate(
            input_variables=["experience", "level", "major", "duration"],
            template=(
                "Based on the user's experience: {experience}, "
                "level: {level}, major: {major}, "
                "and desired course duration: {duration}, "
                "recommend top courses. "
                "Rank them in the order of relevance to the user's background and goals. "
                "Provide the course name, duration, and description in a clear numbered list, "
                "with the most relevant course listed first. "
                "Do NOT use any Markdown formatting (no **, *, _, etc.), just plain text."
            )
        )

        # Initialize the LLMChain
        self.course_chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt_template
        )

    def recommend_courses(self, experience: str, level: str, major: str, duration: str) -> str:
        """Generates prioritized course recommendations based on user input."""
        result = self.course_chain.run(
            {
                "experience": experience,
                "level": level,
                "major": major,
                "duration": duration
            }
        )
        return result


if __name__ == "__main__":
    recommender = CourseRecommender(openai_api_key=OPENAI_API_KEY)

    # Example user input
    experience = "I have experience in baking pastry 3 years , I want learn how to make pasta"
    level = "beginner"
    major = "chef"
    duration = "3 weeks"

    recommendations = recommender.recommend_courses(
        experience=experience,
        level=level,
        major=major,
        duration=duration
    )

    print("Recommended Courses:\n")
    print(recommendations)
