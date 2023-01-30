from django.urls import path, include
from rest_framework import routers

from borrowing.views import BorrowingViewSet

app_name = "borrowing"


router = routers.DefaultRouter()
router.register("borrowings", BorrowingViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("borrowings/<int:pk>/return/", borrowing_return_book, name="return-book"),
]

# urlpatterns = format_suffix_patterns(
#     [
#         path("", include(router.urls)),
#         path("borrowings/<int:pk>/return/", borrowing_return_book, name="return-book"),
#     ]
# )

# 1. POST: borrowings/ - add new borrowing (when borrow book - inventory should be made -= 1)
# 2. GET: borrowings/?user_id=...&is_active=...- get borrowings by user id
# and whether is borrowing still active or not.
# 3. GET: borrowings/<id>/ - get specific borrowing
# 4. POST: borrowings/<id>/return/ - set actual return date (inventory should be made += 1)
