# /src/skills/recommender.py
from ..utils.embedding_utils import generate_embedding
from vector_db.chroma_db import ChromaDBWrapper

class SemanticRecommender:
    def __init__(self):
        print("Initializing Semantic Recommender...")
        self.db = ChromaDBWrapper()
        self.course_descriptions = [
            "Python programming for beginners",
            "Machine learning with scikit-learn",
            "Deep learning with TensorFlow",
            "Data analysis with pandas and Python",
            "Introduction to artificial intelligence"
        ]
        self.course_titles = [
            "Python for Beginners",
            "Machine Learning",
            "Deep Learning",
            "Data Analysis with Pandas",
            "AI Basics"
        ]
        # Generate embeddings for all course descriptions
        course_embeddings = generate_embedding(self.course_descriptions)
        # Add courses to Chroma DB
        self.db.add_embeddings(
            ids=[str(i) for i in range(len(self.course_titles))],
            embeddings=course_embeddings,
            metadatas=self.course_titles
        )

    def recommend_courses(self, user_skills):
        # Generate embedding for user's skills
        user_embedding = generate_embedding([user_skills])[0]
        # Query the Chroma DB for top 3 similar courses
        results = self.db.query(user_embedding, n_results=3)

        # Return the top results with score
        recommendations = []
        for result in results['documents']:
            course_title = result
            course_id = results['ids'][results['documents'].index(course_title)]
            score = results['distances'][results['documents'].index(course_title)]
            recommendations.append({
                "course_title": course_title,
                "match_score": score
            })
        return recommendations


if __name__ == "__main__":
    recommender = SemanticRecommender()
    
    # Test user input
    user_skills = "I am looking to learn Python and data analysis"
    print(f"Recommendations for: {user_skills}")
    recommendations = recommender.recommend_courses(user_skills)
    
    for i, recommendation in enumerate(recommendations):
        print(f"{i+1}. {recommendation['course_title']} (Match score: {recommendation['match_score']})")
