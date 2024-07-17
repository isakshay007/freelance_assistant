import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Freelance Assistant")
st.markdown("Welcome to Freelance Assistant, your personalized freelancing guide. Enter your career details and goals for customized tips and strategies to enhance your freelance journey.")
st.markdown("            1) Mention your field of expertise. ")
st.markdown("            2) Mention your experience level.")
st.markdown("            3) Mention the income goals.")
st.markdown("            4) Mention your preferred work-life balance.")
input = st.text_input(" Please enter the above details:",placeholder=f"""Type here""")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def generation(input):
    generator_agent = Agent(
        role="Expert FREELANCING CONSULTANT",
        prompt_persona=f"Your task is to OFFER personalized freelancing tips and strategic advice that aligns with the user's specific details.")
    prompt = f"""
You are an Expert FREELANCING CONSULTANT. Your task is to OFFER personalized freelancing tips and strategic advice that aligns with the user's specific details.

Proceed as follows:

1. IDENTIFY detailed information on the user's FIELD OF EXPERTISE , the user's EXPERIENCE LEVEL ,  the user's INCOME GOALS and the user’s preferred WORK-LIFE BALANCE.

2. Based on above provided detailed user information DEVELOP a customized plan that includes:

-  personalized freelancing tips

- strategic advice

DISPLAY the output in markdown format


 """

    generator_agent_task = Task(
        name="Generation",
        model=open_ai_text_completion_model,
        agent=generator_agent,
        instructions=prompt,
        default_input=input,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
    ).execute()

    return generator_agent_task 
   
if st.button("Assist!"):
    solution = generation(input)
    st.markdown(solution)

with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Automata Agent . For any inquiries or issues, please contact Lyzr.

    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack",
                   url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw',
                   use_container_width=True)