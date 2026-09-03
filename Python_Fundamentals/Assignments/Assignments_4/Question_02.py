# Q2. Create a class Book with:
#    Attributes: title, author, list_of_reviews
#    Methods: add_review, count_reviews, display_reviews

class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.list_of_reviews = [] # Created an empty list as no reviews are written yet.

    def add_review(self, review):
        self.list_of_reviews.append(review)

    def count_reviews(self):
        return len(self.list_of_reviews)

    def display_review(self):
        if not self.list_of_reviews:
            print("No reviews yet.")
        else:
            print(f"Reviews for '{self.title}' by {self.author}:")
            i = 1
            for review in self.list_of_reviews:
                print(f"{i}. {review}")
                i += 1

# --- Example Usage ---
book1 = Book("Python Fundamentals", "Asif Hussain")

book1.add_review("Excellent explanation")
book1.add_review("Begginer friendly")
book1.add_review("Need some more examples")

print("Total reviews:", book1.count_reviews())
book1.display_review()
