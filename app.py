import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Smart Summary AI",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Smart Summary AI")
st.write("Convert lengthy text into easy-to-read summaries.")

@st.cache_resource
def create_summarizer():
    return pipeline(
        task="summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )

article = st.text_area(
    "Enter your article",
    placeholder="Type or paste your article here...",
    height=220
)

summary_size = st.selectbox(
    "Select summary size",
    ["Short", "Medium", "Long"]
)

settings = {
    "Short": (10, 40),
    "Medium": (25, 80),
    "Long": (40, 120)
}

if st.button("Generate Summary", type="primary"):
    if len(article.split()) < 20:
        st.warning("Please enter at least 20 words.")
    else:
        try:
            minimum, maximum = settings[summary_size]

            with st.spinner("Summarizing your text..."):
                summarizer = create_summarizer()
                response = summarizer(
                    article,
                    min_length=minimum,
                    max_length=maximum,
                    do_sample=False,
                    truncation=True
                )

            summary = response[0]["summary_text"]

            st.subheader("Generated Summary")
            st.write(summary)

            col1, col2 = st.columns(2)
            col1.metric("Original Words", len(article.split()))
            col2.metric("Summary Words", len(summary.split()))

            st.download_button(
                "Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

        except Exception as error:
            st.error(f"Unable to summarize text: {error}")

st.divider()
st.caption("Built with Python, Streamlit and Hugging Face Transformers.")
