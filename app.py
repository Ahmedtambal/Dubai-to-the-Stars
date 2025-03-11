import streamlit as st
from datetime import datetime, timedelta
from logic import (
    get_destinations,
    get_pricing,
    get_accommodation_recommendations,
    validate_booking,
    get_ai_travel_tips,
)

# Sidebar Navigation
st.sidebar.title("Dubai to the Stars")
page = st.sidebar.radio("Navigate", ["Home", "Book a Trip", "Dashboard"])

if page == "Home":
    st.title("Dubai to the Stars – Space Travel Booking Platform")
    st.write("Welcome to the ultimate space travel booking experience from Dubai to the Stars.")
    st.write("Book your space trip to orbital stations, lunar hotels, and other amazing destinations.")

elif page == "Book a Trip":
    st.title("Book a Space Trip")
    
    st.header("Trip Scheduling & Booking")
    departure_date = st.date_input("Select Departure Date", datetime.today())
    destinations = get_destinations()
    destination = st.selectbox("Select Destination", options=destinations)
    seat_class = st.selectbox("Select Seat Class", options=["Economy", "Luxury", "VIP"])
    
    st.header("Pricing & Packages")
    pricing_info = get_pricing(destination, seat_class)
    st.write(f"Estimated Price: ${pricing_info}")
    
    st.header("Accommodation Recommendations")
    accommodations = get_accommodation_recommendations(destination)
    st.write("Recommended Accommodations:")
    st.write(accommodations)
    
    if st.button("Confirm Booking"):
        valid = validate_booking(departure_date, destination, seat_class)
        if valid:
            st.success("Booking confirmed!")
        else:
            st.error("Booking validation failed. Please check your inputs.")

elif page == "Dashboard":
    st.title("User Dashboard")
    
    st.header("Upcoming Trips")
    # Sample upcoming trip: 10 days from now for demonstration purposes
    upcoming_trip_date = datetime.today() + timedelta(days=10)
    countdown = upcoming_trip_date - datetime.now()
    st.write(f"Next trip departs in: {countdown.days} days and {countdown.seconds // 3600} hours")
    
    st.header("AI-Based Travel Tips")
    travel_tips = get_ai_travel_tips()
    st.write(travel_tips)
