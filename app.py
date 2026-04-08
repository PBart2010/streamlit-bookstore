import streamlit as st

st.set_page_config(page_title="Reader's Online Store", layout="wide")

st.title("Reader's Online Store")
st.subheader("Welcome to Reader's Verse")
st.markdown("### Catalog of Books")

books = {
    "The Great Gatsby": "F. Scott Fitzgerald's classic novel set in the Roaring Twenties, following the decadent lifestyle of Jay Gatsby and his wife Daisy Buchanan.",
    "Pride and Prejudice": "The story follows the romantic exploits of the Bennet sisters, Mary and Elizabeth, as they navigate the social norms of the Regency era in England.",
    "The Hobbit": "The Hobbit is a fantasy novel by J. R. R. Tolkien. It was published in 1937 and is the first book of The Lord of the Rings.",
    "The Lord of the Rings": "The Lord of the Rings is an epic high-fantasy novel written by J. R. R. Tolkien.",
    "Animal Farm": "Animal Farm is a novella by George Orwell. It was published in 1945 and is a political satire of the Soviet Union.",
    "Brave New World": "Brave New World is a 1932 novel by Aldous Huxley, published by Secker & Warburg, and is regarded by many critics as one of the greatest novels of the 20th century."
}

search_term = st.text_input("Search for a book title")

filtered_books = {
    title: desc
    for title, desc in books.items()
    if search_term.lower() in title.lower()
}

if filtered_books:
    for title, desc in filtered_books.items():
        st.markdown(f"#### {title}")
        st.write(desc)
        st.divider()
else:
    st.warning("No books found.")
