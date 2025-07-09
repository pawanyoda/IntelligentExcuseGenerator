import streamlit as st
from models.excuse_generator import ExcuseGenerator
from utils.proof_generator import ProofGenerator

generate = ExcuseGenerator()
proof = ProofGenerator()

# st.title("🤖 Intelligent Excuse Generator")
#
# scenario = st.selectbox("Scenario", ["Work", "School", "Social", "Family"])
# details = st.text_input("What Happened")
# generate_proof = st.checkbox("Generate Supporting proof")


def main():
    st.title("🤖 Intelligent Excuse Generator")

    scenario = st.selectbox("Scenario", ["Work", "School", "Social", "Family"])
    details = st.text_input("What Happened")
    generate_proof = st.checkbox("Generate Supporting proof")

    if st.button("Generate Excuse"):
        with st.spinner("Generating Excuse alibi..."):
            excuse = generate.generate(scenario, details)
            st.success(excuse)

            if generate_proof:
                st.divider()
                st.subheader("Supporting Documents")
                tab1, tab2 = st.tabs(["Doctor's Note", "Chat Log"])

                with tab1:
                    st.json(proof.generate_doctors_note())
                with tab2:
                    chat = proof.generate_chat_log(
                        "Friends",
                        f"Hey, I can confirm {excuse}"
                    )
                    st.json(chat)

if __name__ == "__main__":
    main()
