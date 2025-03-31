Initial setup of the project.

These endpoints will guide you to access our services.

For you to access all these endpoints, you should register and then login.

https://library-management-api-cusm.onrender.com/accounts/register/ -> Register an account with the system.

https://library-management-api-cusm.onrender.com/accounts/login/ -> Enables you to login.

https://library-management-api-cusm.onrender.com/accounts/logout/ -> Enables you to logout.

https://library-management-api-cusm.onrender.com/accounts/user/create/ -> Enables you to create a user though you should be an admin for testing purposes it will be left open.

https://library-management-api-cusm.onrender.com/accounts/users/ -> Enables you to list the available users though you should be an admin.

https://library-management-api-cusm.onrender.com/accounts/user/<int:pk>/ -> Enables you to view the user details.

https://library-management-api-cusm.onrender.com/accounts/user/<int:pk>/update/ -> Enables you to update the user details though this is for admins only.

https://library-management-api-cusm.onrender.com/accounts/user/<int:pk>/delete/ -> Helps you to delete the details of the user, though this is for admins only.

https://library-management-api-cusm.onrender.com/api/books/ -> Lists the books available both with and without copies.

https://library-management-api-cusm.onrender.com/api/check_available_books/ -> Helps you to check the books with available copies only.

https://library-management-api-cusm.onrender.com/api/book/create/ -> Helps you to create a book.

https://library-management-api-cusm.onrender.com/api/book/<int:pk>/ -> Helps you to access the book details.

https://library-management-api-cusm.onrender.com/api/book/<int:pk>/update/  -> Helps you to update the created book. 

https://library-management-api-cusm.onrender.com/api/book/<int:pk>/delete/ -> Helps you to delete the created book.

https://library-management-api-cusm.onrender.com/api/check_out_book/id/ -> Helps you to check out a book.

https://library-management-api-cusm.onrender.com/api/transactions/ -> Helps you to monitor the transactions of the library though for admin user only.




