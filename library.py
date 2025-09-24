import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def add_member(name, email):
    payload = {
        "name": name,
        "email": email,
    }
    resp = sb.table("members").insert(payload).execute()
    return resp.data

def add_book(title, author, category, stock):
    payload = {
        "title": title,
        "author": author,
        "category": category,
        "stock": stock
    }
    resp = sb.table("books").insert(payload).execute()
    return resp.data

def list_books():
    resp = sb.table("books").select("*").execute()
    books = resp.data

    if not books:
        print("No books found.")
        return

    print("\n=== Book List with Availability ===")
    print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Category':<15} {'Stock':<6}")
    print("-" * 80)
    for book in books:
        print(f"{book['book_id']:<5} {book['title']:<30} {book['author']:<20} {book['category']:<15} {book['stock']:<6}")


if __name__ == "__main__":
    while True:
        print("\n=== Library Management Menu ===")
        print("1. Add a new member")
        print("2. Add a new book")
        print("3.List books")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            name = input("Enter member name: ").strip()
            email = input("Enter member email: ").strip()
            created = add_member(name, email)
            if created:
                print("Inserted member:", created)
            else:
                print("Failed to insert member. Check if email is unique or input is valid.")
        
        elif choice == "2":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            category = input("Enter book category: ").strip()
            stock = int(input("Enter stock quantity: ").strip())
            created = add_book(title, author, category, stock)
            if created:
                print("Inserted book:", created)
            else:
                print("Failed to insert book. Check input values.")
        
        elif choice == "3":
            list_books()
            
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
