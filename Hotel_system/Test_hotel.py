import pytest
from unittest.mock import patch
from Hotel_reservation_agency import Room, Customer, Hotel


@pytest.fixture
def single_room():
    return Room(room_number=101, room_type="Single", price_per_night=100.0, max_guests=1)

@pytest.fixture
def customer():
    return Customer(name="test_user", budget=500.0)

@pytest.fixture
def hotel(single_room):
    my_hotel = Hotel("Oasis")
    my_hotel.add_room_to_hotel(single_room)
    return my_hotel


def test_customer_pay_for_booking_reduces_budget(customer):
    success = customer.pay_for_booking(170.0)
    assert success is True
    assert customer.budget == 330.0

@patch('Hotel_reservation_agency.datetime')
def test_book_room_only_when_available(mock_datetime, hotel, customer, single_room):
    mock_datetime.now.return_value.month = 11
    first_attempt = hotel.book_room_for_customer(customer, room_number=101, nights=1)
    assert first_attempt is True
    assert single_room.is_available is False

    second_attempt = hotel.book_room_for_customer(customer, room_number=101, nights=1)
    assert second_attempt is False
