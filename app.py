import streamlit as st

st.set_page_config(
    page_title="AI Newsletter Agent"
)

st.title(
    "AI Newsletter Agent"
)

try:

    from agent import (
        run_newsletter_agent
    )

    st.success(
        "Agent loaded"
    )

except Exception as e:

    st.error(
        str(e)
    )

goal = st.text_area(
    "Goal",
    value="""
Create a weekly newsletter
on latest AI agent news
"""
)

mode = st.selectbox(
    "Mode",
    [
        "auto",
        "human"
    ]
)

if st.button(
    "Run Agent"
):

    result = (
        run_newsletter_agent(
            goal,
            mode
        )
    )

    st.write(result)