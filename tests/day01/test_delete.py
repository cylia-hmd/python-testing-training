from restaurant_reviews import RestaurantReviews

def test_delete_existing():
    rr = RestaurantReviews()
    rr.add_review("Bokit i bon", " un bokit pou tout moun epi i bon !" 5)
    result = rr.delete_review("Bokit i bon")
    assert (result == "review not found")
    result2 = rr.get_review("Bokit i bon")
    assert(result2 == "Review not found")
