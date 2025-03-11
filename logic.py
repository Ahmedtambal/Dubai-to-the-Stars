from datetime import datetime

def get_destinations():
    return [
        "Orbital Station Alpha",
        "Lunar Hotel Luna",
        "Mars Colony Beta",
        "International Space Station"
    ]

def get_pricing(destination, seat_class):
    base_prices = {
        "Orbital Station Alpha": 50000,
        "Lunar Hotel Luna": 75000,
        "Mars Colony Beta": 100000,
        "International Space Station": 120000,
    }
    multipliers = {"Economy": 1.0, "Luxury": 1.5, "VIP": 2.0}
    price = base_prices.get(destination, 50000) * multipliers.get(seat_class, 1.0)
    return price

def get_accommodation_recommendations(destination):
    recommendations = {
        "Orbital Station Alpha": "Alpha Suites with zero-gravity spa",
        "Lunar Hotel Luna": "Luna Luxury Lofts with moon views",
        "Mars Colony Beta": "Beta Bunkers with interplanetary connectivity",
        "International Space Station": "ISS Comfort Cabins with panoramic Earth views"
    }
    return recommendations.get(destination, "Standard Space Pod")

def validate_booking(departure_date, destination, seat_class):
    # Validate that the departure date is in the future
    if departure_date < datetime.today().date():
        return False
    if destination not in get_destinations():
        return False
    if seat_class not in ["Economy", "Luxury", "VIP"]:
        return False
    return True

def get_ai_travel_tips():
    # Placeholder AI-based travel tips
    tips = [
        "Pack light for zero-gravity conditions.",
        "Book a window seat for the best views of Earth.",
        "Arrive early to get the most out of pre-flight orientations.",
        "Explore local space cuisine and try the interstellar buffet!"
    ]
    return tips
