import streamlit as st 
import requests 
st.title("Whether App")
city = st.text_input("Enter City Name")
search = st.button("Search")
if search and city:
    api_key = "974359bd870b4c17ee1efdb78e65b58a"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == "404":
        st.error("City Not Found")
    else:
        st.success("City Found")
        st.write(f"city: {city}")
        st.write(f"Temparature: {data['main']['temp']} K")
        st.write(f"Humidity: {data['main']['humidity']}")
        




