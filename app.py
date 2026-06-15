import streamlit as st

from agent import (
    run_newsletter_agent
)

st.title(
    "AI Newsletter Agent"
)

goal = st.text_area(
    "Goal",
    value="""Create a weekly newsletter on latest AI agent news and send it to subscribers"""
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

    with st.spinner(
        "Running..."
    ):

        result = (
            run_newsletter_agent(
                goal,
                mode
            )
        )

    if result != "Rejected":

        st.success(
            "Completed"
        )

        st.subheader(
            "Execution Plan"
        )

        st.write(
            result["plan"]
        )

        st.subheader(
            "Newsletter"
        )

        st.markdown(
            result[
                "newsletter"
            ]
        )

        st.info(f"""Saved:{result['file']}""")