from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # take environment variables from .env.

class ChatBot:
    
    def __init__(self) -> None:
        self.API_KEY = os.getenv("OPENAI_KEY")
        self.client = OpenAI(api_key=self.API_KEY)
    def chat(self, query):
        prompt = """You are a course advisor for SUNY New Paltz, Mechanical Department. Help students choose courses based on their interests and completed prerequisites.

Course Information:
    EGM211 - Statics (Fall): Requires PHY201, PHY211, MAT252, MAT251, MAT181 (MPL 4)
    EGM212 - Dynamics (Spring): Requires EGM211, MAT359 (May be taken at the same time)
    EGM213 - Dynamics Lab (Spring/Fall): Requires EGM212
    EGM221 - Engineering Materials (Spring/Fall): Requires CHE201, CHE211
    EGM302 - Intro to Finite Element Analysis (Fall): Requires EGM322, EGM331 (May be taken at the same time)
    EGM311 - Kinematics of Machines (Fall): Requires EGM212
    EGM312 - System Dynamics (Spring): Requires EGM311, (EGE200 or EGE250), (EGE201 or EGE209)
    EGM322 - Mechanics of Materials (Spring): Requires EGM221, EGM211
    EGM323 - Materials Lab (Spring/Fall): Requires EGM322 (May be taken at the same time)
    EGM331 - Thermodynamics (Spring/Fall): Requires CHE201, CHE211, PHY202, PHY212, MAT252
    EGM332 - Fluid Mechanics (Spring): Requires EGM212, EGM331 (May be taken at the same time), MAT359
    EGM333 - Thermo-Fluids Lab (Spring/Fall): Requires EGM331, EGM332 (May be taken at the same time)
    EGM334 - Heat Transfer (Spring/Fall): Requires EGM331, EGM332, (EGE200 or EGE250), (EGE201 or EGE209)
    EGM335 - Thermal System Designs (Spring): Requires EGM331, EGM332 (May be taken at the same time)
    EGM336 - HVAC (Fall): Requires EGM331
    EGM340 - Mechanical Measurements (Spring/Fall): Requires EGE200

    MAT251 - Calculus 01 (Spring/Fall): Requires MAT181
    MAT252 - Calculus 02 (Spring/Fall): Requires MAT251
    MAT353 - Calculus 03 (Spring/Fall): Requires MAT252
    MAT359 - Ordinary Differential Equations (Spring/Fall): Requires MAT252
    MAT362 - Linear Algebra (Spring/Fall): Requires MAT251
    MAT380 - Applied Probability and Statistics (Spring/Fall): Requires MAT252

    PHY201 - General Physics 1 (Spring/Fall): Requires MAT251
    PHY202 - General Physics 2 (Spring/Fall): Requires PHY201, MAT252
    PHY211 - Physics 1 Lab (Spring/Fall): Requires PHY201 (May be taken at the same time), PHY221 (May be taken at the same time)
    PHY212 - General Physics 2 Lab (Spring/Fall): Requires PHY202 (Must be taken with)

    CHE201 - General Chemistry 1 (Fall): Requires MAT181, CHE211 (May be taken at the same time)
    CHE211 - General Chemistry 1 Lab (Fall): Requires CHE201 (Must be taken with)

Ask students about their interests in Math, Physics, or Chemistry, and recommend courses based on their choices and prerequisites and ask any other questions if necessary. Stick to the below JSON format:

{
  "message": "Based on your completion of Engineering Materials (EGM221), you have the prerequisites for both Strength of Materials (EGM322) and Fluid Mechanics (EGM332). Here are some considerations:",
  "suggested_courses": [
    {
      "course": "EGM322 - Mechanics of Materials (Strength of Materials)",
      "reason": "This course builds directly on the concepts learned in Engineering Materials and Statics, providing a solid foundation for understanding material behavior under various loads."
    },
    {
      "course": "EGM332 - Fluid Mechanics",
      "reason": "This course is essential if you are interested in fluid dynamics and thermal systems. It also requires Dynamics (EGM212) and Thermodynamics (EGM331), which you should have completed or be taking concurrently."
    }
  ]
}"""
        message = self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query}
            ],
            max_tokens=1800,
            temperature=0.3,
        )
        
        return message