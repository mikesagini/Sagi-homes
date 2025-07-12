import openai
import streamlit as st


# Make sure to add "openai_api_key" to your .streamlit/secrets.toml file like:
# [general]
# openai_api_key = "your-openai-api-key"
if not openai.api_key:
    st.error("OpenAI API key not found. Please add it to .streamlit/secrets.toml.")
st.title("Sagini Estate Listing Generator")

location = st.text_input("Property Location (e.g., Kileleshwa, Nairobi)")
property_type = st.text_input("Property Type (e.g., 3-bedroom apartment)")
price = st.text_input("Price (e.g., KES 14M)")
features = st.text_area("Features (comma separated, e.g., Modern kitchen, Swimming pool, 24/7 security)")

if st.button("Generate Listing Description"):
    if not location or not property_type or not price or not features:
        st.error("Please fill in all fields.")
    else:
        prompt = (
            f"Write a compelling real estate listing description for a {property_type} "
            f"located in {location}, priced at {price}. Features include: {features}."
        )

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7
            )
            description = response.choices[0].message.content.strip()
            st.subheader("Generated Listing Description:")
            st.write(description)
        except Exception as e:
            st.error(f"API error: {e}")
