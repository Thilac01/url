import streamlit as st
import json
import os

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    else:
        return []

def main():
    filename = "urls.json"
    urls = load_from_json(filename)
    if urls:
        st.write("Existing URLs:")
        for url in urls:
            st.write(url)

    uploaded_urls = st.text_input("Upload URLs (one per line):", "", key="urls")

    if st.button("Upload"):
        new_urls = uploaded_urls.split("\n")
        urls.extend(new_urls)
        save_to_json(urls, filename)
        st.success("URLs uploaded successfully!")

if __name__ == "__main__":
    main()
