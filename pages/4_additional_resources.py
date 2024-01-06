import streamlit as st
import webbrowser

def open_website(url):
    webbrowser.open_new_tab(url)

def main():
    st.header("Additional Resources")
    st.markdown("Here are some additional resources that may help you with your knowledge aquisition journey!")

    # classic literature:
    st.subheader("Classic Literature:  ")
    st.markdown("Visit these sites for free ebooks and audiobooks.")
    col11, col21, col31 = st.columns(3)
    with col11:
        if st.button("Project Gutenberg"):
            open_website("https://www.gutenberg.org/")
    with col31:
        if st.button("Librivox"):
            open_website("https://www.librivox.org/")
    with col21:
        if st.button("The Internet Archive"):
            open_website("https://www.archive.org/")

    # news articles:
    st.subheader("News Articles:  ")
    st.markdown("These are some great websites for reading about current events.")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("CNN (Cable News Network)"):
            open_website("https://www.cnn.com/")
    with col2:
        if st.button("BBC (British Broadcasting Corp.)"):
            open_website("https://www.bbc.com/")
    with col3:
        if st.button("WSJ (Wall Street Journal)"):
            open_website("https://www.wsj.com/")
    with col4:
        if st.button("NPR (National Public Radio)"):
            open_website("https://www.npr.org/")


    # museum virtual tours:
    st.subheader("Museum Virtual Tours:  ")
    st.markdown("You can also look around some famous museums, virtually!")
    col11, col21, col31 = st.columns(3)
    with col11:
        if st.button("The Acropolis Museum"):
            open_website("https://www.theacropolismuseum.gr/en/virtual-tour-acropolis-museum")
    with col31:
        if st.button("National Gallery of Art, Washington D.C"):
            open_website("https://www.nga.gov/features/true-to-nature-virtual-tour.html")
    with col21:
        if st.button("The Vatican Museums"):
            open_website("https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/tour-virtuali-elenco.html")

if __name__ == "__main__":
    main()